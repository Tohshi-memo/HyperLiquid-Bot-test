# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T03:22:34.414159+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4392`

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

- `market_context_high->unknown_24h` score `2152.0775` n `59` status `ready` deltaP `3.4483` edge `179.3168` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.0558` n `50` status `ready` deltaP `59.5517` edge `4.2616` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.3358` n `50` status `ready` deltaP `36.4483` edge `2.3503` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.6524` n `59` status `ready` deltaP `13.5242` edge `1.5099` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.4848` n `50` status `ready` deltaP `44.0976` edge `1.0261` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.5507` n `59` status `ready` deltaP `37.7703` edge `1.6843` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.3409` n `50` status `ready` deltaP `21.931` edge `1.5019` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.2295` n `50` status `ready` deltaP `50.931` edge `0.3766` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.3164` n `50` status `ready` deltaP `45.3448` edge `0.3074` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2629` n `50` status `ready` deltaP `46.3659` edge `0.1671` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.578` n `50` status `ready` deltaP `26.9939` edge `0.3451` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5214` n `50` status `ready` deltaP `22.5449` edge `0.2895` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.3426` n `50` status `ready` deltaP `21.9085` edge `0.3534` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1143` n `50` status `ready` deltaP `37.3354` edge `0.1193` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1078` n `50` status `ready` deltaP `29.0671` edge `0.1002` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2305` n `50` status `ready` deltaP `24.994` edge `0.0447` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5311` n `50` status `ready` deltaP `19.5928` edge `0.0271` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8207` n `50` status `ready` deltaP `18.3448` edge `0.2002` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.7882` n `50` status `ready` deltaP `18.994` edge `0.0796` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7851` n `50` status `ready` deltaP `16.8443` edge `0.0863` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
