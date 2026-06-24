# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T00:52:29.003903+00:00`
- Price records: `672`
- Market context records: `4571`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9991`

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

- `market_context_high->unknown_1h` score `69.8263` n `157` status `ready` deltaP `6.2856` edge `5.827` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `2.9907` n `157` status `ready` deltaP `7.15` edge `0.3226` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5238` n `157` status `ready` deltaP `5.8334` edge `0.0022` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6176` n `157` status `ready` deltaP `1.2491` edge `0.0198` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.7045` n `157` status `ready` deltaP `2.1147` edge `0.0725` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-0.7105` n `157` status `ready` deltaP `-2.1883` edge `0.0222` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-0.725` n `157` status `ready` deltaP `-0.2479` edge `-0.0033` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.7985` n `157` status `ready` deltaP `2.806` edge `-0.0088` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1759` n `157` status `ready` deltaP `3.6614` edge `0.0356` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6067` n `157` status `ready` deltaP `-3.1246` edge `-0.0122` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9525` n `157` status `ready` deltaP `-4.554` edge `-0.083` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-3.0774` n `155` status `ready` deltaP `1.5278` edge `-0.1743` maxDD `-4.7201`
- `market_context_high->fx_24h` score `-5.4362` n `155` status `ready` deltaP `-13.3782` edge `-0.0126` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.4864` n `155` status `ready` deltaP `-8.5809` edge `-0.1087` maxDD `-29.3321`
- `market_context_high->crypto_alt_1h` score `-5.4956` n `157` status `ready` deltaP `-2.6755` edge `-0.1114` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.8077` n `155` status `ready` deltaP `8.3815` edge `0.0446` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.7147` n `157` status `ready` deltaP `-5.9365` edge `-0.1447` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.0137` n `157` status `ready` deltaP `-3.4925` edge `-0.2666` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2698` n `157` status `ready` deltaP `-8.5822` edge `-0.3377` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.7973` n `157` status `ready` deltaP `-2.3546` edge `-0.4024` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
