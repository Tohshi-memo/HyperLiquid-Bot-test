# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T03:37:29.455706+00:00`
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

- `market_context_high->unknown_4h` score `80.1394` n `88` status `ready` deltaP `7.525` edge `6.6729` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.5566` n `88` status `ready` deltaP `32.2601` edge `2.9038` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.0917` n `37` status `ready` deltaP `33.6314` edge `0.8123` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.6302` n `88` status `ready` deltaP `32.2443` edge `1.2727` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1437` n `88` status `ready` deltaP `31.8497` edge `0.3459` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.8448` n `46` status `ready` deltaP `20.3918` edge `0.2557` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `3.2355` n `37` status `ready` deltaP `23.8464` edge `0.136` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.1924` n `88` status `ready` deltaP `28.2512` edge `0.133` maxDD `-1.4245`
- `news_risk_high->index_4h` score `2.4191` n `37` status `ready` deltaP `24.8723` edge `0.0794` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.165` n `37` status `ready` deltaP `28.6544` edge `0.2504` maxDD `-10.1088`
- `news_risk_high->crypto_major_4h` score `1.8049` n `37` status `ready` deltaP `20.2415` edge `0.2452` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `1.6595` n `37` status `ready` deltaP `30.9287` edge `0.0442` maxDD `-1.0104`
- `news_risk_high->metal_1h` score `1.554` n `46` status `ready` deltaP `20.2421` edge `0.02` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3959` n `46` status `ready` deltaP `18.3676` edge `0.024` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.0586` n `46` status `ready` deltaP `22.4095` edge `0.0801` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6991` n `46` status `ready` deltaP `20.3853` edge `0.0589` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1554` n `46` status `ready` deltaP `-3.2934` edge `0.0355` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.4261` n `88` status `ready` deltaP `2.3884` edge `-0.0023` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.448` n `88` status `ready` deltaP `3.0485` edge `0.01` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6847` n `88` status `ready` deltaP `1.5798` edge `0.0123` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
