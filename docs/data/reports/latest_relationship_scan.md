# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T00:07:30.131249+00:00`
- Price records: `672`
- Market context records: `7304`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13813`

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

- `market_context_high->fx_1h` score `-0.1` n `126` status `ready` deltaP `5.148` edge `0.0018` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5979` n `126` status `ready` deltaP `-1.1154` edge `-0.012` maxDD `-1.5775`
- `market_context_high->crypto_major_1h` score `-0.7487` n `126` status `ready` deltaP `3.4146` edge `0.0223` maxDD `-7.6171`
- `market_context_high->commodity_4h` score `-0.7519` n `120` status `ready` deltaP `1.896` edge `-0.0122` maxDD `-2.4139`
- `market_context_high->fx_24h` score `-0.8217` n `114` status `ready` deltaP `2.2121` edge `0.0027` maxDD `-2.1564`
- `market_context_high->index_1h` score `-0.8381` n `126` status `ready` deltaP `-5.2124` edge `-0.0085` maxDD `-2.1355`
- `market_context_high->fx_4h` score `-0.9946` n `120` status `ready` deltaP `3.3104` edge `0.0104` maxDD `-1.4649`
- `market_context_high->crypto_alt_1h` score `-1.0689` n `126` status `ready` deltaP `-1.1382` edge `0.0224` maxDD `-5.9775`
- `market_context_high->unknown_4h` score `-1.4362` n `120` status `ready` deltaP `4.9187` edge `0.0834` maxDD `-6.2031`
- `market_context_high->unknown_1h` score `-1.742` n `126` status `ready` deltaP `0.8079` edge `-0.0882` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.8532` n `120` status `ready` deltaP `2.9878` edge `0.0168` maxDD `-15.2776`
- `market_context_high->metal_1h` score `-2.1801` n `126` status `ready` deltaP `-10.0941` edge `-0.004` maxDD `-1.4971`
- `market_context_high->metal_4h` score `-2.3751` n `120` status `ready` deltaP `-8.2826` edge `-0.0011` maxDD `-4.8549`
- `market_context_high->crypto_major_4h` score `-2.807` n `120` status `ready` deltaP `3.6382` edge `0.0053` maxDD `-23.4879`
- `market_context_high->unknown_24h` score `-3.0412` n `115` status `ready` deltaP `-7.5619` edge `-0.0349` maxDD `-12.3663`
- `market_context_high->commodity_24h` score `-3.5576` n `114` status `ready` deltaP `-7.0953` edge `-0.1694` maxDD `-2.3815`
- `market_context_high->equity_1h` score `-4.3745` n `126` status `ready` deltaP `-9.1806` edge `-0.0657` maxDD `-14.3442`
- `market_context_high->index_4h` score `-4.4281` n `120` status `ready` deltaP `-13.1193` edge `-0.0469` maxDD `-8.4382`
- `market_context_high->crypto_alt_24h` score `-8.7418` n `115` status `ready` deltaP `3.3741` edge `-0.2503` maxDD `-61.4351`
- `market_context_high->metal_24h` score `-10.7106` n `115` status `ready` deltaP `-28.0964` edge `-0.1237` maxDD `-19.8569`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
