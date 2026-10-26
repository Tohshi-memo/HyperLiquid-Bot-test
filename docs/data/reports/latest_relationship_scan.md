# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T03:22:28.283291+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5104`

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

- `market_context_high->unknown_4h` score `27.4073` n `113` status `ready` deltaP `-1.9682` edge `2.3306` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.1307` n `100` status `ready` deltaP `22.3472` edge `0.1348` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.0695` n `100` status `ready` deltaP `20.6319` edge `0.0286` maxDD `-1.2451`
- `market_context_high->fx_4h` score `-0.0645` n `113` status `ready` deltaP `7.0014` edge `0.0078` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.1535` n `118` status `ready` deltaP `2.1948` edge `0.0015` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.3642` n `118` status `ready` deltaP `5.3385` edge `-0.0031` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.5622` n `118` status `ready` deltaP `-1.0479` edge `0.0102` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5842` n `113` status `ready` deltaP `0.8107` edge `0.0426` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.7851` n `100` status `ready` deltaP `10.2708` edge `-0.0409` maxDD `-4.925`
- `market_context_high->index_1h` score `-1.1421` n `118` status `ready` deltaP `-3.537` edge `-0.0064` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-2.0328` n `113` status `ready` deltaP `3.2417` edge `-0.02` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1498` n `113` status `ready` deltaP `-7.7676` edge `-0.0364` maxDD `-4.3282`
- `market_context_high->crypto_major_1h` score `-2.2253` n `118` status `ready` deltaP `1.8954` edge `-0.04` maxDD `-9.3126`
- `market_context_high->crypto_alt_1h` score `-3.6455` n `118` status `ready` deltaP `-2.0882` edge `-0.0692` maxDD `-12.3203`
- `market_context_high->crypto_major_24h` score `-3.8052` n `100` status `ready` deltaP `0.4375` edge `-0.0567` maxDD `-15.7321`
- `market_context_high->equity_1h` score `-3.9818` n `118` status `ready` deltaP `-1.7406` edge `-0.0916` maxDD `-12.2891`
- `market_context_high->commodity_24h` score `-4.7919` n `100` status `ready` deltaP `-14.7361` edge `-0.1096` maxDD `-16.1866`
- `market_context_high->equity_24h` score `-7.4088` n `100` status `ready` deltaP `-2.5625` edge `-0.4044` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.0856` n `113` status `ready` deltaP `-12.7428` edge `-0.2557` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-10.6566` n `100` status `ready` deltaP `-10.4375` edge `-0.4068` maxDD `-61.8548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
