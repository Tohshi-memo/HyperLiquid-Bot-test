# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T17:22:29.353829+00:00`
- Price records: `672`
- Market context records: `7051`
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

- `market_context_high->fx_4h` score `0.4653` n `197` status `ready` deltaP `14.7263` edge `0.0106` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.3322` n `197` status `ready` deltaP `2.3754` edge `0.0016` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.6012` n `197` status `ready` deltaP `0.9955` edge `0.0297` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7963` n `197` status `ready` deltaP `-1.1057` edge `-0.0036` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8008` n `197` status `ready` deltaP `-3.6642` edge `-0.0166` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-0.8225` n `197` status `ready` deltaP `-3.969` edge `-0.0022` maxDD `-2.1427`
- `market_context_high->unknown_1h` score `-0.8947` n `197` status `ready` deltaP `-2.5768` edge `0.0155` maxDD `-2.1637`
- `market_context_high->crypto_major_1h` score `-0.9573` n `197` status `ready` deltaP `3.6247` edge `0.0313` maxDD `-7.1523`
- `market_context_high->unknown_4h` score `-1.3301` n `197` status `ready` deltaP `-5.6743` edge `0.103` maxDD `-5.748`
- `market_context_high->equity_1h` score `-1.9726` n `197` status `ready` deltaP `3.0138` edge `-0.0307` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.1208` n `197` status `ready` deltaP `3.4689` edge `0.0033` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.1853` n `197` status `ready` deltaP `2.6456` edge `-0.0279` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.2375` n `197` status `ready` deltaP `-0.7165` edge `-0.0508` maxDD `-4.4704`
- `market_context_high->commodity_4h` score `-2.2996` n `197` status `ready` deltaP `-5.4901` edge `-0.039` maxDD `-2.9494`
- `market_context_high->crypto_alt_4h` score `-2.6039` n `197` status `ready` deltaP `2.8955` edge `0.0254` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.8048` n `197` status `ready` deltaP `4.5693` edge `0.0384` maxDD `-24.6094`
- `market_context_high->unknown_24h` score `-3.1172` n `197` status `ready` deltaP `-12.3987` edge `0.1977` maxDD `-23.5076`
- `market_context_high->fx_24h` score `-3.5164` n `197` status `ready` deltaP `-0.0934` edge `-0.0097` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.7293` n `197` status `ready` deltaP `3.2554` edge `-0.1256` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.0421` n `197` status `ready` deltaP `-17.1972` edge `-0.0795` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
