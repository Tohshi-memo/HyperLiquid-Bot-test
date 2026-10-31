# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T01:52:29.148663+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1585.0623` n `134` status `ready` deltaP `-6.0894` edge `132.1721` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `141.4847` n `96` status `ready` deltaP `-2.9067` edge `11.8384` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.3378` n `134` status `ready` deltaP `0.4163` edge `3.372` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.8637` n `85` status `ready` deltaP `24.5983` edge `0.5574` maxDD `-3.6198`
- `market_context_high->equity_24h` score `7.0701` n `134` status `ready` deltaP `18.5687` edge `0.7411` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.8714` n `134` status `ready` deltaP `37.1735` edge `0.0931` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.4299` n `96` status `ready` deltaP `10.7348` edge `0.1305` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4402` n `134` status `ready` deltaP `15.3099` edge `0.0565` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3774` n `134` status `ready` deltaP `10.7539` edge `0.0146` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3256` n `134` status `ready` deltaP `14.9163` edge `0.0319` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1863` n `134` status `ready` deltaP `4.1827` edge `0.0752` maxDD `-2.3383`
- `market_context_high->equity_4h` score `-0.0166` n `134` status `ready` deltaP `2.0864` edge `0.1424` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `-0.0839` n `134` status `ready` deltaP `6.8661` edge `0.05` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.101` n `134` status `ready` deltaP `3.5794` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.1439` n `134` status `ready` deltaP `3.4409` edge `0.0165` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4634` n `134` status `ready` deltaP `0.4414` edge `-0.0025` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.6757` n `134` status `ready` deltaP `3.9257` edge `0.1519` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.8558` n `134` status `ready` deltaP `-2.3952` edge `0.0005` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8624` n `96` status `ready` deltaP `1.7715` edge `-0.0037` maxDD `-1.3981`
- `news_risk_high->commodity_1h` score `-0.9744` n `96` status `ready` deltaP `-8.7637` edge `-0.0001` maxDD `-1.9789`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
