# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T20:22:33.088100+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7314`

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

- `news_risk_high->unknown_24h` score `2672.316` n `139` status `ready` deltaP `1.2153` edge `222.6849` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `9.8337` n `139` status `ready` deltaP `25.6433` edge `1.0437` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `6.2932` n `139` status `ready` deltaP `25.241` edge `0.6118` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.0975` n `139` status `ready` deltaP `21.5952` edge `0.8076` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.3095` n `139` status `ready` deltaP `30.8728` edge `0.1395` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.4099` n `139` status `ready` deltaP `23.2527` edge `0.2313` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.3939` n `139` status `ready` deltaP `25.9541` edge `0.1874` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.7489` n `139` status `ready` deltaP `7.736` edge `0.2768` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6471` n `139` status `ready` deltaP `6.8679` edge `0.0992` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5068` n `139` status `ready` deltaP `7.2546` edge `0.06` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4683` n `139` status `ready` deltaP `8.9013` edge `0.0087` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1733` n `139` status `ready` deltaP `6.658` edge `0.0265` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5256` n `139` status `ready` deltaP `1.3408` edge `0.0102` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5599` n `139` status `ready` deltaP `0.5966` edge `0.0525` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1967` n `139` status `ready` deltaP `-9.4172` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2579` n `139` status `ready` deltaP `9.3722` edge `-0.0024` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4596` n `139` status `ready` deltaP `-9.6135` edge `0.0264` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8483` n `139` status `ready` deltaP `-5.3957` edge `0.0705` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0381` n `139` status `ready` deltaP `-12.0159` edge `-0.0137` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7946` n `139` status `ready` deltaP `-11.0173` edge `-0.0009` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
