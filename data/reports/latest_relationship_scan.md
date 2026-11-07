# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T06:34:33.704417+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4144`

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

- `news_risk_high->equity_4h` score `1.3237` n `62` status `ready` deltaP `12.7508` edge `0.1586` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.8421` n `62` status `ready` deltaP `14.4522` edge `0.0216` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3465` n `62` status `ready` deltaP `9.7558` edge `0.1462` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.2142` n `62` status `ready` deltaP `-0.8345` edge `0.0676` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.1104` n `62` status `ready` deltaP `8.3977` edge `0.0035` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0892` n `62` status `ready` deltaP `-0.5988` edge `0.0475` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1565` n `62` status `ready` deltaP `2.4097` edge `0.0024` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2785` n `62` status `ready` deltaP `0.7474` edge `0.0039` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5556` n `62` status `ready` deltaP `-4.2737` edge `-0.007` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.0552` n `62` status `ready` deltaP `-0.5606` edge `-0.041` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.2156` n `62` status `ready` deltaP `-2.4435` edge `-0.024` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2776` n `62` status `ready` deltaP `-3.1619` edge `0.0177` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.544` n `62` status `ready` deltaP `-10.5756` edge `-0.0022` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-1.9583` n `62` status `ready` deltaP `-7.881` edge `-0.0289` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.2371` n `62` status `ready` deltaP `-3.1619` edge `-0.0037` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.8225` n `62` status `ready` deltaP `-5.9476` edge `-0.2608` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5153` n `62` status `ready` deltaP `-31.1271` edge `-0.0116` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.8301` n `62` status `ready` deltaP `20.5197` edge `0.4026` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.6328` n `62` status `ready` deltaP `-28.7915` edge `-0.1281` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.5255` n `62` status `ready` deltaP `-31.4908` edge `-0.1502` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
