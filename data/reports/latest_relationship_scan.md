# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T10:07:27.422393+00:00`
- Price records: `672`
- Market context records: `6908`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `0.0968` n `192` status `ready` deltaP `-5.2878` edge `0.4468` maxDD `-14.2644`
- `market_context_high->fx_1h` score `-0.1693` n `224` status `ready` deltaP `3.5848` edge `0.0029` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3719` n `224` status `ready` deltaP `3.109` edge `0.0247` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4543` n `224` status `ready` deltaP `4.5953` edge `0.0219` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.612` n `224` status `ready` deltaP `-0.7485` edge `-0.005` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.7314` n `224` status `ready` deltaP `15.3746` edge `0.0101` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7658` n `224` status `ready` deltaP `-0.7298` edge `-0.0022` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8285` n `224` status `ready` deltaP `-3.6944` edge `-0.0048` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3144` n `224` status `ready` deltaP `-1.5789` edge `-0.009` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5678` n `224` status `ready` deltaP `-2.9619` edge `-0.0208` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7302` n `224` status `ready` deltaP `2.3845` edge `-0.0197` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9045` n `224` status `ready` deltaP `5.1612` edge `-0.0206` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1646` n `224` status `ready` deltaP `2.7766` edge `0.0023` maxDD `-5.5324`
- `market_context_high->commodity_24h` score `-2.4575` n `192` status `ready` deltaP `-0.7601` edge `-0.0129` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `-2.7231` n `224` status `ready` deltaP `2.2104` edge `-0.0055` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.8213` n `224` status `ready` deltaP `-0.0871` edge `-0.0284` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0071` n `224` status `ready` deltaP `-7.9704` edge `0.0391` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.1386` n `192` status `ready` deltaP `-5.3031` edge `-0.0059` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.1224` n `224` status `ready` deltaP `2.5588` edge `-0.1357` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.3173` n `192` status `ready` deltaP `-13.2899` edge `-0.1185` maxDD `-28.4043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
