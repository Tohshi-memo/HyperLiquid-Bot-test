# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T10:37:36.771288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1252.3258` n `149` status `ready` deltaP `-2.0216` edge `104.4667` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `31.916` n `149` status `ready` deltaP `4.9947` edge `2.6416` maxDD `-0.5521`
- `market_context_high->index_24h` score `0.5277` n `149` status `ready` deltaP `17.9204` edge `-0.0067` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1158` n `149` status `ready` deltaP `6.6702` edge `0.001` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.1133` n `149` status `ready` deltaP `10.2503` edge `0.0441` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1322` n `149` status `ready` deltaP `7.7282` edge `0.0062` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.138` n `149` status `ready` deltaP `6.7718` edge `0.0032` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.4442` n `149` status `ready` deltaP `5.4827` edge `0.0348` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.4919` n `149` status `ready` deltaP `1.1564` edge `0.0097` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.8107` n `149` status `ready` deltaP `7.8368` edge `-0.0021` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.8605` n `149` status `ready` deltaP `-5.5701` edge `-0.0049` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-1.4279` n `149` status `ready` deltaP `4.3857` edge `0.009` maxDD `-1.2451`
- `market_context_high->equity_1h` score `-1.5363` n `149` status `ready` deltaP `-0.4079` edge `-0.003` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6811` n `149` status `ready` deltaP `1.3985` edge `0.0115` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1414` n `149` status `ready` deltaP `-10.0937` edge `-0.0323` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.3613` n `149` status `ready` deltaP `2.5946` edge `-0.0163` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-3.7045` n `149` status `ready` deltaP `-2.2686` edge `0.0259` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.9701` n `149` status `ready` deltaP `-0.5069` edge `-0.0211` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-5.4612` n `149` status `ready` deltaP `-4.3921` edge `-0.1475` maxDD `-35.2032`
- `market_context_high->equity_24h` score `-5.9573` n `149` status `ready` deltaP `1.813` edge `-0.2121` maxDD `-15.7143`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
