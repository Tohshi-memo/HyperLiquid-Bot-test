# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T13:37:32.020319+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3916`

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

- `news_risk_high->equity_24h` score `0.3856` n `116` status `ready` deltaP `24.3259` edge `1.0459` maxDD `-86.0244`
- `news_risk_high->index_4h` score `-0.0133` n `116` status `ready` deltaP `9.735` edge `0.0128` maxDD `-2.0195`
- `news_risk_high->index_1h` score `-0.2442` n `116` status `ready` deltaP `6.1429` edge `0.0019` maxDD `-0.9325`
- `news_risk_high->fx_1h` score `-0.3817` n `116` status `ready` deltaP `-1.1924` edge `-0.0007` maxDD `-0.2232`
- `news_risk_high->index_24h` score `-0.551` n `116` status `ready` deltaP `-2.2431` edge `0.1278` maxDD `-6.6786`
- `news_risk_high->crypto_alt_4h` score `-0.6117` n `116` status `ready` deltaP `3.648` edge `0.1609` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6455` n `116` status `ready` deltaP `1.5331` edge `0.0298` maxDD `-5.8225`
- `news_risk_high->metal_1h` score `-0.9709` n `116` status `ready` deltaP `-2.7359` edge `-0.0107` maxDD `-1.1577`
- `news_risk_high->crypto_major_4h` score `-1.0991` n `116` status `ready` deltaP `-2.9857` edge `0.0601` maxDD `-9.1553`
- `news_risk_high->fx_4h` score `-1.1406` n `116` status `ready` deltaP `-1.8923` edge `-0.0015` maxDD `-0.4745`
- `news_risk_high->fx_24h` score `-1.2969` n `116` status `ready` deltaP `-14.9147` edge `-0.0034` maxDD `-0.4086`
- `news_risk_high->equity_1h` score `-1.3854` n `116` status `ready` deltaP `-0.8621` edge `0.0184` maxDD `-10.2217`
- `news_risk_high->crypto_major_1h` score `-1.4738` n `116` status `ready` deltaP `-3.0405` edge `-0.002` maxDD `-4.7103`
- `news_risk_high->equity_4h` score `-1.7593` n `116` status `ready` deltaP `10.1924` edge `0.1165` maxDD `-21.818`
- `news_risk_high->metal_4h` score `-2.3422` n `116` status `ready` deltaP `-5.8926` edge `-0.0443` maxDD `-2.5944`
- `news_risk_high->commodity_1h` score `-2.7324` n `116` status `ready` deltaP `-12.9672` edge `-0.0046` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.3441` n `116` status `ready` deltaP `-3.5139` edge `-0.2157` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.8958` n `116` status `ready` deltaP `-23.4231` edge `-0.0164` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.2743` n `116` status `ready` deltaP `-16.8864` edge `0.1585` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.3013` n `116` status `ready` deltaP `-23.7233` edge `0.0046` maxDD `-39.0575`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
