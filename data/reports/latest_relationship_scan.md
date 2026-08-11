# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T04:22:25.018812+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `27.2257` n `138` status `ready` deltaP `-16.1075` edge `2.6216` maxDD `-9.6329`
- `market_context_high->commodity_4h` score `0.8217` n `169` status `ready` deltaP `11.6452` edge `0.0623` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.6229` n `138` status `ready` deltaP `19.0687` edge `0.0335` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.6174` n `181` status `ready` deltaP `8.6325` edge `0.0282` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.219` n `169` status `ready` deltaP `4.2077` edge `0.0041` maxDD `-0.4854`
- `market_context_high->fx_1h` score `-0.2418` n `181` status `ready` deltaP `2.2751` edge `-0.001` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.8273` n `181` status `ready` deltaP `-6.4473` edge `-0.0043` maxDD `-1.0359`
- `market_context_high->commodity_24h` score `-0.8506` n `138` status `ready` deltaP `10.1048` edge `0.125` maxDD `-17.1133`
- `market_context_high->index_4h` score `-1.0654` n `169` status `ready` deltaP `-5.2597` edge `-0.0121` maxDD `-1.4875`
- `market_context_high->metal_1h` score `-1.2822` n `181` status `ready` deltaP `-5.017` edge `-0.0098` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.4641` n `181` status `ready` deltaP `-6.2582` edge `-0.0183` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-2.0805` n `138` status `ready` deltaP `1.3139` edge `-0.0497` maxDD `-2.9283`
- `market_context_high->index_24h` score `-2.4642` n `138` status `ready` deltaP `-11.6243` edge `-0.0289` maxDD `-6.7627`
- `market_context_high->crypto_alt_1h` score `-2.5985` n `181` status `ready` deltaP `-8.8844` edge `-0.0388` maxDD `-6.4812`
- `market_context_high->metal_4h` score `-3.1539` n `169` status `ready` deltaP `-7.4608` edge `-0.0367` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.355` n `181` status `ready` deltaP `-6.7594` edge `-0.0441` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.2206` n `169` status `ready` deltaP `-14.7443` edge `-0.1319` maxDD `-15.8728`
- `market_context_high->crypto_alt_4h` score `-6.3684` n `169` status `ready` deltaP `-10.2141` edge `-0.1278` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-6.8416` n `138` status `ready` deltaP `-14.069` edge `-0.2062` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.1684` n `138` status `ready` deltaP `-10.9824` edge `-0.211` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
