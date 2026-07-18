# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T10:02:53.625300+00:00`
- Price records: `672`
- Market context records: `7127`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11667`

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

- `market_context_high->fx_4h` score `0.4556` n `140` status `ready` deltaP `17.0122` edge `0.015` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0862` n `151` status `ready` deltaP `4.6903` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4134` n `151` status `ready` deltaP `-2.6986` edge `0.0394` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6698` n `151` status `ready` deltaP `-0.694` edge `0.0218` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.7039` n `151` status `ready` deltaP `2.6173` edge `0.034` maxDD `-7.6692`
- `market_context_high->commodity_1h` score `-0.7919` n `151` status `ready` deltaP `-3.112` edge `-0.0187` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7984` n `151` status `ready` deltaP `0.7852` edge `-0.0053` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.4254` n `151` status `ready` deltaP `-5.538` edge `-0.0053` maxDD `-2.1249`
- `market_context_high->unknown_4h` score `-2.1522` n `140` status `ready` deltaP `-5.453` edge `0.0172` maxDD `-4.4825`
- `market_context_high->commodity_4h` score `-2.3085` n `140` status `ready` deltaP `-6.5461` edge `-0.0452` maxDD `-2.9494`
- `market_context_high->crypto_major_4h` score `-3.1138` n `140` status `ready` deltaP `3.2012` edge `0.0079` maxDD `-24.6094`
- `market_context_high->equity_1h` score `-3.4212` n `151` status `ready` deltaP `0.9577` edge `-0.0457` maxDD `-14.9961`
- `market_context_high->commodity_24h` score `-4.0658` n `140` status `ready` deltaP `-11.2401` edge `-0.133` maxDD `-4.4704`
- `market_context_high->index_4h` score `-4.2478` n `140` status `ready` deltaP `-4.7213` edge `-0.0526` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-4.5119` n `140` status `ready` deltaP `-10.0131` edge `-0.0133` maxDD `-5.3419`
- `market_context_high->fx_24h` score `-4.8016` n `140` status `ready` deltaP `-14.0129` edge `-0.024` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-4.8341` n `140` status `ready` deltaP `-0.331` edge `-0.0221` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-9.7229` n `140` status `ready` deltaP `-29.4842` edge `-0.099` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.8567` n `140` status `ready` deltaP `-1.8728` edge `-0.2552` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.6511` n `140` status `ready` deltaP `-28.5814` edge `-0.1731` maxDD `-41.5829`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
