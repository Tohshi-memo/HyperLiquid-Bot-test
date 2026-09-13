# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T21:52:30.866701+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `11532.4092` n `56` status `ready` deltaP `10.2093` edge `960.9862` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `1828.7647` n `34` status `ready` deltaP `10.3144` edge `152.3348` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `1828.7647` n `34` status `ready` deltaP `10.3144` edge `152.3348` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `436.0816` n `82` status `ready` deltaP `-5.4002` edge `36.4183` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.7159` n `82` status `ready` deltaP `36.2027` edge `1.3671` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.2908` n `82` status `ready` deltaP `38.0236` edge `1.4178` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.9424` n `82` status `ready` deltaP `29.5122` edge `0.8098` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.3928` n `82` status `ready` deltaP `53.2842` edge `0.2785` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.8791` n `82` status `ready` deltaP `27.6914` edge `0.2674` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.877` n `34` status `ready` deltaP `39.8276` edge `0.1409` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.877` n `34` status `ready` deltaP `39.8276` edge `0.1409` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.769` n `56` status `ready` deltaP `39.8276` edge `0.1319` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `3.5043` n `56` status `ready` deltaP `5.0616` edge `0.4244` maxDD `-9.6226`
- `risk_on_high->crypto_alt_24h` score `3.1505` n `34` status `ready` deltaP `0.3347` edge `0.3939` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `3.1505` n `34` status `ready` deltaP `0.3347` edge `0.3939` maxDD `-7.0204`
- `risk_on_high->fx_24h` score `2.5796` n `34` status `ready` deltaP `50.1115` edge `0.0312` maxDD `-0.7642`
- `risk_on_and_context->fx_24h` score `2.5796` n `34` status `ready` deltaP `50.1115` edge `0.0312` maxDD `-0.7642`
- `risk_on_high->commodity_4h` score `1.5221` n `56` status `ready` deltaP `21.6028` edge `0.0178` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.5221` n `56` status `ready` deltaP `21.6028` edge `0.0178` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.1063` n `129` status `ready` deltaP `17.6853` edge `0.0161` maxDD `-0.345`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
