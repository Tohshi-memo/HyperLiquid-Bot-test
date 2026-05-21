# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T21:37:20.396685+00:00`
- Price records: `672`
- Market context records: `1463`
- Flow alert records: `6121`
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

- `market_context_high->crypto_alt_24h` score `12.8893` n `165` status `ready` deltaP `28.911` edge `1.083` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.9892` n `165` status `ready` deltaP `27.6136` edge `0.9282` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.3751` n `165` status `ready` deltaP `15.0663` edge `1.0142` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.1834` n `165` status `ready` deltaP `19.9874` edge `0.324` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.065` n `165` status `ready` deltaP `13.2197` edge `0.4833` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5288` n `222` status `ready` deltaP `7.1687` edge `0.1626` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2727` n `165` status `ready` deltaP `11.9602` edge `0.0479` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0955` n `222` status `ready` deltaP `3.6374` edge `0.0143` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1263` n `222` status `ready` deltaP `1.9933` edge `0.0362` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.2152` n `222` status `ready` deltaP `11.4631` edge `0.2376` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4248` n `222` status `ready` deltaP `1.2292` edge `0.0653` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4734` n `222` status `ready` deltaP `0.7553` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5695` n `222` status `ready` deltaP `1.6656` edge `0.0438` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0312` n `222` status `ready` deltaP `-3.9222` edge `-0.009` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.1443` n `222` status `ready` deltaP `5.2679` edge `0.0031` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.1533` n `222` status `ready` deltaP `5.1568` edge `0.1404` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.2782` n `222` status `ready` deltaP `-1.7978` edge `-0.0024` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5938` n `222` status `ready` deltaP `-0.739` edge `0.0078` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.8043` n `222` status `ready` deltaP `7.7895` edge `0.0669` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.023` n `222` status `ready` deltaP `-11.4068` edge `-0.0681` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
