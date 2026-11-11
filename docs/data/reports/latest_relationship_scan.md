# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T04:52:27.328825+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11742`

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

- `market_context_high->unknown_4h` score `79.0582` n `88` status `ready` deltaP `7.525` edge `6.5828` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.4966` n `88` status `ready` deltaP `32.2601` edge `2.8988` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.8638` n `39` status `ready` deltaP `34.463` edge `0.8711` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.9568` n `88` status `ready` deltaP `32.7651` edge `1.3111` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1701` n `88` status `ready` deltaP `31.8497` edge `0.3481` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.8474` n `47` status `ready` deltaP `20.3943` edge `0.2559` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.4899` n `88` status `ready` deltaP `29.1193` edge `0.152` maxDD `-1.4245`
- `news_risk_high->commodity_4h` score `3.3077` n `39` status `ready` deltaP `25.0938` edge `0.1337` maxDD `-0.3611`
- `news_risk_high->metal_4h` score `2.8192` n `39` status `ready` deltaP `31.8989` edge `0.0599` maxDD `-1.0104`
- `news_risk_high->index_4h` score `2.611` n `39` status `ready` deltaP `25.9811` edge `0.088` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.4604` n `39` status `ready` deltaP `30.179` edge `0.2781` maxDD `-10.1088`
- `news_risk_high->crypto_major_4h` score `1.9482` n `39` status `ready` deltaP `19.9226` edge `0.2657` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `1.6069` n `47` status `ready` deltaP `20.8434` edge `0.0204` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4345` n `47` status `ready` deltaP `18.7158` edge `0.0249` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1305` n `47` status `ready` deltaP `23.0571` edge `0.085` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7999` n `47` status `ready` deltaP `21.3785` edge `0.0652` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2099` n `47` status `ready` deltaP `-4.2075` edge `0.0346` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.4175` n `88` status `ready` deltaP `2.5381` edge `-0.0022` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4504` n `88` status `ready` deltaP `3.0485` edge `0.0098` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6683` n `88` status `ready` deltaP `1.5798` edge `0.0144` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
