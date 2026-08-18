# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T05:37:25.999930+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `2.8881` n `73` status `ready` deltaP `7.3147` edge `0.3127` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.698` n `73` status `ready` deltaP `12.6469` edge `0.1885` maxDD `-4.666`
- `market_context_high->metal_4h` score `0.6485` n `97` status `ready` deltaP `13.3077` edge `0.0229` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.3883` n `97` status `ready` deltaP `9.4167` edge `0.0891` maxDD `-3.1677`
- `market_context_high->equity_1h` score `0.2682` n `102` status `ready` deltaP `5.2895` edge `0.0371` maxDD `-1.0384`
- `market_context_high->unknown_1h` score `0.2387` n `102` status `ready` deltaP `9.0701` edge `-0.0179` maxDD `-0.4807`
- `market_context_high->index_1h` score `0.1761` n `102` status `ready` deltaP `8.7179` edge `0.0045` maxDD `-0.2038`
- `market_context_high->commodity_4h` score `-0.0477` n `97` status `ready` deltaP `7.9284` edge `0.0282` maxDD `-2.4692`
- `market_context_high->metal_24h` score `-0.0712` n `73` status `ready` deltaP `4.8384` edge `0.0655` maxDD `-2.9618`
- `market_context_high->metal_1h` score `-0.2142` n `102` status `ready` deltaP `1.1301` edge `0.0037` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2587` n `97` status `ready` deltaP `2.5411` edge `0.0006` maxDD `-0.3904`
- `market_context_high->crypto_alt_4h` score `-0.2826` n `97` status `ready` deltaP `7.3108` edge `0.0811` maxDD `-6.6186`
- `market_context_high->crypto_alt_1h` score `-0.4518` n `102` status `ready` deltaP `0.8307` edge `0.0167` maxDD `-2.413`
- `market_context_high->unknown_24h` score `-0.4839` n `73` status `ready` deltaP `9.798` edge `-0.0735` maxDD `-0.5713`
- `market_context_high->fx_1h` score `-0.4975` n `102` status `ready` deltaP `-1.0626` edge `0.0018` maxDD `-0.2273`
- `market_context_high->crypto_major_1h` score `-0.6413` n `102` status `ready` deltaP `-0.2172` edge `0.0076` maxDD `-3.07`
- `market_context_high->index_4h` score `-0.6731` n `97` status `ready` deltaP `-0.3756` edge `0.0076` maxDD `-0.2281`
- `market_context_high->commodity_1h` score `-0.7461` n `102` status `ready` deltaP `-5.2014` edge `0.0003` maxDD `-1.5684`
- `market_context_high->equity_4h` score `-0.8604` n `97` status `ready` deltaP `-2.8869` edge `0.038` maxDD `-2.5696`
- `market_context_high->index_24h` score `-1.7304` n `73` status `ready` deltaP `-1.4506` edge `-0.096` maxDD `-3.9612`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
