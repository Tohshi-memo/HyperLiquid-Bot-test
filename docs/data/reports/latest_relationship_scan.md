# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T07:52:27.260406+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9414`

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

- `market_context_high->crypto_alt_4h` score `7.7` n `131` status `ready` deltaP `18.857` edge `0.6074` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0581` n `54` status `ready` deltaP `38.5017` edge `0.3315` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0581` n `54` status `ready` deltaP `38.5017` edge `0.3315` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.2279` n `131` status `ready` deltaP `23.8875` edge `0.4919` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.3986` n `57` status `ready` deltaP `18.8034` edge `0.3692` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.3986` n `57` status `ready` deltaP `18.8034` edge `0.3692` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.2892` n `57` status `ready` deltaP `36.1146` edge `0.3944` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2892` n `57` status `ready` deltaP `36.1146` edge `0.3944` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3198` n `143` status `ready` deltaP `11.5385` edge `0.1395` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1358` n `143` status `ready` deltaP `8.4911` edge `0.1186` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.4614` n `131` status `ready` deltaP `13.6625` edge `0.0519` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.0355` n `69` status `ready` deltaP `6.9708` edge `0.0212` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.0355` n `69` status `ready` deltaP `6.9708` edge `0.0212` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.116` n `69` status `ready` deltaP `3.682` edge `0.0042` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.116` n `69` status `ready` deltaP `3.682` edge `0.0042` maxDD `-0.7394`
- `market_context_high->metal_1h` score `-0.2179` n `143` status `ready` deltaP `8.9381` edge `0.0092` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.2305` n `143` status `ready` deltaP `6.2056` edge `0.0039` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.4213` n `69` status `ready` deltaP `2.2694` edge `0.004` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4213` n `69` status `ready` deltaP `2.2694` edge `0.004` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.5015` n `143` status `ready` deltaP `7.8572` edge `0.0343` maxDD `-7.0778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
