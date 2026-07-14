# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T14:52:26.675415+00:00`
- Price records: `672`
- Market context records: `6718`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `1.4266` n `176` status `ready` deltaP `2.7935` edge `0.5395` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0719` n `176` status `ready` deltaP `8.55` edge `0.0382` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0063` n `176` status `ready` deltaP `5.9472` edge `0.0373` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3555` n `176` status `ready` deltaP `0.3334` edge `0.0007` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.481` n `176` status `ready` deltaP `7.9704` edge `0.0936` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5477` n `176` status `ready` deltaP `-0.1191` edge `0.002` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6375` n `176` status `ready` deltaP `-0.3028` edge `-0.0114` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6716` n `176` status `ready` deltaP `-4.6918` edge `-0.0023` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-0.9025` n `176` status `ready` deltaP `4.1542` edge `-0.0002` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.0931` n `176` status `ready` deltaP `8.1208` edge `-0.0063` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2138` n `176` status `ready` deltaP `7.5388` edge `0.0005` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.6521` n `176` status `ready` deltaP `-3.6031` edge `-0.0388` maxDD `-5.5853`
- `market_context_high->crypto_major_4h` score `-2.0336` n `176` status `ready` deltaP `5.9451` edge `0.0311` maxDD `-16.8495`
- `market_context_high->unknown_1h` score `-2.0498` n `176` status `ready` deltaP `-8.6724` edge `-0.0229` maxDD `-3.2083`
- `market_context_high->crypto_alt_4h` score `-2.2028` n `176` status `ready` deltaP `4.0465` edge `0.0308` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.48` n `176` status `ready` deltaP `-5.0998` edge `0.0021` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.6862` n `176` status `ready` deltaP `6.5133` edge `-0.0891` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-4.0162` n `176` status `ready` deltaP `-18.1541` edge `0.0229` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2863` n `176` status `ready` deltaP `-8.0492` edge `0.0001` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.256` n `176` status `ready` deltaP `-7.3864` edge `-0.0325` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
