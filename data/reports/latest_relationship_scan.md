# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T01:07:29.309609+00:00`
- Price records: `672`
- Market context records: `7935`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `16.5666` n `82` status `ready` deltaP `25.7749` edge `1.3429` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.2913` n `82` status `ready` deltaP `38.3016` edge `0.4356` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7477` n `91` status `ready` deltaP `24.8681` edge `0.4858` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.5381` n `82` status `ready` deltaP `27.7058` edge `0.2634` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.8356` n `91` status `ready` deltaP `25.5511` edge `0.1282` maxDD `-0.979`
- `market_context_high->index_4h` score `2.7499` n `91` status `ready` deltaP `28.2219` edge `0.077` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7433` n `91` status `ready` deltaP `13.2792` edge `0.1385` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `1.4094` n `91` status `ready` deltaP `10.1347` edge `0.1616` maxDD `-3.9374`
- `market_context_high->fx_24h` score `1.3729` n `82` status `ready` deltaP `27.926` edge `0.037` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.2625` n `82` status `ready` deltaP `10.4379` edge `0.1593` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.2018` n `91` status `ready` deltaP `11.7228` edge `0.1938` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.0336` n `91` status `ready` deltaP `15.8318` edge `0.0236` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6528` n `91` status `ready` deltaP `9.14` edge `0.0313` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5767` n `91` status `ready` deltaP `10.739` edge `0.0432` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.2475` n `91` status `ready` deltaP `4.9928` edge `0.0417` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.4008` n `91` status `ready` deltaP `0.3036` edge `0.0013` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.4028` n `91` status `ready` deltaP `0.9933` edge `-0.0014` maxDD `-1.5486`
- `market_context_high->fx_4h` score `-0.5003` n `91` status `ready` deltaP `4.0763` edge `0.0059` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.5078` n `91` status `ready` deltaP `2.7372` edge `0.0159` maxDD `-2.4502`
- `market_context_high->unknown_1h` score `-1.7845` n `91` status `ready` deltaP `8.8406` edge `-0.1653` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
