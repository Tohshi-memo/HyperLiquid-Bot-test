# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T15:37:39.792953+00:00`
- Price records: `672`
- Market context records: `5157`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5612`

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

- `market_context_high->unknown_24h` score `30.2715` n `63` status `ready` deltaP `34.2758` edge `2.3131` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `6.2348` n `134` status `ready` deltaP `19.9331` edge `0.4889` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.8723` n `134` status `ready` deltaP `15.021` edge `0.4658` maxDD `-9.46`
- `market_context_high->crypto_alt_24h` score `4.8325` n `63` status `ready` deltaP `19.7173` edge `0.8268` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.6076` n `63` status `ready` deltaP `17.9067` edge `0.8375` maxDD `-22.6266`
- `market_context_high->unknown_1h` score `4.5759` n `145` status `ready` deltaP `9.7915` edge `0.3802` maxDD `-2.7986`
- `market_context_high->crypto_major_4h` score `3.9595` n `134` status `ready` deltaP `13.6808` edge `0.468` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `2.0237` n `63` status `ready` deltaP `20.2381` edge `0.157` maxDD `-5.1955`
- `market_context_high->metal_24h` score `0.9567` n `63` status `ready` deltaP `0.9424` edge `0.2472` maxDD `-5.4668`
- `market_context_high->crypto_major_1h` score `0.764` n `145` status `ready` deltaP `7.7121` edge `0.1368` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.732` n `145` status `ready` deltaP `5.2581` edge `0.1221` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.6172` n `134` status `ready` deltaP `8.9552` edge `0.1556` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.0832` n `145` status `ready` deltaP `6.8191` edge `0.058` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0975` n `145` status `ready` deltaP `3.9108` edge `0.0118` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1083` n `145` status `ready` deltaP `4.5364` edge `0.0143` maxDD `-2.0075`
- `market_context_high->fx_1h` score `-0.1743` n `145` status `ready` deltaP `3.344` edge `0.0006` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4218` n `134` status `ready` deltaP `4.2842` edge `0.0291` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.4439` n `63` status `ready` deltaP `6.6965` edge `0.0079` maxDD `-0.8294`
- `market_context_high->fx_4h` score `-0.5556` n `134` status `ready` deltaP `3.8042` edge `0.0068` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6113` n `145` status `ready` deltaP `0.4037` edge `-0.0002` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
