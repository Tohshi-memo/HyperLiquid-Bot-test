# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T14:37:24.339971+00:00`
- Price records: `672`
- Market context records: `6400`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11091`

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

- `news_risk_high->crypto_alt_24h` score `13.64` n `32` status `ready` deltaP `35.4167` edge `0.9153` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6406` n `32` status `ready` deltaP `55.9028` edge `0.1807` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3562` n `32` status `ready` deltaP `37.6736` edge `0.1324` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.1626` n `32` status `ready` deltaP `17.0139` edge `0.4982` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.062` n `32` status `ready` deltaP `42.1494` edge `0.0621` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4338` n `32` status `ready` deltaP `29.3413` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4359` n `32` status `ready` deltaP `13.6789` edge `0.1396` maxDD `-2.0691`
- `market_context_high->unknown_24h` score `1.0071` n `146` status `ready` deltaP `7.5248` edge `0.4136` maxDD `-19.0537`
- `news_risk_high->crypto_alt_1h` score `0.8349` n `32` status `ready` deltaP `10.2732` edge `0.0847` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4637` n `216` status `ready` deltaP `11.6248` edge `0.0408` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.4314` n `217` status `ready` deltaP `-5.5403` edge `0.1737` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.044` n `216` status `ready` deltaP `7.5147` edge `0.0212` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2141` n `32` status `ready` deltaP `6.8301` edge `-0.0289` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3269` n `146` status `ready` deltaP `19.6205` edge `0.0988` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4688` n `217` status `ready` deltaP `2.2586` edge `0.0026` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.4949` n `216` status `ready` deltaP `8.3898` edge `0.0505` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.6453` n `32` status `ready` deltaP `-1.1976` edge `-0.025` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.6947` n `217` status `ready` deltaP `-2.9719` edge `0.0027` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.7377` n `217` status `ready` deltaP `-0.9582` edge `-0.0017` maxDD `-0.9376`
- `market_context_high->commodity_1h` score `-0.7453` n `217` status `ready` deltaP `-3.6059` edge `-0.0032` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
