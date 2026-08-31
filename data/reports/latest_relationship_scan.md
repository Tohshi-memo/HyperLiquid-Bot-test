# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T08:52:23.829625+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11586`

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

- `risk_on_high->crypto_alt_24h` score `22.107` n `55` status `ready` deltaP `48.7942` edge `1.565` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `22.107` n `55` status `ready` deltaP `48.7942` edge `1.565` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `10.8552` n `55` status `ready` deltaP `31.1238` edge `0.8389` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `10.8552` n `55` status `ready` deltaP `31.1238` edge `0.8389` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.0628` n `107` status `ready` deltaP `25.4032` edge `0.5642` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.0628` n `107` status `ready` deltaP `25.4032` edge `0.5642` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5168` n `159` status `ready` deltaP `22.0998` edge `0.4651` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.4793` n `55` status `ready` deltaP `72.3958` edge `0.0573` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.4793` n `55` status `ready` deltaP `72.3958` edge `0.0573` maxDD `0.0`
- `market_context_high->metal_24h` score `5.2456` n `96` status `ready` deltaP `37.1527` edge `0.2503` maxDD `-1.8678`
- `market_context_high->crypto_major_24h` score `4.9159` n `96` status `ready` deltaP `22.2223` edge `0.5106` maxDD `-17.2607`
- `market_context_high->crypto_alt_24h` score `4.6592` n `96` status `ready` deltaP `23.2639` edge `0.8612` maxDD `-27.517`
- `risk_on_high->metal_24h` score `4.426` n `55` status `ready` deltaP `40.5808` edge `0.1455` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.426` n `55` status `ready` deltaP `40.5808` edge `0.1455` maxDD `-0.7767`
- `risk_on_high->unknown_1h` score `2.4647` n `107` status `ready` deltaP `6.2161` edge `0.2216` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.4647` n `107` status `ready` deltaP `6.2161` edge `0.2216` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2421` n `159` status `ready` deltaP `5.5578` edge `0.2128` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.1541` n `96` status `ready` deltaP `39.0625` edge `0.0334` maxDD `-1.6688`
- `news_risk_high->commodity_24h` score `1.1256` n `44` status `ready` deltaP `11.0322` edge `0.1023` maxDD `-1.1904`
- `risk_on_high->equity_24h` score `1.0695` n `55` status `ready` deltaP `20.625` edge `0.0324` maxDD `-3.7955`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
