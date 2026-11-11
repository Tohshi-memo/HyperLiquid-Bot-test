# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T03:52:31.884703+00:00`
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

- `market_context_high->unknown_4h` score `80.0506` n `88` status `ready` deltaP `7.525` edge `6.6655` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.5398` n `88` status `ready` deltaP `32.2601` edge `2.9024` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1085` n `37` status `ready` deltaP `33.6314` edge `0.8137` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.6762` n `88` status `ready` deltaP `32.2443` edge `1.2786` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1485` n `88` status `ready` deltaP `31.8497` edge `0.3463` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.9121` n `47` status `ready` deltaP `20.8434` edge `0.2583` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.2459` n `88` status `ready` deltaP `28.4249` edge `0.1363` maxDD `-1.4245`
- `news_risk_high->commodity_4h` score `3.2403` n `37` status `ready` deltaP `23.8464` edge `0.1364` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4227` n `37` status `ready` deltaP `24.8723` edge `0.0797` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1861` n `37` status `ready` deltaP `28.6544` edge `0.2531` maxDD `-10.1088`
- `news_risk_high->crypto_major_4h` score `1.8212` n `37` status `ready` deltaP `20.2415` edge `0.2473` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `1.6666` n `37` status `ready` deltaP `30.9287` edge `0.0451` maxDD `-1.0104`
- `news_risk_high->metal_1h` score `1.5937` n `47` status `ready` deltaP `20.6937` edge `0.0203` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4489` n `47` status `ready` deltaP `18.8655` edge `0.0251` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1071` n `47` status `ready` deltaP `22.9074` edge `0.083` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7492` n `47` status `ready` deltaP `20.9294` edge `0.0617` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2099` n `47` status `ready` deltaP `-4.2075` edge `0.0346` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.4175` n `88` status `ready` deltaP `2.5381` edge `-0.0022` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4635` n `88` status `ready` deltaP `2.8988` edge `0.0097` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6815` n `88` status `ready` deltaP `1.5798` edge `0.0127` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
