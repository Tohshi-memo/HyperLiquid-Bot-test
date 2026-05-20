# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T21:52:18.607221+00:00`
- Price records: `672`
- Market context records: `1360`
- Flow alert records: `5829`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.3368` n `134` status `ready` deltaP `32.6233` edge `1.0071` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.681` n `134` status `ready` deltaP `12.925` edge `1.1373` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.8832` n `134` status `ready` deltaP `28.4904` edge `0.8353` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1442` n `134` status `ready` deltaP `23.2328` edge `0.2991` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8514` n `134` status `ready` deltaP `16.1847` edge `0.3624` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3037` n `159` status `ready` deltaP `12.1155` edge `0.1817` maxDD `-3.6396`
- `market_context_high->fx_24h` score `1.2052` n `134` status `ready` deltaP `13.8785` edge `0.0562` maxDD `-0.5297`
- `market_context_high->commodity_24h` score `0.8004` n `134` status `ready` deltaP `-9.6056` edge `0.3617` maxDD `-13.477`
- `market_context_high->metal_4h` score `0.1949` n `159` status `ready` deltaP `13.1606` edge `0.0716` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.0449` n `171` status `ready` deltaP `5.0181` edge `0.0157` maxDD `-1.6329`
- `market_context_high->equity_1h` score `0.0129` n `171` status `ready` deltaP `2.6369` edge `0.0281` maxDD `-1.9017`
- `market_context_high->index_4h` score `0.0092` n `159` status `ready` deltaP `5.0822` edge `0.0762` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.1912` n `171` status `ready` deltaP `6.7628` edge `0.0004` maxDD `-2.9335`
- `market_context_high->fx_1h` score `-0.3193` n `171` status `ready` deltaP `1.42` edge `-0.0039` maxDD `-0.3865`
- `market_context_high->commodity_1h` score `-0.5091` n `171` status `ready` deltaP `0.8492` edge `0.0134` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8335` n `171` status `ready` deltaP `-0.3904` edge `0.0202` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1243` n `171` status `ready` deltaP `-3.1227` edge `-0.0168` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.3393` n `159` status `ready` deltaP `8.0917` edge `0.1664` maxDD `-19.5565`
- `market_context_high->unknown_24h` score `-1.433` n `134` status `ready` deltaP `-4.1174` edge `0.181` maxDD `-10.1706`
- `market_context_high->unknown_4h` score `-1.7226` n `159` status `ready` deltaP `1.2857` edge `-0.0023` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
