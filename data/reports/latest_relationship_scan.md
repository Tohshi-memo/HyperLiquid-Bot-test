# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T16:52:33.827872+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11696`

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

- `market_context_high->equity_24h` score `1.3646` n `136` status `ready` deltaP `4.636` edge `0.3962` maxDD `-21.0709`
- `market_context_high->commodity_4h` score `0.709` n `169` status `ready` deltaP `10.9269` edge `0.0577` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7071` n `136` status `ready` deltaP `18.7634` edge `0.0146` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7054` n `177` status `ready` deltaP `9.5826` edge `0.0292` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.1117` n `169` status `ready` deltaP `6.49` edge `0.0074` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1273` n `177` status `ready` deltaP `4.2517` edge `0.0005` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.2447` n `136` status `ready` deltaP `4.2524` edge `0.1044` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5514` n `177` status `ready` deltaP `-2.9965` edge `-0.003` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.7695` n `136` status `ready` deltaP `1.3852` edge `0.0548` maxDD `-2.9193`
- `market_context_high->metal_1h` score `-0.7805` n `177` status `ready` deltaP `-4.1941` edge `-0.0085` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.9` n `177` status `ready` deltaP `-2.2049` edge `-0.013` maxDD `-4.6817`
- `market_context_high->index_4h` score `-1.2289` n `169` status `ready` deltaP `-1.8843` edge `-0.0116` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.7722` n `177` status `ready` deltaP `-10.4765` edge `-0.047` maxDD `-6.1624`
- `market_context_high->metal_4h` score `-2.0752` n `169` status `ready` deltaP `-7.5246` edge `-0.0395` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.1726` n `169` status `ready` deltaP `-10.7961` edge `-0.1231` maxDD `-7.9331`
- `market_context_high->crypto_major_24h` score `-3.3597` n `136` status `ready` deltaP `0.9227` edge `-0.0367` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.81` n `169` status `ready` deltaP `-11.2354` edge `-0.1378` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-3.8838` n `136` status `ready` deltaP `-10.521` edge `-0.1092` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.9076` n `177` status `ready` deltaP `-11.0026` edge `-0.065` maxDD `-11.649`
- `market_context_high->commodity_24h` score `-8.7679` n `136` status `ready` deltaP `-5.3752` edge `-0.2167` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
