# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T04:52:24.687531+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6373`

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

- `market_context_high->unknown_24h` score `5881.1474` n `63` status `ready` deltaP `-0.7936` edge `490.1177` maxDD `-0.6766`
- `market_context_high->unknown_4h` score `291.6844` n `63` status `ready` deltaP `4.1425` edge `24.2838` maxDD `-0.0174`
- `news_risk_high->unknown_1h` score `81.5872` n `108` status `ready` deltaP `-5.1951` edge `6.8622` maxDD `-0.9571`
- `market_context_high->equity_24h` score `18.1183` n `63` status `ready` deltaP `35.5407` edge `1.347` maxDD `-3.2594`
- `market_context_high->unknown_1h` score `15.8349` n `63` status `ready` deltaP `3.7996` edge `1.3053` maxDD `-0.2178`
- `news_risk_high->crypto_alt_24h` score `13.5472` n `98` status `ready` deltaP `32.2421` edge `1.0496` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.4651` n `63` status `ready` deltaP `55.3075` edge `0.1837` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.2449` n `108` status `ready` deltaP `19.8171` edge `0.4436` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `2.7946` n `63` status `ready` deltaP `27.0422` edge `0.086` maxDD `-0.3387`
- `market_context_high->commodity_24h` score `2.6771` n `63` status `ready` deltaP `36.2103` edge `0.1935` maxDD `-4.6677`
- `market_context_high->crypto_alt_24h` score `1.7343` n `63` status `ready` deltaP `-9.0278` edge `0.3565` maxDD `-8.8096`
- `market_context_high->equity_4h` score `1.3783` n `63` status `ready` deltaP `0.0315` edge `0.2479` maxDD `-2.379`
- `market_context_high->metal_4h` score `1.2544` n `63` status `ready` deltaP `15.2585` edge `0.0453` maxDD `-0.7323`
- `market_context_high->crypto_major_4h` score `1.237` n `63` status `ready` deltaP `20.7293` edge `0.1493` maxDD `-7.3124`
- `market_context_high->crypto_major_24h` score `1.2352` n `63` status `ready` deltaP `5.382` edge `0.227` maxDD `-5.6946`
- `market_context_high->crypto_alt_4h` score `1.0363` n `63` status `ready` deltaP `14.6584` edge `0.1897` maxDD `-9.3654`
- `news_risk_high->crypto_alt_1h` score `0.8217` n `108` status `ready` deltaP `8.727` edge `0.1057` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.6067` n `63` status `ready` deltaP `8.1005` edge `0.0214` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5688` n `63` status `ready` deltaP `13.7321` edge `-0.0002` maxDD `-0.1407`
- `market_context_high->equity_1h` score `0.1602` n `63` status `ready` deltaP `-3.5192` edge `0.1266` maxDD `-2.275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
