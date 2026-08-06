# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T01:52:26.824090+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.5392` n `90` status `ready` deltaP `4.4445` edge `1.0196` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.91` n `109` status `ready` deltaP `-2.1076` edge `0.3561` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2156` n `109` status `ready` deltaP `14.209` edge `0.0912` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.808` n `90` status `ready` deltaP `2.0139` edge `0.207` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7877` n `90` status `ready` deltaP `24.5486` edge `0.0579` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3988` n `109` status `ready` deltaP `7.61` edge `0.0241` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0847` n `109` status `ready` deltaP `6.5813` edge `-0.0018` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1368` n `109` status `ready` deltaP `9.0093` edge `0.0084` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5347` n `109` status `ready` deltaP `-1.7099` edge `-0.0077` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6996` n `109` status `ready` deltaP `-2.7578` edge `-0.0179` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8847` n `109` status `ready` deltaP `1.7174` edge `-0.0014` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.2831` n `90` status `ready` deltaP `0.5555` edge `-0.0239` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.4354` n `109` status `ready` deltaP `-4.5391` edge `-0.0183` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7294` n `109` status `ready` deltaP `1.8679` edge `-0.0806` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.7925` n `90` status `ready` deltaP `-5.8681` edge `0.0288` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1589` n `109` status `ready` deltaP `-13.43` edge `-0.0618` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1625` n `109` status `ready` deltaP `0.9272` edge `-0.0474` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-3.2669` n `109` status `ready` deltaP `2.0326` edge `-0.2411` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.2803` n `109` status `ready` deltaP `-11.1493` edge `-0.0617` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0644` n `90` status `ready` deltaP `10.6598` edge `-0.0271` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
