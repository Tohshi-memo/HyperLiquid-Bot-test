# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T03:37:24.204082+00:00`
- Price records: `672`
- Market context records: `6245`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `14.177` n `32` status `ready` deltaP `42.2194` edge `0.9147` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1109` n `32` status `ready` deltaP `52.0408` edge `0.1623` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1913` n `32` status `ready` deltaP `43.8262` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.241` n `32` status `ready` deltaP `15.625` edge `0.3893` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3248` n `32` status `ready` deltaP `27.994` edge `0.021` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.2315` n `192` status `ready` deltaP `2.4108` edge `0.2707` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `2.1764` n `32` status `ready` deltaP `25.0213` edge `0.0351` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `1.8688` n `192` status `ready` deltaP `0.4446` edge `0.406` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3446` n `32` status `ready` deltaP `14.128` edge `0.1249` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7654` n `32` status `ready` deltaP `10.4229` edge `0.0748` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.1032` n `192` status `ready` deltaP `19.8023` edge `0.1116` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.18` n `32` status `ready` deltaP `8.801` edge `0.0054` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3058` n `192` status `ready` deltaP `0.9107` edge `-0.0007` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.4953` n `192` status `ready` deltaP `4.281` edge `0.0267` maxDD `-3.4996`
- `market_context_high->equity_4h` score `-0.5858` n `192` status `ready` deltaP `2.8201` edge `0.0241` maxDD `-2.671`
- `market_context_high->commodity_1h` score `-0.6817` n `192` status `ready` deltaP `-2.0958` edge `0.0018` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7753` n `32` status `ready` deltaP `-3.5928` edge `-0.0257` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.852` n `192` status `ready` deltaP `1.6155` edge `-0.0019` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8983` n `192` status `ready` deltaP `4.6937` edge `0.0288` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.955` n `192` status `ready` deltaP `4.2322` edge `0.0261` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
