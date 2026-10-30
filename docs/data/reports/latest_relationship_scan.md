# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T13:37:32.060943+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7038`

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

- `market_context_high->unknown_24h` score `1683.977` n `134` status `ready` deltaP `-2.7908` edge `140.393` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `223.3806` n `48` status `ready` deltaP `-1.709` edge `18.639` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.1488` n `134` status `ready` deltaP `2.0932` edge `2.6784` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `9.4796` n `36` status `ready` deltaP `30.8605` edge `0.6189` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.3608` n `134` status `ready` deltaP `34.9166` edge `0.0656` maxDD `-0.1315`
- `market_context_high->equity_24h` score `2.9159` n `134` status `ready` deltaP `16.4853` edge `0.4088` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `1.4919` n `48` status `ready` deltaP `8.6577` edge `0.1083` maxDD `-1.669`
- `market_context_high->metal_1h` score `0.3829` n `134` status `ready` deltaP `10.9036` edge `0.0143` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3309` n `134` status `ready` deltaP `15.6785` edge `0.0275` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1538` n `134` status `ready` deltaP `4.6318` edge `0.0695` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.1469` n `134` status `ready` deltaP `13.0233` edge `0.0473` maxDD `-1.0837`
- `news_risk_high->commodity_4h` score `0.1288` n `36` status `ready` deltaP `-0.9485` edge `0.0566` maxDD `-0.7008`
- `market_context_high->crypto_major_1h` score `0.0672` n `134` status `ready` deltaP `7.4649` edge `0.0586` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0777` n `134` status `ready` deltaP `4.0285` edge `-0.001` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.1706` n `134` status `ready` deltaP `2.5437` edge `0.1196` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.3104` n `134` status `ready` deltaP `1.7942` edge `0.0136` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.367` n `48` status `ready` deltaP `3.8548` edge `-0.0034` maxDD `-0.5475`
- `market_context_high->fx_4h` score `-0.5298` n `134` status `ready` deltaP `-0.6257` edge `-0.0039` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8508` n `134` status `ready` deltaP `2.9985` edge `0.0574` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.863` n `134` status `ready` deltaP `-2.3952` edge `-0.0001` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
