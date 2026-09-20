# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T20:07:28.107560+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10418`

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

- `news_risk_high->crypto_major_24h` score `23.9687` n `98` status `ready` deltaP `11.7489` edge `2.6049` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3926` n `98` status `ready` deltaP `15.2671` edge `2.0857` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `14.3728` n `44` status `ready` deltaP `-0.4158` edge `1.2155` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `4.892` n `101` status `ready` deltaP `21.5105` edge `0.3852` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.2336` n `44` status `ready` deltaP `38.1791` edge `0.1116` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `3.8499` n `101` status `ready` deltaP `20.5958` edge `0.3093` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.9189` n `101` status `ready` deltaP `16.8302` edge `0.1776` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1875` n `101` status `ready` deltaP `18.6266` edge `0.1104` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.7606` n `44` status `ready` deltaP `24.3626` edge `0.0103` maxDD `-0.0801`
- `news_risk_high->commodity_24h` score `1.0339` n `98` status `ready` deltaP `22.775` edge `0.1113` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8889` n `55` status `ready` deltaP `12.9314` edge `0.0058` maxDD `-0.1012`
- `market_context_high->commodity_1h` score `0.7522` n `55` status `ready` deltaP `13.6581` edge `0.0329` maxDD `-0.2012`
- `news_risk_high->metal_4h` score `0.6142` n `101` status `ready` deltaP `17.0988` edge `0.0426` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6053` n `101` status `ready` deltaP `14.2986` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.5074` n `98` status `ready` deltaP `16.3974` edge `0.0739` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.3761` n `55` status `ready` deltaP `8.9521` edge `0.0065` maxDD `-0.4538`
- `news_risk_high->equity_1h` score `0.2292` n `101` status `ready` deltaP `5.364` edge `0.0239` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `0.1615` n `101` status `ready` deltaP `8.1834` edge `0.0225` maxDD `-0.421`
- `news_risk_high->metal_24h` score `0.1238` n `98` status `ready` deltaP `14.9837` edge `0.0004` maxDD `-2.4203`
- `news_risk_high->fx_1h` score `-0.2927` n `101` status `ready` deltaP `2.0943` edge `0.006` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
