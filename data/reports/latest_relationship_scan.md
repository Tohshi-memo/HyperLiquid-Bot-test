# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T14:05:51.236723+00:00`
- Price records: `672`
- Market context records: `3080`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6901`

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

- `market_context_high->crypto_alt_24h` score `17.2817` n `88` status `ready` deltaP `12.0265` edge `2.5271` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `15.1783` n `88` status `ready` deltaP `47.2538` edge `0.9788` maxDD `-1.6506`
- `market_context_high->unknown_24h` score `14.0576` n `88` status `ready` deltaP `23.3901` edge `1.062` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.564` n `88` status `ready` deltaP `32.6705` edge `0.9465` maxDD `-7.0507`
- `market_context_high->equity_24h` score `10.712` n `88` status `ready` deltaP `24.4003` edge `1.5386` maxDD `-22.2351`
- `market_context_high->commodity_4h` score `2.6978` n `124` status `ready` deltaP `16.7879` edge `0.1587` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `-0.1125` n `124` status `ready` deltaP `3.3389` edge `0.0737` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.3034` n `125` status `ready` deltaP `-0.6479` edge `0.0213` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.6472` n `125` status `ready` deltaP `1.6958` edge `0.012` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.7804` n `125` status `ready` deltaP `3.497` edge `0.0896` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-1.0486` n `125` status `ready` deltaP `-7.2024` edge `-0.0021` maxDD `-0.3147`
- `market_context_high->unknown_1h` score `-1.0575` n `125` status `ready` deltaP `1.509` edge `-0.0251` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.1572` n `88` status `ready` deltaP `-0.6787` edge `-0.0049` maxDD `-0.6271`
- `market_context_high->equity_1h` score `-1.2213` n `125` status `ready` deltaP `-1.3497` edge `-0.0009` maxDD `-8.7345`
- `market_context_high->fx_4h` score `-1.3288` n `124` status `ready` deltaP `-11.9689` edge `-0.0062` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4332` n `124` status `ready` deltaP `8.694` edge `0.0492` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.9336` n `125` status `ready` deltaP `0.3389` edge `0.0629` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.194` n `125` status `ready` deltaP `-5.8084` edge `-0.0073` maxDD `-7.278`
- `market_context_high->crypto_alt_4h` score `-3.0593` n `124` status `ready` deltaP `17.9485` edge `0.2926` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7822` n `124` status `ready` deltaP `6.9089` edge `-0.0071` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
