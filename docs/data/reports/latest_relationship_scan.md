# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T02:37:22.939403+00:00`
- Price records: `672`
- Market context records: `7094`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.4455` n `161` status `ready` deltaP `16.9672` edge `0.014` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1483` n `161` status `ready` deltaP `4.464` edge `0.003` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.3033` n `161` status `ready` deltaP `-0.5718` edge `0.0344` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.3805` n `161` status `ready` deltaP `1.298` edge `0.029` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4107` n `161` status `ready` deltaP `2.1451` edge `-0.005` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.5501` n `161` status `ready` deltaP `4.0819` edge `0.0375` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8494` n `161` status `ready` deltaP `-4.2251` edge `-0.0191` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.3941` n `161` status `ready` deltaP `-5.2033` edge `-0.0047` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.4216` n `161` status `ready` deltaP `-5.2388` edge `-0.0438` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.714` n `161` status `ready` deltaP `-8.1209` edge `-0.0054` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0132` n `161` status `ready` deltaP `3.3873` edge `-0.0384` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.3173` n `161` status `ready` deltaP `1.9078` edge `-0.0399` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-2.9403` n `161` status `ready` deltaP `4.9633` edge `0.0184` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-2.9552` n `161` status `ready` deltaP `-5.7432` edge `-0.0771` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.1725` n `161` status `ready` deltaP `-1.3047` edge `-0.0195` maxDD `-22.2831`
- `market_context_high->fx_24h` score `-4.1491` n `161` status `ready` deltaP `-6.7417` edge `-0.0181` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.1887` n `161` status `ready` deltaP `-6.2301` edge `-0.0092` maxDD `-5.5324`
- `market_context_high->equity_4h` score `-8.3359` n `161` status `ready` deltaP `1.744` edge `-0.1933` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.8007` n `161` status `ready` deltaP `-23.087` edge `-0.0648` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.1498` n `161` status `ready` deltaP `-24.491` edge `-0.1303` maxDD `-43.5125`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
