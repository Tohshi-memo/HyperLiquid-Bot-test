# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T12:52:26.829652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7034`

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

- `market_context_high->unknown_24h` score `1815.8954` n `134` status `ready` deltaP `-2.7908` edge `151.3862` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `207.0752` n `45` status `ready` deltaP `-2.6813` edge `17.2867` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.2897` n `134` status `ready` deltaP `2.5505` edge `2.6871` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `9.4402` n `33` status `ready` deltaP `29.0928` edge `0.6274` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.2891` n `134` status `ready` deltaP `34.3957` edge `0.0631` maxDD `-0.1315`
- `market_context_high->equity_24h` score `2.6392` n `134` status `ready` deltaP `16.3117` edge `0.3869` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `1.98` n `45` status `ready` deltaP `11.9694` edge `0.1269` maxDD `-1.669`
- `news_risk_high->commodity_4h` score `0.4071` n `33` status `ready` deltaP `2.8872` edge `0.0667` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.3821` n `134` status `ready` deltaP `10.9036` edge `0.0142` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.32` n `134` status `ready` deltaP `15.6785` edge `0.0261` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1118` n `134` status `ready` deltaP `4.3324` edge `0.068` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.0959` n `134` status `ready` deltaP `12.566` edge `0.0461` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0216` n `134` status `ready` deltaP `7.1655` edge `0.0568` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1042` n `134` status `ready` deltaP `3.5794` edge `-0.0014` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.2513` n `134` status `ready` deltaP `2.0864` edge `0.1123` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.3619` n `134` status `ready` deltaP `1.3451` edge `0.0123` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.3854` n `45` status `ready` deltaP `3.0107` edge `-0.0045` maxDD `-0.5314`
- `news_risk_high->metal_4h` score `-0.5035` n `33` status `ready` deltaP `5.9543` edge `-0.0139` maxDD `-2.2282`
- `market_context_high->fx_4h` score `-0.5582` n `134` status `ready` deltaP `-1.083` edge `-0.0045` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.6298` n `45` status `ready` deltaP `-9.4012` edge `0.0163` maxDD `-0.4158`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
