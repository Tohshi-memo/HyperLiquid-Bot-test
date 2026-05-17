# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T07:59:35.060154+00:00`
- Price records: `672`
- Market context records: `992`
- Flow alert records: `4764`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `12.8303` n `211` status `ready` deltaP `31.3866` edge `0.9188` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1301` n `211` status `ready` deltaP `10.7369` edge `0.396` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.3559` n `211` status `ready` deltaP `1.912` edge `-0.0003` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.4976` n `211` status `ready` deltaP `2.8528` edge `0.0203` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6616` n `211` status `ready` deltaP `0.9053` edge `0.0157` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.6954` n `211` status `ready` deltaP `2.9648` edge `0.1218` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.7392` n `211` status `ready` deltaP `0.6107` edge `0.0008` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7651` n `211` status `ready` deltaP `2.5496` edge `0.0046` maxDD `-2.8282`
- `market_context_high->equity_24h` score `-1.2047` n `211` status `ready` deltaP `4.4376` edge `0.1305` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.2313` n `211` status `ready` deltaP `4.5807` edge `-0.0161` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.527` n `211` status `ready` deltaP `1.6889` edge `0.0767` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.76` n `211` status `ready` deltaP `-1.8291` edge `0.0178` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.9032` n `211` status `ready` deltaP `-1.3765` edge `-0.0389` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.0665` n `211` status `ready` deltaP `-0.8005` edge `-0.0229` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9631` n `211` status `ready` deltaP `6.8518` edge `0.078` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.3099` n `211` status `ready` deltaP `-2.2145` edge `0.0557` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.3574` n `211` status `ready` deltaP `-2.1862` edge `0.0126` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5844` n `211` status `ready` deltaP `-1.4565` edge `-0.0219` maxDD `-20.2343`
- `market_context_high->metal_4h` score `-4.6178` n `211` status `ready` deltaP `-5.0149` edge `-0.1629` maxDD `-24.9891`
- `market_context_high->commodity_24h` score `-8.3013` n `211` status `ready` deltaP `2.4915` edge `0.3839` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
