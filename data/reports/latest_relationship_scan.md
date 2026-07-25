# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T16:22:31.206850+00:00`
- Price records: `672`
- Market context records: `7896`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14713`

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

- `market_context_high->equity_24h` score `14.6887` n `103` status `ready` deltaP `29.8561` edge `1.1592` maxDD `-6.0681`
- `market_context_high->metal_24h` score `5.4363` n `103` status `ready` deltaP `26.7891` edge `0.3338` maxDD `-0.4159`
- `market_context_high->equity_4h` score `5.3875` n `105` status `ready` deltaP `17.8408` edge `0.4193` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `1.8442` n `103` status `ready` deltaP `21.6643` edge `0.1676` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.5845` n `105` status `ready` deltaP `13.1637` edge `0.156` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.4268` n `105` status `ready` deltaP `14.9554` edge `0.191` maxDD `-6.7444`
- `market_context_high->index_4h` score `1.3538` n `105` status `ready` deltaP `17.8408` edge `0.0632` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.3529` n `110` status `ready` deltaP `11.8346` edge `0.1156` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3152` n `103` status `ready` deltaP `34.3009` edge `0.0487` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.2146` n `110` status `ready` deltaP `13.797` edge `0.0501` maxDD `-1.6021`
- `market_context_high->metal_4h` score `1.1446` n `105` status `ready` deltaP `12.1331` edge `0.1059` maxDD `-0.979`
- `market_context_high->index_1h` score `0.5719` n `110` status `ready` deltaP `10.7508` edge `0.019` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.5588` n `105` status `ready` deltaP `9.6037` edge `0.0419` maxDD `-1.0817`
- `market_context_high->index_24h` score `0.4949` n `103` status `ready` deltaP `2.8199` edge `0.1272` maxDD `-1.3807`
- `market_context_high->crypto_alt_1h` score `0.4204` n `110` status `ready` deltaP `5.5934` edge `0.041` maxDD `-1.4603`
- `market_context_high->metal_1h` score `0.2306` n `110` status `ready` deltaP `4.8231` edge `0.0249` maxDD `-0.6936`
- `market_context_high->fx_1h` score `-0.277` n `110` status `ready` deltaP `0.4341` edge `-0.0002` maxDD `-0.3901`
- `market_context_high->fx_4h` score `-0.3974` n `105` status `ready` deltaP `3.2716` edge `0.0034` maxDD `-1.0924`
- `market_context_high->commodity_1h` score `-0.4291` n `110` status `ready` deltaP `2.76` edge `0.0027` maxDD `-1.5486`
- `market_context_high->crypto_alt_24h` score `-1.894` n `103` status `ready` deltaP `9.8266` edge `0.2212` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
