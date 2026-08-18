# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T13:37:26.784467+00:00`
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

- `market_context_high->crypto_major_24h` score `2.4122` n `88` status `ready` deltaP `9.5262` edge `0.2583` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6687` n `88` status `ready` deltaP `18.2488` edge `0.2756` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0964` n `96` status `ready` deltaP `9.7618` edge `0.0567` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.7043` n `96` status `ready` deltaP `14.126` edge `0.0221` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6599` n `96` status `ready` deltaP `12.9179` edge `0.0076` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.5656` n `96` status `ready` deltaP `9.0193` edge `0.0891` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.5544` n `96` status `ready` deltaP `9.506` edge `0.0055` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.244` n `96` status `ready` deltaP `9.6037` edge `0.0833` maxDD `-5.4926`
- `market_context_high->equity_4h` score `0.0855` n `96` status `ready` deltaP `2.9217` edge `0.0781` maxDD `-2.5696`
- `market_context_high->metal_1h` score `-0.0705` n `96` status `ready` deltaP `3.7238` edge `0.008` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1981` n `96` status `ready` deltaP `3.6839` edge `0.0003` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `-0.3448` n `88` status `ready` deltaP `11.3774` edge `-0.0856` maxDD `-0.1855`
- `market_context_high->commodity_4h` score `-0.3805` n `96` status `ready` deltaP `3.938` edge `0.01` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.3808` n `96` status `ready` deltaP `2.0771` edge `0.0175` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4709` n `96` status `ready` deltaP `-3.8673` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4756` n `96` status `ready` deltaP `1.3348` edge `0.0146` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.6359` n `96` status `ready` deltaP `0.3303` edge `0.0103` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8931` n `96` status `ready` deltaP `-7.7408` edge `-0.0063` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.1966` n `88` status `ready` deltaP `-7.8462` edge `0.0187` maxDD `-7.5076`
- `market_context_high->fx_24h` score `-4.615` n `88` status `ready` deltaP `-30.8059` edge `-0.0303` maxDD `-1.2459`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
