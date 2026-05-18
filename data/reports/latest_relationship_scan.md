# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T23:37:15.463658+00:00`
- Price records: `672`
- Market context records: `1166`
- Flow alert records: `5258`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8750`

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

- `market_context_high->crypto_major_24h` score `20.921` n `138` status `ready` deltaP `45.8861` edge `1.5507` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.1317` n `138` status `ready` deltaP `22.1317` edge `0.8984` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.6899` n `138` status `ready` deltaP `21.7844` edge `0.5886` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.7406` n `138` status `ready` deltaP `20.3955` edge `0.3982` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.4711` n `138` status `ready` deltaP `-3.744` edge `0.6476` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.4804` n `154` status `ready` deltaP `12.589` edge `0.1891` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1258` n `154` status `ready` deltaP `8.9583` edge `0.1024` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `1.05` n `138` status `ready` deltaP `2.6495` edge `0.3428` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.5127` n `154` status `ready` deltaP `7.9069` edge `0.0217` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2502` n `154` status `ready` deltaP `2.6129` edge `0.0412` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1755` n `154` status `ready` deltaP `8.8946` edge `0.0009` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.1229` n `154` status `ready` deltaP `8.4416` edge `0.1516` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.0025` n `154` status `ready` deltaP `7.0943` edge `0.0296` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.4003` n `154` status `ready` deltaP `2.403` edge `0.0349` maxDD `-3.4088`
- `market_context_high->unknown_4h` score `-0.4302` n `154` status `ready` deltaP `5.8501` edge `0.0468` maxDD `-6.7322`
- `market_context_high->metal_1h` score `-0.4898` n `154` status `ready` deltaP `5.4029` edge `-0.0158` maxDD `-2.2164`
- `market_context_high->commodity_1h` score `-0.818` n `154` status `ready` deltaP `-3.1476` edge `-0.0031` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.9977` n `154` status `ready` deltaP `-3.5793` edge `-0.0044` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.2871` n `154` status `ready` deltaP `4.0327` edge `0.1046` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.9102` n `154` status `ready` deltaP `4.8009` edge `-0.0815` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
