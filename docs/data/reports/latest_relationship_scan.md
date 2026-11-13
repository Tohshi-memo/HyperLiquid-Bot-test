# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T06:52:31.654890+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `266.4265` n `84` status `ready` deltaP `6.2996` edge `22.1743` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `60.7644` n `94` status `ready` deltaP `6.7333` edge `5.0636` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.8583` n `53` status `ready` deltaP `29.8481` edge `2.5265` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.8409` n `84` status `ready` deltaP `27.5794` edge `1.8735` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.269` n `53` status `ready` deltaP `40.3073` edge `1.629` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.2623` n `84` status `ready` deltaP `48.3383` edge `1.403` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `10.0662` n `53` status `ready` deltaP `34.106` edge `0.7245` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.1634` n `84` status `ready` deltaP `43.8988` edge `0.3456` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.3955` n `53` status `ready` deltaP `40.1042` edge `0.2656` maxDD `0.0`
- `market_context_high->index_24h` score `4.5074` n `84` status `ready` deltaP `25.8929` edge `0.2125` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.4289` n `53` status `ready` deltaP `42.5852` edge `0.1228` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0991` n `53` status `ready` deltaP `24.0959` edge `0.2113` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.3838` n `53` status `ready` deltaP `20.2859` edge `0.2955` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.2122` n `53` status `ready` deltaP `17.5658` edge `0.2136` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1691` n `53` status `ready` deltaP `29.1504` edge `0.0951` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.8246` n `53` status `ready` deltaP `18.4191` edge `0.6899` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.078` n `53` status `ready` deltaP `24.6921` edge `0.034` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9812` n `53` status `ready` deltaP `26.4985` edge `0.2412` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.8192` n `53` status `ready` deltaP `19.0693` edge `0.0681` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1735` n `53` status `ready` deltaP `16.2778` edge `0.0194` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
