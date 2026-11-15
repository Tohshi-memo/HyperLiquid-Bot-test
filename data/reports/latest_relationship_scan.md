# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T08:22:24.481940+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9934`

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

- `market_context_high->unknown_24h` score `539.1621` n `66` status `ready` deltaP `2.4263` edge `44.914` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.4122` n `50` status `ready` deltaP `48.8319` edge `3.4461` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1811` n `66` status `ready` deltaP `42.6501` edge `3.0516` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.6868` n `66` status `ready` deltaP `57.8121` edge `2.2795` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.7535` n `50` status `ready` deltaP `46.3882` edge `2.8504` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.3151` n `50` status `ready` deltaP `39.372` edge `0.8768` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.0545` n `50` status `ready` deltaP `16.9636` edge `1.3701` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.5328` n `66` status `ready` deltaP `44.9372` edge `0.3373` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.3509` n `50` status `ready` deltaP `49.0468` edge `0.2856` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3365` n `50` status `ready` deltaP `40.513` edge `0.2883` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.0808` n `66` status `ready` deltaP `57.2922` edge `0.4868` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.6465` n `50` status `ready` deltaP `23.4329` edge `0.4519` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.1007` n `50` status `ready` deltaP `46.2134` edge `0.1546` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `5.0587` n `50` status `ready` deltaP `29.4329` edge `0.3689` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0355` n `50` status `ready` deltaP `21.6467` edge `0.255` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4674` n `50` status `ready` deltaP `31.6951` edge `0.103` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `3.0749` n `66` status `ready` deltaP `12.6306` edge `1.2046` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.8448` n `50` status `ready` deltaP `28.0` edge `0.0854` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.3167` n `50` status `ready` deltaP `26.491` edge `0.0419` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3238` n `50` status `ready` deltaP `17.497` edge `0.0238` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
