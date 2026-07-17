# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T09:18:46.132225+00:00`
- Price records: `672`
- Market context records: `7013`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2729` n `229` status `ready` deltaP `1.8775` edge `0.001` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.3627` n `216` status `ready` deltaP `-5.7291` edge `0.4467` maxDD `-18.7342`
- `market_context_high->crypto_alt_1h` score `-0.5082` n `229` status `ready` deltaP `1.903` edge `0.0314` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6286` n `229` status `ready` deltaP `-0.7806` edge `0.0014` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.6407` n `229` status `ready` deltaP `1.091` edge `0.0017` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-1.0111` n `229` status `ready` deltaP `3.5373` edge `0.0274` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-1.0171` n `229` status `ready` deltaP `10.481` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.2459` n `229` status `ready` deltaP `-2.4266` edge `-0.0155` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.2861` n `229` status `ready` deltaP `-1.8409` edge `-0.0048` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.696` n `229` status `ready` deltaP `-4.5073` edge `-0.0384` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7643` n `229` status `ready` deltaP `8.0419` edge `-0.0099` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.7889` n `229` status `ready` deltaP `4.1354` edge `-0.0015` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8556` n `229` status `ready` deltaP `7.3384` edge `0.0115` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.4863` n `229` status `ready` deltaP `-6.1083` edge `0.0693` maxDD `-10.1948`
- `market_context_high->crypto_alt_4h` score `-2.6876` n `229` status `ready` deltaP `1.8253` edge `0.0218` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.1229` n `216` status `ready` deltaP `-4.6297` edge `-0.086` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.22` n `216` status `ready` deltaP `-5.8449` edge `-0.0157` maxDD `-5.0932`
- `market_context_high->crypto_major_4h` score `-4.8422` n `229` status `ready` deltaP `1.8046` edge `0.0129` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-11.3188` n `229` status `ready` deltaP `5.2615` edge `-0.0566` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.3706` n `216` status `ready` deltaP `-9.4328` edge `-0.0544` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
