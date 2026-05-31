# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T16:37:23.402568+00:00`
- Price records: `672`
- Market context records: `2475`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9236`

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

- `market_context_high->unknown_24h` score `5.4142` n `119` status `ready` deltaP `20.8815` edge `0.3448` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.0545` n `136` status `ready` deltaP `20.7406` edge `0.4675` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8527` n `136` status `ready` deltaP `18.0236` edge `0.3819` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1525` n `119` status `ready` deltaP `12.0186` edge `0.5851` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.6241` n `136` status `ready` deltaP `10.3031` edge `0.1687` maxDD `-3.4972`
- `market_context_high->crypto_major_1h` score `0.6766` n `138` status `ready` deltaP `8.3247` edge `0.1203` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.5168` n `138` status `ready` deltaP `6.5999` edge `0.1178` maxDD `-6.1656`
- `market_context_high->index_24h` score `-0.021` n `119` status `ready` deltaP `3.1994` edge `0.075` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0942` n `119` status `ready` deltaP `1.4341` edge `0.6741` maxDD `-43.6595`
- `market_context_high->index_4h` score `-0.1764` n `136` status `ready` deltaP `5.9451` edge `0.0219` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.2762` n `119` status `ready` deltaP `17.8324` edge `0.0108` maxDD `-6.8828`
- `market_context_high->fx_1h` score `-0.382` n `138` status `ready` deltaP `0.0` edge `0.0045` maxDD `-0.278`
- `market_context_high->index_1h` score `-0.4634` n `138` status `ready` deltaP `-1.7421` edge `0.0016` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4908` n `138` status `ready` deltaP `1.2996` edge `0.0224` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.5346` n `138` status `ready` deltaP `0.1974` edge `0.0061` maxDD `-3.0759`
- `market_context_high->commodity_1h` score `-0.5707` n `138` status `ready` deltaP `2.2759` edge `-0.0005` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.6619` n `136` status `ready` deltaP `-1.094` edge `0.0084` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8312` n `138` status `ready` deltaP `-0.1063` edge `0.0153` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8492` n `119` status `ready` deltaP `3.802` edge `0.0043` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-0.9684` n `136` status `ready` deltaP `2.977` edge `0.0382` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
