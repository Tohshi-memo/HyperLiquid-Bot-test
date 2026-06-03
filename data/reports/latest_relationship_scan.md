# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T14:07:26.497389+00:00`
- Price records: `672`
- Market context records: `2770`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `4.3512` n `135` status `ready` deltaP `9.155` edge `0.3436` maxDD `-1.6961`
- `market_context_high->crypto_alt_24h` score `2.6189` n `135` status `ready` deltaP `4.3403` edge `0.6985` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `1.0956` n `142` status `ready` deltaP `7.1002` edge `0.1493` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.1922` n `135` status `ready` deltaP `9.4675` edge `0.2709` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.044` n `142` status `ready` deltaP `10.7094` edge `0.0184` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0157` n `142` status `ready` deltaP `4.1811` edge `0.0439` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1498` n `142` status `ready` deltaP `3.4495` edge `0.0072` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.573` n `142` status `ready` deltaP `-0.9867` edge `0.0032` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5805` n `142` status `ready` deltaP `0.466` edge `-0.0022` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7027` n `142` status `ready` deltaP `-0.1666` edge `-0.0044` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7537` n `142` status `ready` deltaP `5.0962` edge `0.0454` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-1.0028` n `142` status `ready` deltaP `3.3272` edge `0.0362` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1617` n `142` status `ready` deltaP `-3.7973` edge `0.0118` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.2007` n `142` status `ready` deltaP `-4.3627` edge `0.0069` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.3439` n `142` status `ready` deltaP `14.3378` edge `0.2265` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.348` n `135` status `ready` deltaP `-0.787` edge `-0.0199` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.5611` n `142` status `ready` deltaP `0.161` edge `-0.0092` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.0623` n `142` status `ready` deltaP `-0.6291` edge `-0.0297` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.4264` n `142` status `ready` deltaP `-2.6` edge `-0.0387` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.6412` n `142` status `ready` deltaP `5.1249` edge `0.1178` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
