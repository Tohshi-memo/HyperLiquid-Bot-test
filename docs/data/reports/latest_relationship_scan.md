# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T12:22:30.879570+00:00`
- Price records: `672`
- Market context records: `5980`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.337` n `30` status `ready` deltaP `67.1875` edge `0.1635` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.7638` n `30` status `ready` deltaP `35.1042` edge `0.1835` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.0254` n `30` status `ready` deltaP `41.6768` edge `0.0622` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1508` n `30` status `ready` deltaP `25.8782` edge `0.0206` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.241` n `238` status `ready` deltaP `8.1843` edge `0.1583` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7296` n `30` status `ready` deltaP `9.5908` edge `0.0763` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.0852` n `30` status `ready` deltaP `4.7206` edge `0.0256` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.043` n `30` status `ready` deltaP `9.2361` edge `0.0311` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.4297` n `240` status `ready` deltaP `3.7575` edge `0.0327` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.4398` n `30` status `ready` deltaP `1.2375` edge `-0.028` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4679` n `240` status `ready` deltaP `-1.3024` edge `0.003` maxDD `-1.3445`
- `market_context_high->metal_1h` score `-0.5184` n `240` status `ready` deltaP `2.0709` edge `-0.0004` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.6917` n `240` status `ready` deltaP `-0.7884` edge `-0.0007` maxDD `-0.8015`
- `market_context_high->index_1h` score `-0.7023` n `240` status `ready` deltaP `-0.4491` edge `0.0043` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-1.1046` n `213` status `ready` deltaP `20.9752` edge `0.3049` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.1069` n `30` status `ready` deltaP `-10.4491` edge `-0.0208` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.1318` n `238` status `ready` deltaP `0.7698` edge `0.0185` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.1491` n `240` status `ready` deltaP `2.0908` edge `0.0155` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.202` n `240` status `ready` deltaP `1.3872` edge `0.0119` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4038` n `238` status `ready` deltaP `-1.0453` edge `-0.0047` maxDD `-6.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
