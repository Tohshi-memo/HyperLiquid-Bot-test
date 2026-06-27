# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T11:52:34.778931+00:00`
- Price records: `672`
- Market context records: `4930`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9400`

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

- `market_context_high->unknown_1h` score `16.7996` n `103` status `ready` deltaP `10.4892` edge `1.3718` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.2423` n `103` status `ready` deltaP `28.9619` edge `0.7952` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `7.1847` n `103` status `ready` deltaP `24.1875` edge `0.5727` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.7239` n `103` status `ready` deltaP `19.2206` edge `0.5546` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.9976` n `86` status `ready` deltaP `26.5141` edge `0.3573` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3603` n `103` status `ready` deltaP `10.2579` edge `0.1112` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.9922` n `103` status `ready` deltaP `13.1631` edge `0.1776` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.6778` n `103` status `ready` deltaP `9.2633` edge `0.0409` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.4448` n `103` status `ready` deltaP `5.4255` edge `0.1247` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.3654` n `103` status `ready` deltaP `5.7889` edge `0.0656` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.2672` n `103` status `ready` deltaP `6.1653` edge `0.0954` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0377` n `103` status `ready` deltaP `3.2614` edge `0.0331` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2174` n `103` status `ready` deltaP `3.3297` edge `0.0159` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5089` n `103` status `ready` deltaP `-0.1134` edge `0.011` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7062` n `103` status `ready` deltaP `8.1474` edge `0.0055` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.908` n `103` status `ready` deltaP `-2.6359` edge `-0.0018` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.5083` n `103` status `ready` deltaP `-8.9152` edge `-0.005` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.9739` n `86` status `ready` deltaP `-7.0293` edge `-0.0166` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.9338` n `86` status `ready` deltaP `-9.9281` edge `-0.1578` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.0616` n `86` status `ready` deltaP `12.9724` edge `0.0026` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
