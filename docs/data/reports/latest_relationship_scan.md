# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T13:22:27.636398+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.378` n `88` status `ready` deltaP `9.3529` edge `0.2566` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6749` n `88` status `ready` deltaP `18.2488` edge `0.2764` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0772` n `96` status `ready` deltaP `9.6121` edge `0.0561` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.7189` n `96` status `ready` deltaP `14.2784` edge `0.0223` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6611` n `96` status `ready` deltaP `12.9179` edge `0.0077` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.58` n `96` status `ready` deltaP `9.0193` edge `0.0903` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.5544` n `96` status `ready` deltaP `9.506` edge `0.0055` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.2802` n `96` status `ready` deltaP `9.7561` edge `0.0853` maxDD `-5.4926`
- `market_context_high->equity_4h` score `0.0879` n `96` status `ready` deltaP `2.9217` edge `0.0783` maxDD `-2.5696`
- `market_context_high->metal_1h` score `-0.0693` n `96` status `ready` deltaP `3.7238` edge `0.0081` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1902` n `96` status `ready` deltaP `3.8363` edge `0.0003` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.3448` n `88` status `ready` deltaP `11.3774` edge `-0.0856` maxDD `-0.1855`
- `market_context_high->crypto_alt_1h` score `-0.3808` n `96` status `ready` deltaP `2.0771` edge `0.0175` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.3813` n `96` status `ready` deltaP `3.938` edge `0.0099` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4623` n `96` status `ready` deltaP `-3.7176` edge `0.0014` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4764` n `96` status `ready` deltaP `1.3348` edge `0.0145` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.6213` n `96` status `ready` deltaP `0.4827` edge `0.0105` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8845` n `96` status `ready` deltaP `-7.5911` edge `-0.0062` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2111` n `88` status `ready` deltaP `-8.0195` edge `0.018` maxDD `-7.5076`
- `market_context_high->fx_24h` score `-4.63` n `88` status `ready` deltaP `-30.9792` edge `-0.0304` maxDD `-1.2459`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
