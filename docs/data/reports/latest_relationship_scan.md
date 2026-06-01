# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T01:22:22.417371+00:00`
- Price records: `672`
- Market context records: `2515`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->unknown_24h` score `5.0147` n `119` status `ready` deltaP `19.548` edge `0.3204` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.7357` n `151` status `ready` deltaP `21.5756` edge `0.5187` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9223` n `151` status `ready` deltaP `17.8596` edge `0.3888` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2172` n `119` status `ready` deltaP `11.4627` edge `0.5971` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.0563` n `151` status `ready` deltaP `11.5843` edge `0.1991` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.9876` n `162` status `ready` deltaP `8.2853` edge `0.1458` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6094` n `162` status `ready` deltaP `7.7992` edge `0.1182` maxDD `-4.2199`
- `market_context_high->index_24h` score `-0.0234` n `119` status `ready` deltaP `3.1994` edge `0.0748` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0319` n `119` status `ready` deltaP `0.8782` edge `0.6858` maxDD `-43.6595`
- `market_context_high->index_4h` score `-0.1397` n `151` status `ready` deltaP `6.7214` edge `0.0277` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.1706` n `119` status `ready` deltaP `17.8324` edge `0.0196` maxDD `-6.8828`
- `market_context_high->commodity_1h` score `-0.3859` n `162` status `ready` deltaP `3.9089` edge `0.0123` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4362` n `162` status `ready` deltaP `1.8334` edge `0.0049` maxDD `-0.278`
- `market_context_high->index_1h` score `-0.4483` n `162` status `ready` deltaP `0.8021` edge `0.0067` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.457` n `162` status `ready` deltaP `1.0294` edge `0.0105` maxDD `-3.0759`
- `market_context_high->unknown_1h` score `-0.5612` n `162` status `ready` deltaP `1.7391` edge `0.0136` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.7964` n `119` status `ready` deltaP `4.1214` edge `0.0055` maxDD `-2.4729`
- `market_context_high->equity_1h` score `-0.8401` n `162` status `ready` deltaP `-0.2476` edge `0.0155` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9351` n `151` status `ready` deltaP `-0.3836` edge `0.0106` maxDD `-0.8774`
- `market_context_high->commodity_4h` score `-1.0553` n `151` status `ready` deltaP `3.4001` edge `0.0363` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
