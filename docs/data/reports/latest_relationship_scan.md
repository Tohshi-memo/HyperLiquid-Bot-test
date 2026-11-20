# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T09:37:44.855703+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2612`

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

- `market_context_high->unknown_1h` score `11861.5345` n `109` status `ready` deltaP `1.2471` edge `988.4727` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7449.8537` n `108` status `ready` deltaP `0.5194` edge `620.8461` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4481` n `102` status `ready` deltaP `30.77` edge `1.3415` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.562` n `102` status `ready` deltaP `16.8812` edge `1.1216` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.7017` n `108` status `ready` deltaP `5.1603` edge `0.3893` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.4777` n `108` status `ready` deltaP `6.2274` edge `0.2892` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5896` n `108` status `ready` deltaP `18.1741` edge `0.0624` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.1945` n `109` status `ready` deltaP `5.0802` edge `0.0164` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2889` n `109` status `ready` deltaP `2.9652` edge `0.0044` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.3652` n `109` status `ready` deltaP `4.3701` edge `0.0637` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-1.105` n `109` status `ready` deltaP `-1.7525` edge `0.0418` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.2523` n `109` status `ready` deltaP `6.1665` edge `0.0324` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.4692` n `109` status `ready` deltaP `-9.7484` edge `-0.0015` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.7456` n `108` status `ready` deltaP `-1.3098` edge `-0.0024` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.3328` n `109` status `ready` deltaP `-8.8118` edge `-0.0257` maxDD `-4.1298`
- `market_context_high->fx_4h` score `-2.3723` n `108` status `ready` deltaP `-14.7979` edge `-0.0039` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.7927` n `102` status `ready` deltaP `14.5425` edge `0.1` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5606` n `102` status `ready` deltaP `-16.8913` edge `-0.0068` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.9139` n `108` status `ready` deltaP `-27.5858` edge `-0.1063` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.0121` n `108` status `ready` deltaP `-5.5273` edge `-0.032` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
