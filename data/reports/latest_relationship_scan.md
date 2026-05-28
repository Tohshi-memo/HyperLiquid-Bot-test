# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T14:22:22.980857+00:00`
- Price records: `672`
- Market context records: `2149`
- Flow alert records: `8083`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.628` n `152` status `ready` deltaP `38.0696` edge `0.9755` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `12.0055` n `152` status `ready` deltaP `42.1133` edge `0.7727` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.5222` n `152` status `ready` deltaP `25.1604` edge `0.4507` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `6.2116` n `33` status `ready` deltaP `28.0442` edge `0.3978` maxDD `-3.0367`
- `market_context_high->equity_4h` score `4.8458` n `152` status `ready` deltaP `26.2757` edge `0.3381` maxDD `-5.0894`
- `market_context_high->index_24h` score `3.7558` n `152` status `ready` deltaP `14.7935` edge `0.3372` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.5795` n `152` status `ready` deltaP `19.2602` edge `0.2176` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.3415` n `152` status `ready` deltaP `17.255` edge `0.2498` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.2483` n `152` status `ready` deltaP `23.5879` edge `0.1818` maxDD `-1.8022`
- `market_context_high->metal_4h` score `3.2275` n `152` status `ready` deltaP `21.9752` edge `0.2612` maxDD `-4.7664`
- `market_context_high->equity_24h` score `3.1518` n `152` status `ready` deltaP `26.4894` edge `0.5759` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.8006` n `152` status `ready` deltaP `27.1382` edge `0.5845` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `2.3275` n `33` status `ready` deltaP `30.4278` edge `0.0095` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1767` n `152` status `ready` deltaP `21.2628` edge `0.9959` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.5586` n `33` status `ready` deltaP `18.8008` edge `0.1468` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0399` n `43` status `ready` deltaP `18.8692` edge `0.0078` maxDD `-1.7548`
- `market_context_high->equity_1h` score `0.8902` n `152` status `ready` deltaP `10.7273` edge `0.0815` maxDD `-2.6402`
- `news_risk_high->commodity_1h` score `0.7853` n `43` status `ready` deltaP `10.4651` edge `0.0989` maxDD `-2.1052`
- `market_context_high->metal_1h` score `0.6997` n `152` status `ready` deltaP `9.6005` edge `0.0613` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.4885` n `43` status `ready` deltaP `8.4389` edge `0.0101` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
