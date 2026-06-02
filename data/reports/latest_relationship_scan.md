# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T05:07:19.644330+00:00`
- Price records: `672`
- Market context records: `2631`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.5267` n `145` status `ready` deltaP `18.2627` edge `0.5383` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.1648` n `145` status `ready` deltaP `25.4552` edge `0.5286` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.369` n `145` status `ready` deltaP `14.8276` edge `0.3629` maxDD `-10.1468`
- `market_context_high->index_24h` score `1.4298` n `145` status `ready` deltaP `11.4332` edge `0.141` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.2005` n `145` status `ready` deltaP `10.572` edge `0.1483` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0564` n `145` status `ready` deltaP `7.7859` edge `0.1411` maxDD `-3.7312`
- `market_context_high->crypto_alt_24h` score `0.9175` n `145` status `ready` deltaP `3.113` edge `0.6829` maxDD `-38.5086`
- `market_context_high->crypto_major_1h` score `0.6526` n `145` status `ready` deltaP `8.4442` edge `0.1175` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.3774` n `145` status `ready` deltaP `9.63` edge `0.0514` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.085` n `145` status `ready` deltaP `4.4879` edge `0.0124` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.2466` n `145` status `ready` deltaP `6.7923` edge `0.022` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4288` n `145` status `ready` deltaP `2.1784` edge `0.0119` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.725` n `145` status `ready` deltaP `-1.5424` edge `0.0031` maxDD `-0.2588`
- `market_context_high->metal_1h` score `-0.7967` n `145` status `ready` deltaP `0.3128` edge `0.0063` maxDD `-2.9823`
- `market_context_high->commodity_4h` score `-0.8289` n `145` status `ready` deltaP `5.8042` edge `0.0493` maxDD `-10.2078`
- `market_context_high->equity_1h` score `-0.9534` n `145` status `ready` deltaP `-1.4092` edge `0.0138` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-1.0509` n `145` status `ready` deltaP `2.3844` edge `0.0293` maxDD `-4.6217`
- `market_context_high->fx_24h` score `-1.0678` n `145` status `ready` deltaP `2.0282` edge `-0.0042` maxDD `-1.5312`
- `market_context_high->fx_4h` score `-1.1009` n `145` status `ready` deltaP `-2.3339` edge `0.0089` maxDD `-0.8066`
- `market_context_high->equity_4h` score `-1.3875` n `145` status `ready` deltaP `1.4277` edge `0.0153` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
