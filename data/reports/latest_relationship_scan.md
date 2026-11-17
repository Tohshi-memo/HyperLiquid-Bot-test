# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T03:37:29.581167+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4404`

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

- `market_context_high->unknown_24h` score `2141.0039` n `59` status `ready` deltaP `3.4483` edge `178.394` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.1236` n `50` status `ready` deltaP `59.7241` edge `4.2661` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.2761` n `50` status `ready` deltaP `36.2759` edge `2.3438` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.617` n `59` status `ready` deltaP `13.3518` edge `1.5081` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.462` n `50` status `ready` deltaP `44.0976` edge `1.0242` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.491` n `59` status `ready` deltaP `37.5979` edge `1.6778` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.3179` n `50` status `ready` deltaP `21.7586` edge `1.5001` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.2493` n `50` status `ready` deltaP `51.1034` edge `0.3771` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.3542` n `50` status `ready` deltaP `45.5172` edge `0.3094` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2593` n `50` status `ready` deltaP `46.3659` edge `0.1668` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5672` n `50` status `ready` deltaP `26.9939` edge `0.3442` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5082` n `50` status `ready` deltaP `22.5449` edge `0.2884` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.3305` n `50` status `ready` deltaP `21.9085` edge `0.3524` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1301` n `50` status `ready` deltaP `37.4878` edge `0.1196` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1066` n `50` status `ready` deltaP `29.0671` edge `0.1001` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2174` n `50` status `ready` deltaP `24.8443` edge `0.0446` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5179` n `50` status `ready` deltaP `19.4431` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.816` n `50` status `ready` deltaP `18.3448` edge `0.1996` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.7656` n `50` status `ready` deltaP `18.8443` edge `0.0777` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7648` n `50` status `ready` deltaP `16.6946` edge `0.0847` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
