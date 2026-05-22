# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T01:22:15.136263+00:00`
- Price records: `672`
- Market context records: `1480`
- Flow alert records: `6169`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `12.6768` n `172` status `ready` deltaP `28.985` edge `1.0648` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.5712` n `172` status `ready` deltaP `27.3538` edge `0.8951` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.0754` n `172` status `ready` deltaP `16.4204` edge `0.9802` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.3185` n `172` status `ready` deltaP `13.6144` edge `0.5018` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2398` n `172` status `ready` deltaP `20.3327` edge `0.3264` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.6043` n `214` status `ready` deltaP `7.1832` edge `0.1688` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.4464` n `172` status `ready` deltaP `14.1312` edge `0.0479` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `0.0123` n `214` status `ready` deltaP `11.8019` edge `0.2543` maxDD `-19.5565`
- `market_context_high->equity_1h` score `-0.0722` n `214` status `ready` deltaP `2.4148` edge `0.0379` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1941` n `214` status `ready` deltaP `2.6597` edge `0.0126` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.4313` n `214` status `ready` deltaP `2.3141` edge `0.051` maxDD `-4.1892`
- `market_context_high->index_4h` score `-0.5123` n `214` status `ready` deltaP `0.5414` edge `0.0626` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-0.8361` n `214` status `ready` deltaP `6.3468` edge `0.1589` maxDD `-13.3376`
- `market_context_high->fx_1h` score `-0.8687` n `214` status `ready` deltaP `-0.88` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0329` n `214` status `ready` deltaP `-4.4905` edge `-0.0096` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.1425` n `214` status `ready` deltaP `5.6215` edge `0.0009` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.2305` n `214` status `ready` deltaP `-1.3655` edge `-0.0013` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.503` n `214` status `ready` deltaP `-0.34` edge `0.0127` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7383` n `214` status `ready` deltaP `8.2687` edge `0.0692` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0774` n `214` status `ready` deltaP `-12.017` edge `-0.071` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
