# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T12:07:52.143563+00:00`
- Price records: `672`
- Market context records: `6916`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->fx_1h` score `-0.1615` n `224` status `ready` deltaP `3.7345` edge `0.0029` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.1942` n `200` status `ready` deltaP `-5.3795` edge `0.4126` maxDD `-14.4643`
- `market_context_high->crypto_alt_1h` score `-0.3935` n `224` status `ready` deltaP `2.9593` edge `0.0239` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4711` n `224` status `ready` deltaP `4.5953` edge `0.0205` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.5949` n `224` status `ready` deltaP `-0.4491` edge `-0.0048` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.7291` n `224` status `ready` deltaP `15.3746` edge `0.0104` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7448` n `224` status `ready` deltaP `-0.4304` edge `-0.0015` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8183` n `224` status `ready` deltaP `-3.5447` edge `-0.0045` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3735` n `224` status `ready` deltaP `-2.3411` edge `-0.0115` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5319` n `224` status `ready` deltaP `-2.3631` edge `-0.0218` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.6718` n `224` status `ready` deltaP `3.133` edge `-0.0172` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.8161` n `224` status `ready` deltaP `6.3807` edge `-0.0174` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1031` n `224` status `ready` deltaP `3.5387` edge `0.0051` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6589` n `224` status `ready` deltaP `2.5152` edge `0.0007` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7815` n `224` status `ready` deltaP `-0.0871` edge `-0.0233` maxDD `-16.9508`
- `market_context_high->commodity_24h` score `-2.8443` n `200` status `ready` deltaP `-2.565` edge `-0.0331` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `-2.9233` n `224` status `ready` deltaP `-7.2082` edge `0.041` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.0579` n `200` status `ready` deltaP `-4.2938` edge `-0.0059` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.9412` n `224` status `ready` deltaP `3.7783` edge `-0.1206` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.1931` n `200` status `ready` deltaP `-11.8674` edge `-0.1117` maxDD `-28.433`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
