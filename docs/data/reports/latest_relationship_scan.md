# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T10:37:23.911371+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11488`

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

- `market_context_high->unknown_4h` score `81.3138` n `88` status `ready` deltaP `8.1347` edge `6.7667` maxDD `-0.9161`
- `market_context_high->equity_24h` score `32.6176` n `88` status `ready` deltaP `28.9614` edge `2.7642` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.4271` n `52` status `ready` deltaP `37.3944` edge `0.8985` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.0029` n `88` status `ready` deltaP `36.7582` edge `1.4186` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.8495` n `88` status `ready` deltaP `29.0719` edge `0.3399` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.1785` n `88` status `ready` deltaP `31.2026` edge `0.1955` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.7122` n `53` status `ready` deltaP `18.464` edge `0.2575` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5619` n `52` status `ready` deltaP `36.2336` edge `0.0929` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.3915` n `52` status `ready` deltaP `27.4155` edge `0.1252` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.2337` n `52` status `ready` deltaP `19.2191` edge `0.2901` maxDD `-9.2335`
- `news_risk_high->index_4h` score `2.3984` n `52` status `ready` deltaP `22.4085` edge `0.0941` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7086` n `52` status `ready` deltaP `23.5225` edge `0.2261` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.667` n `53` status `ready` deltaP `20.7999` edge `0.0257` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3712` n `53` status `ready` deltaP `17.7748` edge `0.0259` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7093` n `53` status `ready` deltaP `18.4922` edge `0.0656` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6396` n `53` status `ready` deltaP `18.6419` edge `0.0629` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1408` n `53` status `ready` deltaP `-2.35` edge `0.0374` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3352` n `88` status `ready` deltaP `3.6473` edge `0.0154` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4292` n `88` status `ready` deltaP `2.3884` edge `-0.0027` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.6665` n `88` status `ready` deltaP `3.0903` edge `-0.0083` maxDD `-2.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
