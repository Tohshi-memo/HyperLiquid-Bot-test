# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T14:22:32.635281+00:00`
- Price records: `672`
- Market context records: `5360`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `12.163` n `168` status `ready` deltaP `17.3611` edge `0.911` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.122` n `168` status `ready` deltaP `21.9991` edge `0.7342` maxDD `-29.6555`
- `market_context_high->equity_24h` score `3.9554` n `168` status `ready` deltaP `16.8155` edge `0.7804` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.2405` n `194` status `ready` deltaP `12.8788` edge `0.3301` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.8514` n `194` status `ready` deltaP `9.4449` edge `0.2554` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.5716` n `194` status `ready` deltaP `9.635` edge `0.2306` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.6975` n `168` status `ready` deltaP `22.8919` edge `0.1003` maxDD `-7.413`
- `market_context_high->fx_24h` score `0.17` n `168` status `ready` deltaP `10.0199` edge `0.0369` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.1473` n `204` status `ready` deltaP `6.2258` edge `0.0673` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.11` n `204` status `ready` deltaP `4.5321` edge `0.1035` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0539` n `204` status `ready` deltaP `2.1369` edge `0.0864` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.1079` n `204` status `ready` deltaP `4.7669` edge `0.0096` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4196` n `194` status `ready` deltaP `5.6119` edge `0.0247` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.4606` n `204` status `ready` deltaP `-1.3062` edge `-0.0014` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.6091` n `204` status `ready` deltaP `0.9393` edge `0.0105` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6581` n `194` status `ready` deltaP `2.2881` edge `0.0033` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2425` n `194` status `ready` deltaP `7.7555` edge `-0.037` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.5494` n `204` status `ready` deltaP `-4.1388` edge `-0.0081` maxDD `-3.4738`
- `market_context_high->metal_4h` score `-2.8125` n `194` status `ready` deltaP `-8.7487` edge `-0.0498` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.7691` n `168` status `ready` deltaP `12.0288` edge `0.3063` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
