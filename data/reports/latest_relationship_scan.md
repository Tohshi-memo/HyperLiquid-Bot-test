# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T01:52:25.112759+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7535`

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

- `market_context_high->unknown_24h` score `7630.1455` n `53` status `ready` deltaP `1.3889` edge `635.8362` maxDD `0.0`
- `market_context_high->unknown_4h` score `359.0243` n `53` status `ready` deltaP `7.412` edge `29.8736` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `32.5597` n `56` status `ready` deltaP `4.7049` edge `2.693` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.1005` n `53` status `ready` deltaP `42.7313` edge `1.4971` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.58` n `94` status `ready` deltaP `32.698` edge `1.0493` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.1842` n `53` status `ready` deltaP `49.1319` edge `0.1878` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.124` n `53` status `ready` deltaP `24.7297` edge `0.3749` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `6.0927` n `53` status `ready` deltaP `42.1974` edge `0.2575` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.5139` n `53` status `ready` deltaP `31.2472` edge `0.2848` maxDD `-1.6901`
- `market_context_high->commodity_4h` score `3.3835` n `53` status `ready` deltaP `31.7994` edge `0.0867` maxDD `-0.3387`
- `market_context_high->equity_4h` score `2.9916` n `53` status `ready` deltaP `3.555` edge `0.2958` maxDD `-2.283`
- `news_risk_high->crypto_alt_4h` score `2.3016` n `126` status `ready` deltaP `9.4706` edge `0.2673` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.2673` n `53` status `ready` deltaP `9.4864` edge `0.2951` maxDD `-3.0799`
- `market_context_high->equity_1h` score `2.0127` n `56` status `ready` deltaP `6.6938` edge `0.1756` maxDD `-1.5336`
- `market_context_high->crypto_alt_24h` score `1.9506` n `53` status `ready` deltaP `-4.4156` edge `0.4313` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6153` n `53` status `ready` deltaP `19.3338` edge `0.0482` maxDD `-0.7323`
- `market_context_high->crypto_major_1h` score `1.4284` n `56` status `ready` deltaP `6.6938` edge `0.1253` maxDD `-1.4048`
- `market_context_high->crypto_alt_1h` score `1.2573` n `56` status `ready` deltaP `2.2348` edge `0.1511` maxDD `-2.2314`
- `market_context_high->fx_1h` score `1.2368` n `56` status `ready` deltaP `17.2583` edge `0.0056` maxDD `-0.0736`
- `market_context_high->metal_1h` score `1.0204` n `56` status `ready` deltaP `12.5214` edge `0.0264` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
