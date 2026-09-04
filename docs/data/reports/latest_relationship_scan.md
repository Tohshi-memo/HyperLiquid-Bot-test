# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T17:07:27.372851+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10784`

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

- `risk_on_high->unknown_4h` score `19.5166` n `133` status `ready` deltaP `7.3216` edge `1.6394` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5166` n `133` status `ready` deltaP `7.3216` edge `1.6394` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.4381` n `133` status `ready` deltaP `-1.8021` edge `1.0229` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.4381` n `133` status `ready` deltaP `-1.8021` edge `1.0229` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.189` n `212` status `ready` deltaP `9.1233` edge `0.8578` maxDD `-2.563`
- `market_context_high->unknown_1h` score `9.0277` n `214` status `ready` deltaP `-0.8605` edge `0.8211` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `2.8172` n `50` status `ready` deltaP `18.9792` edge `0.1352` maxDD `-0.8236`
- `news_risk_high->commodity_4h` score `1.7146` n `50` status `ready` deltaP `13.6159` edge `0.0722` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `1.7093` n `50` status `ready` deltaP `12.125` edge `0.0788` maxDD `-0.042`
- `news_risk_high->equity_1h` score `0.7298` n `50` status `ready` deltaP `11.9162` edge `0.0532` maxDD `-0.7924`
- `news_risk_high->metal_4h` score `0.6171` n `50` status `ready` deltaP `10.6646` edge `0.0343` maxDD `-0.7692`
- `news_risk_high->crypto_major_4h` score `0.6074` n `50` status `ready` deltaP `6.2073` edge `0.1106` maxDD `-3.5957`
- `news_risk_high->index_1h` score `0.5555` n `50` status `ready` deltaP `11.4551` edge `0.0086` maxDD `-0.1`
- `news_risk_high->fx_4h` score `0.1529` n `50` status `ready` deltaP `9.6037` edge `0.0008` maxDD `-0.9514`
- `risk_on_high->metal_1h` score `0.1101` n `133` status `ready` deltaP `12.5625` edge `0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1101` n `133` status `ready` deltaP `12.5625` edge `0.0016` maxDD `-1.699`
- `news_risk_high->metal_1h` score `0.0956` n `50` status `ready` deltaP `4.6527` edge `0.0059` maxDD `-0.6397`
- `news_risk_high->commodity_1h` score `-0.0977` n `50` status `ready` deltaP `5.4132` edge `0.0004` maxDD `-0.9036`
- `news_risk_high->equity_24h` score `-0.1376` n `50` status `ready` deltaP `3.2361` edge `0.0741` maxDD `-5.0655`
- `risk_on_high->index_1h` score `-0.2136` n `133` status `ready` deltaP `3.0942` edge `-0.0035` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
