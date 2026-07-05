# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T17:07:27.249056+00:00`
- Price records: `672`
- Market context records: `5793`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8106`

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

- `market_context_high->equity_24h` score `0.6737` n `248` status `ready` deltaP `15.3954` edge `0.4614` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0469` n `305` status `ready` deltaP `6.4734` edge `0.1168` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.256` n `305` status `ready` deltaP `2.2239` edge `0.0009` maxDD `-0.5499`
- `market_context_high->metal_1h` score `-0.6215` n `305` status `ready` deltaP `2.5086` edge `-0.001` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6413` n `305` status `ready` deltaP `3.1423` edge `0.0263` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7617` n `305` status `ready` deltaP `-1.7959` edge `-0.0052` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9798` n `305` status `ready` deltaP `2.8723` edge `0.0313` maxDD `-6.2348`
- `market_context_high->index_1h` score `-1.0012` n `305` status `ready` deltaP `-0.0289` edge `0.0036` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-1.0719` n `248` status `ready` deltaP `13.8049` edge `0.0389` maxDD `-4.4684`
- `market_context_high->crypto_alt_1h` score `-1.1311` n `305` status `ready` deltaP `1.4681` edge `0.0294` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1768` n `305` status `ready` deltaP `1.058` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.5109` n `305` status `ready` deltaP `-0.2245` edge `0.0027` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.4693` n `305` status `ready` deltaP `-3.3932` edge `-0.0264` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.7948` n `248` status `ready` deltaP `3.7131` edge `0.0314` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.0347` n `305` status `ready` deltaP `7.4171` edge `0.1349` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8219` n `305` status `ready` deltaP `-5.3009` edge `-0.0472` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.6295` n `305` status `ready` deltaP `5.2284` edge `0.0802` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-7.138` n `248` status `ready` deltaP `-7.9805` edge `-0.255` maxDD `-27.5543`
- `market_context_high->crypto_major_24h` score `-7.9906` n `248` status `ready` deltaP `0.9913` edge `-0.1393` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-11.0508` n `248` status `ready` deltaP `-14.7569` edge `-0.0849` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
