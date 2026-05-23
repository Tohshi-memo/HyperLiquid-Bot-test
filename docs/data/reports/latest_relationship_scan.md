# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T08:22:16.174076+00:00`
- Price records: `672`
- Market context records: `1612`
- Flow alert records: `6550`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `12.5913` n `187` status `ready` deltaP `28.3673` edge `1.0021` maxDD `-7.355`
- `market_context_high->crypto_alt_24h` score `6.1044` n `187` status `ready` deltaP `24.6593` edge `0.9222` maxDD `-43.2315`
- `market_context_high->crypto_major_24h` score `5.4577` n `187` status `ready` deltaP `24.534` edge `0.718` maxDD `-30.4732`
- `market_context_high->index_24h` score `3.8306` n `187` status `ready` deltaP `20.513` edge `0.2911` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.5751` n `187` status `ready` deltaP `19.0684` edge `0.4593` maxDD `-18.7462`
- `market_context_high->equity_4h` score `1.3205` n `195` status `ready` deltaP `11.0687` edge `0.1457` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.2941` n `195` status `ready` deltaP `13.2848` edge `0.2811` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.1546` n `195` status `ready` deltaP `9.3902` edge `0.2281` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.193` n `187` status `ready` deltaP `8.013` edge `0.0354` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.2688` n `195` status `ready` deltaP `0.8107` edge `0.0625` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.485` n `195` status `ready` deltaP `1.3397` edge `0.0315` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.667` n `195` status `ready` deltaP `0.5689` edge `0.0038` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.8641` n `195` status `ready` deltaP `-0.8552` edge `0.0306` maxDD `-6.1883`
- `market_context_high->fx_1h` score `-0.8766` n `195` status `ready` deltaP `-0.9634` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.8889` n `195` status `ready` deltaP `0.2439` edge `0.0332` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-1.121` n `195` status `ready` deltaP `-0.3424` edge `0.001` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.143` n `195` status `ready` deltaP `4.9547` edge `0.0053` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.3933` n `195` status `ready` deltaP `9.0713` edge `0.0926` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.403` n `195` status `ready` deltaP `-10.8724` edge `-0.0145` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.1869` n `195` status `ready` deltaP `-13.9783` edge `-0.1091` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
