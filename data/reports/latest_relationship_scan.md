# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T22:14:32.370038+00:00`
- Price records: `672`
- Market context records: `3117`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7023`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->commodity_24h` score `14.6623` n `95` status `ready` deltaP `46.6027` edge `0.954` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `13.0801` n `95` status `ready` deltaP `11.2664` edge `2.3813` maxDD `-53.6916`
- `market_context_high->unknown_24h` score `12.8655` n `95` status `ready` deltaP `22.3391` edge `0.972` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.3175` n `95` status `ready` deltaP `32.5713` edge `0.8981` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.4869` n `95` status `ready` deltaP `13.6878` edge `1.3266` maxDD `-47.1525`
- `market_context_high->commodity_4h` score `2.9964` n `121` status `ready` deltaP `18.1944` edge `0.1742` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0196` n `133` status `ready` deltaP `2.4886` edge `0.0273` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3997` n `133` status `ready` deltaP `5.1799` edge `0.0205` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5535` n `95` status `ready` deltaP `4.0552` edge `-0.0004` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.725` n `133` status `ready` deltaP `3.8258` edge `0.0945` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.0223` n `133` status `ready` deltaP `0.9781` edge `0.011` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3674` n `121` status `ready` deltaP `-13.0266` edge `-0.0041` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4067` n `121` status `ready` deltaP `9.8329` edge `0.045` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.6627` n `133` status `ready` deltaP `-10.4565` edge `-0.0056` maxDD `-0.7266`
- `market_context_high->crypto_major_1h` score `-2.046` n `133` status `ready` deltaP `-0.2567` edge `0.0575` maxDD `-15.1032`
- `market_context_high->unknown_4h` score `-2.119` n `121` status `ready` deltaP `3.6472` edge `0.0021` maxDD `-13.9067`
- `market_context_high->metal_1h` score `-2.2161` n `133` status `ready` deltaP `-5.656` edge `-0.0076` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.7704` n `133` status `ready` deltaP `3.101` edge `-0.0489` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.9196` n `121` status `ready` deltaP `12.1749` edge `0.2208` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0174` n `121` status `ready` deltaP `6.2865` edge `-0.0264` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
