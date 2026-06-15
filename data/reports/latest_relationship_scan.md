# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T14:52:40.721969+00:00`
- Price records: `672`
- Market context records: `4001`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10252`

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

- `risk_on_high->unknown_4h` score `146.852` n `40` status `ready` deltaP `-3.0183` edge `12.439` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `146.852` n `40` status `ready` deltaP `-3.0183` edge `12.439` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `47.8095` n `136` status `ready` deltaP `-3.0024` edge `4.406` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `25.934` n `148` status `ready` deltaP `2.9952` edge `2.6821` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.064` n `40` status `ready` deltaP `41.8403` edge `0.4764` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.064` n `40` status `ready` deltaP `41.8403` edge `0.4764` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.0312` n `40` status `ready` deltaP `38.2012` edge `0.086` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.0312` n `40` status `ready` deltaP `38.2012` edge `0.086` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.2688` n `136` status `ready` deltaP `26.5727` edge `0.1957` maxDD `-6.7031`
- `market_context_high->metal_24h` score `2.842` n `136` status `ready` deltaP `14.9306` edge `0.2872` maxDD `-8.9923`
- `risk_on_high->index_24h` score `2.6215` n `40` status `ready` deltaP `29.5139` edge `0.0217` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.6215` n `40` status `ready` deltaP `29.5139` edge `0.0217` maxDD `0.0`
- `market_context_high->equity_4h` score `2.0116` n `148` status `ready` deltaP `19.7553` edge `0.1662` maxDD `-7.0879`
- `market_context_high->equity_24h` score `1.8503` n `136` status `ready` deltaP `16.8403` edge `0.3449` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.5486` n `40` status `ready` deltaP `20.6707` edge `0.0578` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.5486` n `40` status `ready` deltaP `20.6707` edge `0.0578` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.177` n `148` status `ready` deltaP `12.5344` edge `0.062` maxDD `-1.7983`
- `market_context_high->crypto_major_1h` score `1.0643` n `148` status `ready` deltaP `10.5155` edge `0.0728` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `1.0503` n `40` status `ready` deltaP `4.1667` edge `0.2879` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0503` n `40` status `ready` deltaP `4.1667` edge `0.2879` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
