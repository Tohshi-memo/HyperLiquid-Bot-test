# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T00:07:26.206363+00:00`
- Price records: `672`
- Market context records: `5092`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `19.8526` n `78` status `ready` deltaP `27.5908` edge `1.5047` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `9.1247` n `111` status `ready` deltaP `3.3056` edge `0.8025` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `8.6479` n `99` status `ready` deltaP `21.8512` edge `0.6772` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.2302` n `99` status `ready` deltaP `14.9314` edge `0.4723` maxDD `-7.5459`
- `market_context_high->crypto_major_4h` score `2.8013` n `99` status `ready` deltaP `14.3786` edge `0.4725` maxDD `-12.4039`
- `market_context_high->equity_4h` score `2.5147` n `99` status `ready` deltaP `14.3416` edge `0.2271` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.1868` n `111` status `ready` deltaP `11.1116` edge `0.078` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.6917` n `111` status `ready` deltaP `6.1499` edge `0.1128` maxDD `-5.0257`
- `market_context_high->index_4h` score `0.5447` n `99` status `ready` deltaP `10.6816` edge `0.0503` maxDD `-1.0893`
- `market_context_high->crypto_major_1h` score `0.4157` n `111` status `ready` deltaP `7.4918` edge `0.1279` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.3762` n `111` status `ready` deltaP `9.8978` edge `0.0319` maxDD `-1.3057`
- `market_context_high->index_1h` score `0.3581` n `111` status `ready` deltaP `6.4574` edge `0.0166` maxDD `-0.3843`
- `market_context_high->metal_4h` score `0.0559` n `99` status `ready` deltaP `6.0498` edge `0.0821` maxDD `-2.5549`
- `market_context_high->commodity_1h` score `-1.0354` n `111` status `ready` deltaP `-1.5092` edge `-0.0014` maxDD `-1.986`
- `market_context_high->commodity_4h` score `-1.3386` n `99` status `ready` deltaP `5.8588` edge `-0.014` maxDD `-5.9285`
- `market_context_high->fx_24h` score `-1.5141` n `78` status `ready` deltaP `-3.1117` edge `-0.0084` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.5846` n `78` status `ready` deltaP `8.3333` edge `0.0375` maxDD `-15.0303`
- `market_context_high->fx_1h` score `-1.7032` n `111` status `ready` deltaP `-10.97` edge `-0.0047` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-2.274` n `99` status `ready` deltaP `-10.7016` edge `-0.0109` maxDD `-1.9141`
- `market_context_high->metal_24h` score `-4.4981` n `78` status `ready` deltaP `-6.21` edge `0.0102` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
