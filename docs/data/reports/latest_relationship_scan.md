# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T05:37:26.283607+00:00`
- Price records: `672`
- Market context records: `4902`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9592`

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

- `market_context_high->unknown_1h` score `14.4752` n `110` status `ready` deltaP `9.1236` edge `1.1872` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.6096` n `110` status `ready` deltaP `23.3148` edge `0.6985` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.5655` n `110` status `ready` deltaP `21.8182` edge `0.5369` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4454` n `110` status `ready` deltaP `18.9495` edge `0.5332` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2824` n `92` status `ready` deltaP `23.6338` edge `0.3169` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1223` n `110` status `ready` deltaP `8.0627` edge `0.106` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8842` n `110` status `ready` deltaP `12.2866` edge `0.1696` maxDD `-6.3852`
- `market_context_high->crypto_major_1h` score `0.5544` n `110` status `ready` deltaP `7.2183` edge `0.1268` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.5145` n `110` status `ready` deltaP `10.7733` edge `0.0404` maxDD `-0.7006`
- `market_context_high->crypto_alt_1h` score `0.4869` n `110` status `ready` deltaP `8.7697` edge `0.1062` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2581` n `110` status `ready` deltaP `4.834` edge `0.0606` maxDD `-2.779`
- `market_context_high->commodity_1h` score `-0.2113` n `110` status `ready` deltaP `3.4322` edge `0.016` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2172` n `110` status `ready` deltaP `-0.0545` edge `0.0305` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5079` n `110` status `ready` deltaP `-0.1388` edge `0.0113` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7383` n `110` status `ready` deltaP `-0.1524` edge `0.0034` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.7491` n `110` status `ready` deltaP `7.4916` edge `0.0063` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3729` n `110` status `ready` deltaP `-7.3163` edge `-0.0043` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.5651` n `92` status `ready` deltaP `-3.3892` edge `-0.0068` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5301` n `92` status `ready` deltaP `-5.3442` edge `-0.1366` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.5459` n `92` status `ready` deltaP `16.6138` edge `0.0213` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
