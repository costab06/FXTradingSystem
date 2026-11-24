# Selective migration plan

## Principles

- New application owns its code; no wholesale repository merges.
- Copy or translate one capability at a time with its required dependencies.
- Preserve original repository attribution and license obligations.
- Use OAF as a dependency; do not duplicate its event bus, checkpointing, or recovery logic.
- Separate quantitative signals from broker execution.
- Require deterministic pre-trade risk checks and broker reconciliation.
- Validate migrated behavior locally, without a comprehensive audit of the source repositories.

## Sequence

1. **FXMarket**: FX instrument/quote models and a historical feed.
2. **forex_stat_arb**: translate R cointegration, pair selection, features and signals into Python.
3. **FXMarket**: adapt the backtest engine for multi-pair portfolio accounting.
4. **FXAgents**: selectively migrate analysts and debate orchestration; remove duplicate market/feed code.
5. **OpenAgentFabric**: wire durable research workflows to application services.
6. **Execution**: add paper brokerage, idempotent order intents, reconciliation, and hard risk limits.

## Design boundaries

- No LLM or research agent may directly submit a live broker order.
- An unknown broker submission result is reconciled, not blindly retried.
- A statistical arbitrage signal is a multi-instrument target, not a single buy/sell command.
- FX market-data quotes are not automatically executable prices.
