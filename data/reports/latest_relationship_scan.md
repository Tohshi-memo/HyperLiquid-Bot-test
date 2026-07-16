# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T11:37:30.566712+00:00`
- Price records: `672`
- Market context records: `6914`
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

- `market_context_high->unknown_24h` score `-0.1388` n `198` status `ready` deltaP `-5.5731` edge `0.421` maxDD `-14.4643`
- `market_context_high->fx_1h` score `-0.1537` n `224` status `ready` deltaP `3.8842` edge `0.0029` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3899` n `224` status `ready` deltaP `2.9593` edge `0.0242` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4459` n `224` status `ready` deltaP `4.745` edge `0.0216` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.5925` n `224` status `ready` deltaP `-0.4491` edge `-0.0045` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.7212` n `224` status `ready` deltaP `15.527` edge `0.0104` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7549` n `224` status `ready` deltaP `-0.5801` edge `-0.0018` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8183` n `224` status `ready` deltaP `-3.5447` edge `-0.0045` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3413` n `224` status `ready` deltaP `-2.0362` edge `-0.0094` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5391` n `224` status `ready` deltaP `-2.5128` edge `-0.0214` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.6851` n `224` status `ready` deltaP `2.9833` edge `-0.0179` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.8382` n `224` status `ready` deltaP `6.0758` edge `-0.0182` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1275` n `224` status `ready` deltaP `3.2339` edge `0.004` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6722` n `224` status `ready` deltaP `2.3628` edge `0.0` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7815` n `224` status `ready` deltaP `-0.0871` edge `-0.0233` maxDD `-16.9508`
- `market_context_high->commodity_24h` score `-2.7985` n `198` status `ready` deltaP `-2.6224` edge `-0.0289` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `-2.9427` n `224` status `ready` deltaP `-7.3606` edge `0.0404` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.0778` n `198` status `ready` deltaP `-4.5279` edge `-0.006` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.9828` n `224` status `ready` deltaP `3.4734` edge `-0.1239` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.2217` n `198` status `ready` deltaP `-12.2175` edge `-0.1134` maxDD `-28.4043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
