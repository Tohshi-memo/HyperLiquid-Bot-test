# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T07:22:31.375134+00:00`
- Price records: `672`
- Market context records: `4910`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9464`

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

- `market_context_high->unknown_1h` score `14.5831` n `110` status `ready` deltaP `9.8721` edge `1.1912` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.6684` n `110` status `ready` deltaP `23.3148` edge `0.7034` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.6367` n `110` status `ready` deltaP `22.1231` edge `0.5408` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4744` n `110` status `ready` deltaP `19.102` edge `0.5346` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.3052` n `92` status `ready` deltaP `23.6338` edge `0.3188` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1466` n `110` status `ready` deltaP `8.3675` edge `0.106` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8179` n `110` status `ready` deltaP `11.372` edge `0.1672` maxDD `-6.3852`
- `market_context_high->crypto_major_1h` score `0.5326` n `110` status `ready` deltaP `6.9189` edge `0.126` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.505` n `110` status `ready` deltaP `10.6208` edge `0.0402` maxDD `-0.7006`
- `market_context_high->crypto_alt_1h` score `0.4542` n `110` status `ready` deltaP `8.3206` edge `0.105` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2433` n `110` status `ready` deltaP `4.6843` edge `0.0597` maxDD `-2.779`
- `market_context_high->commodity_1h` score `-0.195` n `110` status `ready` deltaP `3.7316` edge `0.0161` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2087` n `110` status `ready` deltaP `0.0952` edge `0.0306` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5335` n `110` status `ready` deltaP `-0.5879` edge `0.011` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7368` n `110` status `ready` deltaP `-0.1524` edge `0.0036` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.7941` n `110` status `ready` deltaP `7.0343` edge `0.0056` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.4017` n `110` status `ready` deltaP `-7.6157` edge `-0.0047` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.55` n `92` status `ready` deltaP `-3.2156` edge `-0.0067` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.4181` n `92` status `ready` deltaP `17.6555` edge `0.025` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.5807` n `92` status `ready` deltaP `-6.2123` edge `-0.1373` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
