# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T21:22:27.792711+00:00`
- Price records: `672`
- Market context records: `2904`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `11.3615` n `142` status `ready` deltaP `11.0354` edge `1.2649` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.0897` n `142` status `ready` deltaP `12.7274` edge `0.623` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.3279` n `142` status `ready` deltaP `11.1086` edge `0.4164` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2066` n `142` status `ready` deltaP `10.2382` edge `0.2137` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7616` n `142` status `ready` deltaP `15.5516` edge `0.3525` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4673` n `142` status `ready` deltaP `13.1484` edge `0.0564` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.1279` n `142` status `ready` deltaP `4.8136` edge `0.0839` maxDD `-3.7602`
- `market_context_high->equity_4h` score `0.0879` n `142` status `ready` deltaP `5.7734` edge `0.1068` maxDD `-5.7037`
- `market_context_high->index_1h` score `-0.05` n `142` status `ready` deltaP `4.0483` edge `0.016` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2666` n `142` status `ready` deltaP `4.4805` edge `0.021` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.5418` n `142` status `ready` deltaP `-0.5039` edge `0.0415` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-0.5429` n `142` status `ready` deltaP `14.7951` edge `0.2902` maxDD `-28.7261`
- `market_context_high->crypto_alt_1h` score `-0.5502` n `142` status `ready` deltaP `5.695` edge `0.0675` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.6029` n `142` status `ready` deltaP `-1.2861` edge `0.0027` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6147` n `142` status `ready` deltaP `-0.7316` edge `0.0014` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.663` n `142` status `ready` deltaP `5.8721` edge `0.0628` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6723` n `142` status `ready` deltaP `-0.3163` edge `0.0005` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-1.0847` n `142` status `ready` deltaP `-2.8383` edge `0.0064` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.1899` n `142` status `ready` deltaP `2.9049` edge `0.0201` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2972` n `142` status `ready` deltaP `-1.7116` edge `-0.0095` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
