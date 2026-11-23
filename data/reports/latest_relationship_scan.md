# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T03:22:28.087455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5282`

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

- `market_context_high->unknown_1h` score `15789.3574` n `85` status `ready` deltaP `2.2437` edge `1315.781` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10426.9519` n `84` status `ready` deltaP `3.2884` edge `868.9046` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1337.7994` n `31` status `ready` deltaP `4.0274` edge `111.474` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1184.1369` n `31` status `ready` deltaP `3.634` edge `98.6595` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.6237` n `31` status `ready` deltaP `38.1393` edge `0.7626` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0855` n `31` status `ready` deltaP `25.9982` edge `0.8375` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6572` n `31` status `ready` deltaP `14.4915` edge `0.8986` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0397` n `31` status `ready` deltaP `20.1371` edge `0.2211` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4382` n `31` status `ready` deltaP `36.0051` edge `0.0725` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7346` n `31` status `ready` deltaP `31.9925` edge `0.0231` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5156` n `31` status `ready` deltaP `10.1603` edge `0.3009` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.15` n `31` status `ready` deltaP `9.1124` edge `0.2506` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5586` n `31` status `ready` deltaP `29.433` edge `0.0315` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5215` n `31` status `ready` deltaP `20.894` edge `0.1115` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8383` n `31` status `ready` deltaP `18.2779` edge `0.0254` maxDD `-0.5151`
- `market_context_high->fx_4h` score `-0.0066` n `84` status `ready` deltaP `10.2787` edge `0.0133` maxDD `-0.6138`
- `news_risk_high->commodity_1h` score `-0.0933` n `31` status `ready` deltaP `1.0817` edge `0.0112` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1557` n `85` status `ready` deltaP `3.4748` edge `0.0087` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.3683` n `85` status `ready` deltaP `1.9355` edge `0.002` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.1174` n `85` status `ready` deltaP `-4.9525` edge `-0.0167` maxDD `-3.1494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
