# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T14:22:28.103853+00:00`
- Price records: `672`
- Market context records: `7037`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_4h` score `-0.1968` n `209` status `ready` deltaP `13.1455` edge `0.0097` maxDD `-1.1388`
- `market_context_high->fx_1h` score `-0.216` n `209` status `ready` deltaP `2.3644` edge `0.0018` maxDD `-0.2872`
- `market_context_high->crypto_alt_1h` score `-0.3252` n `209` status `ready` deltaP `1.9418` edge `0.0318` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.7042` n `209` status `ready` deltaP `0.1862` edge `-0.0004` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7291` n `209` status `ready` deltaP `-2.4733` edge `-0.0002` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.7759` n `209` status `ready` deltaP `-3.292` edge `-0.0159` maxDD `-1.9306`
- `market_context_high->crypto_major_1h` score `-0.9519` n `209` status `ready` deltaP `3.797` edge `0.0306` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.0517` n `209` status `ready` deltaP `-2.3293` edge `0.0068` maxDD `-2.6467`
- `market_context_high->unknown_24h` score `-1.6704` n `200` status `ready` deltaP `-8.9236` edge `0.3182` maxDD `-20.162`
- `market_context_high->equity_1h` score `-1.774` n `209` status `ready` deltaP `4.2224` edge `-0.0133` maxDD `-14.716`
- `market_context_high->unknown_4h` score `-1.8217` n `209` status `ready` deltaP `-6.0524` edge `0.0891` maxDD `-7.3778`
- `market_context_high->index_4h` score `-1.9648` n `209` status `ready` deltaP `5.401` edge `-0.018` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-2.0367` n `209` status `ready` deltaP `4.3514` edge `0.0082` maxDD `-5.5324`
- `market_context_high->commodity_4h` score `-2.039` n `209` status `ready` deltaP `-3.4025` edge `-0.0312` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.3254` n `200` status `ready` deltaP `-0.5556` edge `-0.0592` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.5732` n `209` status `ready` deltaP `2.5258` edge `0.0318` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.8696` n `209` status `ready` deltaP `3.6987` edge `0.0359` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7319` n `200` status `ready` deltaP `-2.6111` edge `-0.0117` maxDD `-3.8841`
- `market_context_high->equity_4h` score `-7.2421` n `209` status `ready` deltaP `5.1852` edge `-0.076` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.1514` n `200` status `ready` deltaP `-13.8125` edge `-0.065` maxDD `-41.4429`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
