# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T15:37:16.165132+00:00`
- Price records: `672`
- Market context records: `1539`
- Flow alert records: `6344`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8803`

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

- `market_context_high->metal_24h` score `12.5427` n `179` status `ready` deltaP `22.9613` edge `0.9922` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.5143` n `179` status `ready` deltaP `28.3587` edge `0.9721` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.6477` n `179` status `ready` deltaP `27.3995` edge `0.7345` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.1321` n `179` status `ready` deltaP `20.651` edge `0.3153` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.668` n `179` status `ready` deltaP `13.5931` edge `0.3644` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.7731` n `179` status `ready` deltaP `17.3591` edge `0.0536` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1677` n `199` status `ready` deltaP `4.0239` edge `0.0966` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.4357` n `199` status `ready` deltaP `11.7301` edge `0.1979` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.5139` n `199` status `ready` deltaP `7.7552` edge `0.1533` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.5218` n `199` status `ready` deltaP `0.0692` edge `0.035` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5992` n `199` status `ready` deltaP `-1.5451` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7536` n `199` status `ready` deltaP `0.0256` edge `0.0002` maxDD `-1.7205`
- `market_context_high->commodity_1h` score `-0.7546` n `199` status `ready` deltaP `-0.6469` edge `-0.0003` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7695` n `199` status `ready` deltaP `4.6987` edge `0.0036` maxDD `-6.3532`
- `market_context_high->equity_1h` score `-0.8739` n `199` status `ready` deltaP `-1.6316` edge `0.0189` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.0517` n `199` status `ready` deltaP `-1.4917` edge `0.0108` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.2937` n `199` status `ready` deltaP `-9.0253` edge `-0.0128` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.4066` n `199` status `ready` deltaP `-4.5923` edge `0.0223` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.4699` n `199` status `ready` deltaP `9.4489` edge `0.0837` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.3019` n `199` status `ready` deltaP `-15.9196` edge `-0.1109` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
