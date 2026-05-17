# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T14:22:14.354305+00:00`
- Price records: `672`
- Market context records: `1020`
- Flow alert records: `4845`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.6638` n `193` status `ready` deltaP `32.5055` edge `0.9808` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.3897` n `193` status `ready` deltaP `11.146` edge `0.4149` maxDD `-9.5387`
- `market_context_high->equity_24h` score `1.2089` n `193` status `ready` deltaP `8.0419` edge `0.2156` maxDD `-7.1445`
- `market_context_high->index_24h` score `0.84` n `193` status `ready` deltaP `7.3683` edge `0.1752` maxDD `-4.346`
- `market_context_high->fx_1h` score `-0.1477` n `193` status `ready` deltaP `3.9202` edge `0.0005` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.4786` n `193` status `ready` deltaP `2.5046` edge `0.0242` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7365` n `193` status `ready` deltaP `2.3184` edge `0.0057` maxDD `-2.6023`
- `market_context_high->equity_1h` score `-0.749` n `193` status `ready` deltaP `-0.5027` edge `0.0178` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.8514` n `193` status `ready` deltaP `3.7943` edge `0.0034` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.235` n `193` status `ready` deltaP `4.7493` edge `-0.0177` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.3202` n `193` status `ready` deltaP `2.2937` edge `0.0899` maxDD `-10.5498`
- `market_context_high->crypto_alt_1h` score `-1.3284` n `193` status `ready` deltaP `-0.9967` edge `-0.0197` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.417` n `193` status `ready` deltaP `0.0687` edge `0.0291` maxDD `-6.1444`
- `market_context_high->metal_1h` score `-1.7544` n `193` status `ready` deltaP `0.6384` edge `-0.0389` maxDD `-8.5553`
- `market_context_high->crypto_alt_4h` score `-2.6623` n `193` status `ready` deltaP `0.8333` edge `0.0504` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-2.7132` n `193` status `ready` deltaP `7.6946` edge `0.0932` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.2766` n `193` status `ready` deltaP `1.1636` edge `-0.0202` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.3259` n `193` status `ready` deltaP `-2.9698` edge `0.0594` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-4.1865` n `193` status `ready` deltaP `-2.3648` edge `-0.1598` maxDD `-22.2262`
- `market_context_high->metal_24h` score `-5.1382` n `193` status `ready` deltaP `-8.4852` edge `0.2616` maxDD `-40.657`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
