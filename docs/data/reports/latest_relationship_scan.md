# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T17:07:32.078243+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2588.4936` n `139` status `ready` deltaP `1.2153` edge `215.6997` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.1089` n `139` status `ready` deltaP `31.1988` edge `1.5296` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.8721` n `139` status `ready` deltaP `33.5743` edge `0.8535` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.9117` n `139` status `ready` deltaP `24.8938` edge `0.9368` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1582` n `139` status `ready` deltaP `38.5117` edge `0.1593` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7402` n `139` status `ready` deltaP `31.586` edge `0.2866` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.8573` n `142` status `ready` deltaP `28.8947` edge `0.2056` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.4823` n `142` status `ready` deltaP `9.8528` edge `0.3238` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.002` n `142` status `ready` deltaP `7.8688` edge `0.1221` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7078` n `142` status `ready` deltaP `8.301` edge `0.0696` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.5353` n `142` status `ready` deltaP `9.3489` edge `0.0113` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1596` n `142` status `ready` deltaP `10.0545` edge `0.0316` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2613` n `142` status `ready` deltaP `3.0383` edge `0.0745` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.487` n `142` status `ready` deltaP `1.3135` edge `0.0136` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2367` n `142` status `ready` deltaP `-6.7824` edge `0.0361` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.285` n `142` status `ready` deltaP `9.4362` edge `-0.0063` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.5186` n `142` status `ready` deltaP `-3.6156` edge `0.1009` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.7942` n `142` status `ready` deltaP `-8.6953` edge `-0.0035` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8986` n `142` status `ready` deltaP `-9.7537` edge `-0.0109` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3615` n `142` status `ready` deltaP `-9.7647` edge `0.0042` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
