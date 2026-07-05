# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T00:07:30.975249+00:00`
- Price records: `672`
- Market context records: `5718`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8874`

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

- `market_context_high->crypto_major_4h` score `1.5375` n `269` status `ready` deltaP `9.9771` edge `0.2019` maxDD `-6.8899`
- `market_context_high->equity_24h` score `1.0052` n `219` status `ready` deltaP `17.0496` edge `0.5231` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.2237` n `269` status `ready` deltaP `7.5007` edge `0.1325` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.0963` n `269` status `ready` deltaP `7.4043` edge `0.1444` maxDD `-9.1921`
- `market_context_high->fx_1h` score `-0.1734` n `281` status `ready` deltaP `3.6999` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4382` n `281` status `ready` deltaP `1.7906` edge `-0.0006` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.4866` n `281` status `ready` deltaP `2.9317` edge `0.0355` maxDD `-3.9811`
- `market_context_high->index_1h` score `-0.6035` n `281` status `ready` deltaP `0.8359` edge `0.0039` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6113` n `281` status `ready` deltaP `3.2929` edge `0.0278` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7432` n `281` status `ready` deltaP `-1.4347` edge `-0.005` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.7701` n `281` status `ready` deltaP `0.9856` edge `0.0302` maxDD `-4.4093`
- `market_context_high->fx_24h` score `-1.1283` n `219` status `ready` deltaP `10.7687` edge `0.0419` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1814` n `269` status `ready` deltaP `0.9696` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2736` n `269` status `ready` deltaP `2.3308` edge `0.0057` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6126` n `269` status `ready` deltaP `-7.1233` edge `-0.0499` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8488` n `219` status `ready` deltaP `2.8848` edge `0.03` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8749` n `269` status `ready` deltaP `-4.0133` edge `-0.0286` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.433` n `219` status `ready` deltaP `6.8065` edge `0.0309` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.5759` n `219` status `ready` deltaP `-5.5841` edge `-0.2372` maxDD `-31.7476`
- `market_context_high->commodity_24h` score `-11.4402` n `219` status `ready` deltaP `-9.5225` edge `-0.0663` maxDD `-44.5521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
