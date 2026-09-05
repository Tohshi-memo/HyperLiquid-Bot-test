# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T06:22:28.118107+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10674`

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

- `risk_on_high->unknown_4h` score `19.492` n `133` status `ready` deltaP `7.779` edge `1.6343` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.492` n `133` status `ready` deltaP `7.779` edge `1.6343` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `8.1691` n `222` status `ready` deltaP `7.3624` edge `0.7047` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.3775` n `37` status `ready` deltaP `25.1783` edge `0.4739` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.334` n `37` status `ready` deltaP `25.0` edge `0.1945` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.8086` n `37` status `ready` deltaP `17.4852` edge `0.2421` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.1664` n `37` status `ready` deltaP `21.7123` edge `0.0579` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8143` n `37` status `ready` deltaP `10.3618` edge `0.1022` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6386` n `37` status `ready` deltaP `13.6835` edge `0.0844` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.3429` n `37` status `ready` deltaP `7.3637` edge `0.0811` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.2245` n `37` status `ready` deltaP `15.3221` edge `0.0133` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.158` n `37` status `ready` deltaP `13.817` edge `0.0237` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `0.9993` n `37` status `ready` deltaP `9.1763` edge `0.0486` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.858` n `37` status `ready` deltaP `7.4654` edge `0.0546` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.1901` n `37` status `ready` deltaP `11.9697` edge `0.0376` maxDD `-3.1244`
- `news_risk_high->crypto_major_24h` score `0.1296` n `37` status `ready` deltaP `12.4109` edge `0.2115` maxDD `-18.2098`
- `risk_on_high->metal_1h` score `0.0973` n `142` status `ready` deltaP `12.3324` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0973` n `142` status `ready` deltaP `12.3324` edge `0.0015` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `-0.0161` n `37` status `ready` deltaP `5.8748` edge `0.0034` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1219` n `142` status `ready` deltaP `4.7968` edge `-0.0029` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
