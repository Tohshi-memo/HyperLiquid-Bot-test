# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T16:07:30.558109+00:00`
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

- `news_risk_high->unknown_24h` score `2584.2876` n `139` status `ready` deltaP `1.2153` edge `215.3492` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.3733` n `139` status `ready` deltaP `31.8933` edge `1.547` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.1054` n `139` status `ready` deltaP `34.2688` edge `0.8693` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.0965` n `139` status `ready` deltaP `24.8938` edge `0.9522` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1798` n `139` status `ready` deltaP `38.5117` edge `0.1611` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7738` n `139` status `ready` deltaP `31.586` edge `0.2894` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.776` n `142` status `ready` deltaP `28.285` edge `0.2037` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.2451` n `142` status `ready` deltaP `9.243` edge `0.3081` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8785` n `142` status `ready` deltaP `7.27` edge `0.1158` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6386` n `142` status `ready` deltaP `7.7022` edge `0.068` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4958` n `142` status `ready` deltaP `8.8998` edge `0.011` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1` n `142` status `ready` deltaP `9.4448` edge `0.0307` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.3151` n `142` status `ready` deltaP `2.5892` edge `0.0706` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5313` n `142` status `ready` deltaP `0.8644` edge `0.0129` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.2858` n `142` status `ready` deltaP `9.4362` edge `-0.0064` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.2879` n `142` status `ready` deltaP `-7.3922` edge `0.0336` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.6587` n `142` status `ready` deltaP `-4.2254` edge `0.087` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8205` n `142` status `ready` deltaP `-8.9947` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9134` n `142` status `ready` deltaP `-10.0531` edge `-0.0108` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3544` n `142` status `ready` deltaP `-9.6122` edge `0.0041` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
