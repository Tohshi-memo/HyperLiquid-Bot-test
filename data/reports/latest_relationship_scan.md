# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T10:52:26.837335+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `11599.1106` n `111` status `ready` deltaP `1.0129` edge `966.6056` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7190.0692` n `111` status `ready` deltaP `0.2623` edge `599.1991` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.7565` n `97` status `ready` deltaP `40.3619` edge `1.6521` maxDD `-19.8583`
- `market_context_high->crypto_alt_24h` score `10.5765` n `97` status `ready` deltaP `21.7622` edge `1.4108` maxDD `-12.3265`
- `market_context_high->crypto_major_4h` score `-0.1295` n `111` status `ready` deltaP `1.42` edge `0.3135` maxDD `-20.8321`
- `market_context_high->metal_4h` score `-0.2128` n `111` status `ready` deltaP `14.0038` edge `0.0179` maxDD `-5.9858`
- `market_context_high->metal_24h` score `-0.2346` n `97` status `ready` deltaP `15.6608` edge `0.194` maxDD `-15.4361`
- `market_context_high->metal_1h` score `-0.2841` n `111` status `ready` deltaP `2.6932` edge `0.0121` maxDD `-2.6517`
- `market_context_high->crypto_alt_4h` score `-0.3791` n `111` status `ready` deltaP `1.8773` edge `0.2012` maxDD `-15.9855`
- `market_context_high->crypto_major_1h` score `-0.8397` n `111` status `ready` deltaP `2.5435` edge `0.0621` maxDD `-10.2705`
- `market_context_high->index_1h` score `-0.8422` n `111` status `ready` deltaP `-1.8113` edge `0.0028` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.087` n `111` status `ready` deltaP `-2.108` edge `0.025` maxDD `-7.6911`
- `market_context_high->index_4h` score `-1.2443` n `111` status `ready` deltaP `-3.583` edge `-0.0013` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.4284` n `111` status `ready` deltaP `-9.4703` edge `-0.001` maxDD `-0.392`
- `market_context_high->fx_4h` score `-2.4348` n `111` status `ready` deltaP `-15.601` edge `-0.0039` maxDD `-2.0063`
- `market_context_high->commodity_1h` score `-2.5589` n `111` status `ready` deltaP `-11.5688` edge `-0.0283` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.7925` n `111` status `ready` deltaP `0.8914` edge `-0.0209` maxDD `-11.0868`
- `market_context_high->fx_24h` score `-6.7823` n `97` status `ready` deltaP `-19.4766` edge `-0.0049` maxDD `-5.7694`
- `market_context_high->commodity_4h` score `-7.5128` n `111` status `ready` deltaP `-24.3875` edge `-0.1016` maxDD `-14.9509`
- `market_context_high->index_24h` score `-9.2247` n `97` status `ready` deltaP `-16.9798` edge `-0.1133` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
