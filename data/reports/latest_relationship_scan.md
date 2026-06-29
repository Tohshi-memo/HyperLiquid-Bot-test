# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T16:52:27.017871+00:00`
- Price records: `672`
- Market context records: `5162`
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

- `market_context_high->unknown_24h` score `29.9993` n `63` status `ready` deltaP `33.4077` edge `2.2962` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `6.0249` n `138` status `ready` deltaP `19.9496` edge `0.4713` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.6089` n `138` status `ready` deltaP `14.4132` edge `0.4479` maxDD `-9.46`
- `market_context_high->crypto_alt_24h` score `4.5273` n `63` status `ready` deltaP `19.0229` edge `0.7923` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.2559` n `63` status `ready` deltaP `17.0386` edge `0.7982` maxDD `-22.6266`
- `market_context_high->unknown_1h` score `3.8805` n `149` status `ready` deltaP `10.0983` edge `0.3202` maxDD `-2.7986`
- `market_context_high->crypto_major_4h` score `3.8041` n `138` status `ready` deltaP `13.2689` edge `0.4578` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `2.0369` n `63` status `ready` deltaP `20.2381` edge `0.1581` maxDD `-5.1955`
- `market_context_high->metal_24h` score `0.9372` n `63` status `ready` deltaP `0.9424` edge `0.2447` maxDD `-5.4668`
- `market_context_high->crypto_major_1h` score `0.8476` n `149` status `ready` deltaP `8.0376` edge `0.1416` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.8142` n `149` status `ready` deltaP `5.4153` edge `0.1279` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.4687` n `138` status `ready` deltaP `7.8186` edge `0.1508` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.3103` n `149` status `ready` deltaP `7.7231` edge `0.0709` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0214` n `149` status `ready` deltaP `5.1883` edge `0.014` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1054` n `149` status `ready` deltaP `4.6769` edge `0.0145` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2038` n `149` status `ready` deltaP `2.7931` edge `0.0005` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4412` n `138` status `ready` deltaP `4.001` edge `0.0285` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.494` n `138` status `ready` deltaP `4.8847` edge `0.0075` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.541` n `149` status `ready` deltaP `1.4558` edge `0.0018` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-0.5457` n `63` status `ready` deltaP `5.8284` edge `0.0052` maxDD `-0.8294`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
