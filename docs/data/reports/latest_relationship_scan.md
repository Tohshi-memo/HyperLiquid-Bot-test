# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T11:21:04.707205+00:00`
- Price records: `672`
- Market context records: `6913`
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

- `market_context_high->unknown_24h` score `-0.0985` n `197` status `ready` deltaP `-5.5028` edge `0.4257` maxDD `-14.4643`
- `market_context_high->fx_1h` score `-0.1537` n `224` status `ready` deltaP `3.8842` edge `0.0029` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3875` n `224` status `ready` deltaP `2.9593` edge `0.0244` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4399` n `224` status `ready` deltaP `4.745` edge `0.0221` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6019` n `224` status `ready` deltaP `-0.5988` edge `-0.0047` maxDD `-2.1443`
- `market_context_high->fx_4h` score `-0.7212` n `224` status `ready` deltaP `15.527` edge `0.0104` maxDD `-2.1765`
- `market_context_high->index_1h` score `-0.7557` n `224` status `ready` deltaP `-0.5801` edge `-0.0019` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.8183` n `224` status `ready` deltaP `-3.5447` edge `-0.0045` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3279` n `224` status `ready` deltaP `-1.8838` edge `-0.0087` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5391` n `224` status `ready` deltaP `-2.5128` edge `-0.0214` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.6851` n `224` status `ready` deltaP `2.9833` edge `-0.0179` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.8516` n `224` status `ready` deltaP `5.9234` edge `-0.0189` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.1314` n `224` status `ready` deltaP `3.2339` edge `0.0035` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.6864` n `224` status `ready` deltaP `2.2104` edge `-0.0008` maxDD `-20.6678`
- `market_context_high->commodity_24h` score `-2.7443` n `197` status `ready` deltaP `-2.3199` edge `-0.0264` maxDD `-5.2791`
- `market_context_high->crypto_major_4h` score `-2.7854` n `224` status `ready` deltaP `-0.0871` edge `-0.0238` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9633` n `224` status `ready` deltaP `-7.5131` edge `0.0397` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.0863` n `197` status `ready` deltaP `-4.6494` edge `-0.0059` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.0134` n `224` status `ready` deltaP `3.321` edge `-0.1268` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.2277` n `197` status `ready` deltaP `-12.2267` edge `-0.1141` maxDD `-28.4043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
