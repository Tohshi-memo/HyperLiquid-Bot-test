# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T23:37:29.469640+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `75.0875` n `88` status `ready` deltaP `7.525` edge `6.2519` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2604` n `88` status `ready` deltaP `33.6489` edge `2.9545` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.9298` n `88` status `ready` deltaP `30.161` edge `1.1968` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.0732` n `88` status `ready` deltaP `31.3289` edge `0.3435` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `2.9216` n `33` status `ready` deltaP `14.3849` edge `0.2191` maxDD `-3.7228`
- `market_context_high->metal_24h` score `2.369` n `88` status `ready` deltaP `25.4735` edge `0.0829` maxDD `-1.4245`
- `news_risk_high->index_1h` score `1.0184` n `33` status `ready` deltaP `14.3849` edge `0.0191` maxDD `-0.4103`
- `news_risk_high->metal_1h` score `0.4952` n `33` status `ready` deltaP `10.0073` edge `0.0` maxDD `-0.3692`
- `news_risk_high->crypto_alt_1h` score `0.4319` n `33` status `ready` deltaP `17.9777` edge `0.0293` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.1823` n `33` status `ready` deltaP `17.828` edge `0.0097` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.0394` n `33` status `ready` deltaP `-3.9104` edge `0.0461` maxDD `-0.1983`
- `news_risk_high->fx_1h` score `-0.2455` n `33` status `ready` deltaP `0.1679` edge `-0.0036` maxDD `-0.3199`
- `market_context_high->metal_1h` score `-0.3425` n `88` status `ready` deltaP `3.9467` edge `0.0128` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.356` n `88` status `ready` deltaP `3.2866` edge `0.0007` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6045` n `88` status `ready` deltaP `2.342` edge `0.0175` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6082` n `88` status `ready` deltaP `3.8525` edge `-0.0059` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9745` n `88` status `ready` deltaP `-7.206` edge `0.0062` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0474` n `88` status `ready` deltaP `-1.0532` edge `0.0111` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2338` n `88` status `ready` deltaP `-12.7109` edge `-0.005` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5364` n `88` status `ready` deltaP `-7.206` edge `0.0357` maxDD `-8.1039`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
