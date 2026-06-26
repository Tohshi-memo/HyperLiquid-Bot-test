# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T15:22:26.744561+00:00`
- Price records: `672`
- Market context records: `4840`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7616`

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

- `market_context_high->unknown_1h` score `13.7041` n `109` status `ready` deltaP `10.2703` edge `1.1153` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.3443` n `98` status `ready` deltaP `23.4227` edge `0.8047` maxDD `-3.5727`
- `market_context_high->unknown_24h` score `4.3132` n `94` status `ready` deltaP `21.5204` edge `0.2626` maxDD `-1.7308`
- `market_context_high->crypto_alt_4h` score `1.5907` n `98` status `ready` deltaP `14.5906` edge `0.2473` maxDD `-8.2508`
- `market_context_high->crypto_major_4h` score `1.0155` n `98` status `ready` deltaP `10.8605` edge `0.234` maxDD `-11.4303`
- `market_context_high->index_4h` score `0.2054` n `98` status `ready` deltaP `6.8255` edge `0.0275` maxDD `-0.7334`
- `market_context_high->equity_1h` score `0.1258` n `109` status `ready` deltaP `3.0421` edge `0.0518` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.061` n `98` status `ready` deltaP `7.6002` edge `0.0097` maxDD `-0.788`
- `market_context_high->commodity_4h` score `-0.1175` n `98` status `ready` deltaP `11.9027` edge `0.0228` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.1743` n `98` status `ready` deltaP `8.8197` edge `0.057` maxDD `-6.3852`
- `market_context_high->commodity_1h` score `-0.2131` n `109` status `ready` deltaP `2.1974` edge `0.0187` maxDD `-1.1874`
- `market_context_high->metal_4h` score `-0.4672` n `98` status `ready` deltaP `9.8743` edge `0.0305` maxDD `-9.1643`
- `market_context_high->crypto_alt_1h` score `-0.7951` n `109` status `ready` deltaP `4.8577` edge `0.0189` maxDD `-9.5908`
- `market_context_high->index_1h` score `-0.9618` n `109` status `ready` deltaP `-2.1246` edge `0.0095` maxDD `-0.7054`
- `market_context_high->crypto_major_1h` score `-1.2509` n `109` status `ready` deltaP `2.8155` edge `0.0213` maxDD `-13.3689`
- `market_context_high->fx_1h` score `-1.2887` n `109` status `ready` deltaP `-5.8905` edge `-0.0047` maxDD `-0.7404`
- `market_context_high->metal_1h` score `-1.4534` n `109` status `ready` deltaP `0.0632` edge `-0.0308` maxDD `-9.1432`
- `market_context_high->fx_24h` score `-1.9053` n `94` status `ready` deltaP `-6.9223` edge `-0.0116` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-3.278` n `94` status `ready` deltaP `12.1528` edge `0.0096` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.6473` n `94` status `ready` deltaP `-7.9861` edge `-0.1415` maxDD `-24.085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
