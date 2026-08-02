# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T00:22:27.443316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.7087` n `60` status `ready` deltaP `32.5014` edge `432.2178` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.2735` n `53` status `ready` deltaP `59.5239` edge `1.1657` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8453` n `68` status `ready` deltaP `17.1359` edge `0.3659` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7427` n `68` status `ready` deltaP `16.6786` edge `0.0721` maxDD `-0.3783`
- `market_context_high->commodity_24h` score `1.7267` n `53` status `ready` deltaP `27.4844` edge `0.224` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.7696` n `53` status `ready` deltaP `9.805` edge `0.129` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.7032` n `68` status `ready` deltaP `9.9419` edge `0.0746` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2319` n `53` status `ready` deltaP `14.0158` edge `0.0159` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1235` n `68` status `ready` deltaP `5.165` edge `0.029` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0936` n `68` status `ready` deltaP `6.1818` edge `0.039` maxDD `-3.1233`
- `market_context_high->fx_24h` score `0.0596` n `53` status `ready` deltaP `9.1396` edge `0.0447` maxDD `-2.506`
- `market_context_high->fx_1h` score `-0.0125` n `53` status `ready` deltaP `7.2026` edge `0.0012` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `-0.0211` n `68` status `ready` deltaP `10.7694` edge `0.0222` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.0372` n `68` status `ready` deltaP `2.9148` edge `0.0081` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.0496` n `53` status `ready` deltaP `4.6266` edge `0.0169` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.1097` n `68` status `ready` deltaP `2.0694` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1201` n `68` status `ready` deltaP `2.7651` edge `0.0065` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2233` n `68` status `ready` deltaP `1.77` edge `0.0316` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.2559` n `53` status `ready` deltaP `3.4198` edge `0.0319` maxDD `-3.0005`
- `market_context_high->crypto_alt_1h` score `-0.6176` n `53` status `ready` deltaP `-4.4176` edge `0.013` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
