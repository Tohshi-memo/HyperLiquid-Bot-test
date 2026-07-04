# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T10:22:28.796573+00:00`
- Price records: `672`
- Market context records: `5652`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.4809` n `184` status `ready` deltaP `14.855` edge `0.6156` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.7726` n `237` status `ready` deltaP `10.6996` edge `0.2223` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.7183` n `184` status `ready` deltaP `18.9538` edge `0.0576` maxDD `-1.9277`
- `market_context_high->equity_4h` score `0.4989` n `237` status `ready` deltaP `7.6863` edge `0.1542` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.0121` n `237` status `ready` deltaP `6.5266` edge `0.1404` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2563` n `244` status `ready` deltaP `2.0492` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3633` n `244` status `ready` deltaP `5.5978` edge `0.0331` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5586` n `244` status `ready` deltaP `-0.5988` edge `-0.0001` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.7179` n `244` status `ready` deltaP `0.8442` edge `0.0307` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.8014` n `244` status `ready` deltaP `2.9793` edge `0.0379` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9362` n `244` status `ready` deltaP `0.5129` edge `0.0054` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.9627` n `244` status `ready` deltaP `0.0785` edge `-0.0042` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2678` n `237` status `ready` deltaP `2.1328` edge `0.0066` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0233` n `237` status `ready` deltaP `-1.5366` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3402` n `184` status `ready` deltaP `9.4731` edge `0.0355` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0607` n `237` status `ready` deltaP `-14.8265` edge `-0.0552` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.7996` n `237` status `ready` deltaP `-2.1875` edge `-0.0345` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4958` n `184` status `ready` deltaP `4.0761` edge `0.0522` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3963` n `184` status `ready` deltaP `-13.1491` edge `-0.2527` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.8538` n `184` status `ready` deltaP `-15.3533` edge `-0.1079` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
