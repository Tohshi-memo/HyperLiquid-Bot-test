# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T21:07:21.607632+00:00`
- Price records: `672`
- Market context records: `2903`
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

- `market_context_high->crypto_alt_24h` score `11.2264` n `142` status `ready` deltaP `10.8617` edge `1.2548` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.0423` n `142` status `ready` deltaP `12.5538` edge `0.6202` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.2984` n `142` status `ready` deltaP `10.935` edge `0.4151` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2066` n `142` status `ready` deltaP `10.2382` edge `0.2137` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.752` n `142` status `ready` deltaP `15.5516` edge `0.3517` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4665` n `142` status `ready` deltaP `13.1484` edge `0.0563` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.1279` n `142` status `ready` deltaP `4.8136` edge `0.0839` maxDD `-3.7602`
- `market_context_high->equity_4h` score `0.0589` n `142` status `ready` deltaP `5.6209` edge `0.1054` maxDD `-5.7037`
- `market_context_high->index_1h` score `-0.0594` n `142` status `ready` deltaP `3.8986` edge `0.0158` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2642` n `142` status `ready` deltaP `4.4805` edge `0.0212` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.5466` n `142` status `ready` deltaP `-0.5039` edge `0.0411` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.5494` n `142` status `ready` deltaP `5.695` edge `0.0676` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.5573` n `142` status `ready` deltaP `14.7951` edge `0.289` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.5898` n `142` status `ready` deltaP `-1.1364` edge `0.0028` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6155` n `142` status `ready` deltaP `-0.7316` edge `0.0013` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6614` n `142` status `ready` deltaP `5.8721` edge `0.063` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.673` n `142` status `ready` deltaP `-0.3163` edge `0.0004` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-1.0981` n `142` status `ready` deltaP `-2.9908` edge `0.0063` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.186` n `142` status `ready` deltaP `2.9049` edge `0.0206` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2996` n `142` status `ready` deltaP `-1.7116` edge `-0.0097` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
