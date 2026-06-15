# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T21:22:49.561956+00:00`
- Price records: `672`
- Market context records: `4027`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `145.914` n `40` status `ready` deltaP `-6.2195` edge `12.3826` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.914` n `40` status `ready` deltaP `-6.2195` edge `12.3826` maxDD `-10.864`
- `market_context_high->unknown_24h` score `47.4981` n `134` status `ready` deltaP `-5.6792` edge `4.3989` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `25.5799` n `148` status `ready` deltaP `1.821` edge `2.6618` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `5.6768` n `40` status `ready` deltaP `37.435` edge `0.2235` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.6768` n `40` status `ready` deltaP `37.435` edge `0.2235` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.2219` n `40` status `ready` deltaP `35.7622` edge `0.0348` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2219` n `40` status `ready` deltaP `35.7622` edge `0.0348` maxDD `-0.0446`
- `market_context_high->index_24h` score `3.1651` n `134` status `ready` deltaP `24.3837` edge `0.1224` maxDD `-1.3629`
- `market_context_high->equity_4h` score `2.0828` n `148` status `ready` deltaP `18.6676` edge `0.1772` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.9815` n `134` status `ready` deltaP `12.3943` edge `0.1812` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.1867` n `156` status `ready` deltaP `8.4984` edge `0.0982` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.0085` n `40` status `ready` deltaP `18.689` edge `0.026` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0085` n `40` status `ready` deltaP `18.689` edge `0.026` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.8546` n `40` status `ready` deltaP `4.0295` edge `0.2725` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.8546` n `40` status `ready` deltaP `4.0295` edge `0.2725` maxDD `-12.9187`
- `risk_on_high->index_24h` score `0.7228` n `40` status `ready` deltaP `25.13` edge `-0.1073` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.7228` n `40` status `ready` deltaP `25.13` edge `-0.1073` maxDD `0.0`
- `market_context_high->crypto_major_1h` score `0.549` n `156` status `ready` deltaP `7.6693` edge `0.0556` maxDD `-2.8785`
- `market_context_high->metal_1h` score `0.4288` n `156` status `ready` deltaP `10.1297` edge `0.05` maxDD `-3.0049`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
