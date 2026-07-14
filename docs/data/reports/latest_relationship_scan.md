# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T11:37:27.343333+00:00`
- Price records: `672`
- Market context records: `6705`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_24h` score `1.1775` n `180` status `ready` deltaP `1.6319` edge `0.5153` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.3362` n `180` status `ready` deltaP `9.5709` edge `0.0502` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.1522` n `180` status `ready` deltaP `6.6001` edge `0.0451` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.1886` n `180` status `ready` deltaP `8.7153` edge `0.113` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3626` n `180` status `ready` deltaP `0.1963` edge `0.0007` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5643` n `180` status `ready` deltaP `-0.6188` edge `0.0032` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.6108` n `180` status `ready` deltaP `-3.9721` edge `0.0007` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6563` n `180` status `ready` deltaP `-0.5589` edge `-0.0121` maxDD `-2.1314`
- `market_context_high->unknown_1h` score `-0.741` n `180` status `ready` deltaP `-7.0725` edge `0.0755` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-0.934` n `180` status `ready` deltaP `3.6095` edge `0.0008` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.9558` n `180` status `ready` deltaP `9.9356` edge `-0.0008` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2524` n `180` status `ready` deltaP `7.3171` edge `-0.0001` maxDD `-2.4064`
- `market_context_high->crypto_major_4h` score `-1.636` n `180` status `ready` deltaP `7.2765` edge `0.0732` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.8119` n `180` status `ready` deltaP `-5.5522` edge `-0.0463` maxDD `-5.5853`
- `market_context_high->crypto_alt_4h` score `-1.856` n `180` status `ready` deltaP `5.5556` edge `0.0652` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.3381` n `180` status `ready` deltaP `-3.9905` edge `0.0129` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.8769` n `180` status `ready` deltaP `-16.8327` edge `0.0257` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4375` n `180` status `ready` deltaP `-8.6458` edge `-0.0001` maxDD `-6.2976`
- `market_context_high->equity_4h` score `-5.4023` n `180` status `ready` deltaP `6.8733` edge `-0.0691` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.0625` n `180` status `ready` deltaP `-6.3195` edge `-0.0148` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
