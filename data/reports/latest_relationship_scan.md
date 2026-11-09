# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T01:22:24.801951+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6539`

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

- `market_context_high->equity_24h` score `8.4567` n `34` status `ready` deltaP `15.7782` edge `0.9136` maxDD `-22.7914`
- `market_context_high->index_24h` score `1.243` n `34` status `ready` deltaP `15.4003` edge `0.1148` maxDD `-2.6491`
- `market_context_high->commodity_24h` score `1.2004` n `34` status `ready` deltaP `6.5768` edge `0.1776` maxDD `-2.4036`
- `market_context_high->fx_24h` score `0.6784` n `34` status `ready` deltaP `10.3146` edge `-0.0034` maxDD `-0.0397`
- `market_context_high->metal_1h` score `0.6506` n `63` status `ready` deltaP `8.7302` edge `0.0288` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `0.5254` n `51` status `ready` deltaP `4.1188` edge `0.0552` maxDD `-1.1102`
- `market_context_high->equity_1h` score `-0.0493` n `63` status `ready` deltaP `1.1524` edge `0.1057` maxDD `-5.5762`
- `market_context_high->metal_4h` score `-0.2231` n `51` status `ready` deltaP `3.7243` edge `-0.0009` maxDD `-1.2025`
- `market_context_high->commodity_1h` score `-0.2834` n `63` status `ready` deltaP `4.1489` edge `0.0075` maxDD `-1.7019`
- `market_context_high->fx_4h` score `-0.3228` n `51` status `ready` deltaP `4.5134` edge `0.0085` maxDD `-0.7317`
- `market_context_high->index_4h` score `-0.4201` n `51` status `ready` deltaP `6.2529` edge `-0.0027` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.5241` n `63` status `ready` deltaP `-3.6095` edge `0.0152` maxDD `-0.6664`
- `market_context_high->fx_1h` score `-0.7303` n `63` status `ready` deltaP `-8.3096` edge `-0.0003` maxDD `-0.3682`
- `market_context_high->crypto_alt_1h` score `-0.8765` n `63` status `ready` deltaP `7.7702` edge `0.0251` maxDD `-10.1421`
- `market_context_high->metal_24h` score `-1.9287` n `34` status `ready` deltaP `4.1667` edge `-0.1332` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.958` n `63` status `ready` deltaP `2.4997` edge `-0.0578` maxDD `-11.7911`
- `market_context_high->crypto_major_24h` score `-6.2913` n `34` status `ready` deltaP `-6.6993` edge `-0.0682` maxDD `-26.9129`
- `market_context_high->equity_4h` score `-6.4945` n `51` status `ready` deltaP `2.2208` edge `-0.1822` maxDD `-24.9053`
- `market_context_high->unknown_4h` score `-8.5005` n `51` status `ready` deltaP `-0.1375` edge `-0.6627` maxDD `-0.9139`
- `market_context_high->crypto_alt_4h` score `-10.4072` n `51` status `ready` deltaP `-1.1597` edge `-0.3986` maxDD `-30.5415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
