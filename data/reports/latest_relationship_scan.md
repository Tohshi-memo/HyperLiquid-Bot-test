# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T14:22:30.985487+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->equity_24h` score `7.0397` n `34` status `ready` deltaP `11.9588` edge `0.7442` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `1.974` n `34` status `ready` deltaP `4.1463` edge `0.1956` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.972` n `34` status `ready` deltaP `10.8865` edge `0.0983` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.6186` n `34` status `ready` deltaP `9.9877` edge `-0.0044` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3497` n `88` status `ready` deltaP `3.797` edge `0.0132` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4829` n `88` status `ready` deltaP `0.592` edge `0.0024` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5012` n `88` status `ready` deltaP `4.005` edge `0.0068` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.7706` n `88` status `ready` deltaP `-1.4689` edge `0.0216` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9208` n `88` status `ready` deltaP `-6.4575` edge `0.0081` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.9229` n `88` status `ready` deltaP `0.4712` edge `0.0169` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2876` n `88` status `ready` deltaP `-13.6091` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.3483` n `88` status `ready` deltaP `-6.7569` edge `0.0558` maxDD `-8.0225`
- `market_context_high->crypto_alt_1h` score `-1.8415` n `88` status `ready` deltaP `1.3813` edge `-0.0474` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.9951` n `34` status `ready` deltaP `-2.9514` edge `-0.1808` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.1258` n `88` status `ready` deltaP `-6.9152` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0754` n `88` status `ready` deltaP `-4.3617` edge `-0.1029` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.1806` n `88` status `ready` deltaP `0.6098` edge `-0.0578` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-6.5049` n `34` status `ready` deltaP `-6.5257` edge `-0.0355` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.4922` n `88` status `ready` deltaP `2.8548` edge `-0.2149` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.7146` n `34` status `ready` deltaP `-20.5576` edge `-0.2464` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
