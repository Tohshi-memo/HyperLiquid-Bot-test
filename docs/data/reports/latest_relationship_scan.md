# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T02:22:33.389174+00:00`
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

- `market_context_high->unknown_4h` score `80.8618` n `88` status `ready` deltaP `7.525` edge `6.7331` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.7135` n `88` status `ready` deltaP `32.7809` edge `2.9134` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `9.0146` n `32` status `ready` deltaP `31.0976` edge `0.6561` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.4101` n `88` status `ready` deltaP `31.8971` edge `1.2468` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1305` n `88` status `ready` deltaP `31.8497` edge `0.3448` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.8097` n `41` status `ready` deltaP `19.9832` edge `0.2555` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `3.0615` n `32` status `ready` deltaP `20.3506` edge `0.1448` maxDD `-0.3611`
- `market_context_high->metal_24h` score `2.931` n `88` status `ready` deltaP `27.3832` edge `0.117` maxDD `-1.4245`
- `news_risk_high->index_1h` score `1.5323` n `41` status `ready` deltaP `19.9832` edge `0.0246` maxDD `-0.4103`
- `news_risk_high->metal_1h` score `1.3394` n `41` status `ready` deltaP `17.5442` edge `0.0201` maxDD `-0.3692`
- `news_risk_high->metal_4h` score `1.2587` n `32` status `ready` deltaP `28.125` edge `0.0115` maxDD `-1.0104`
- `news_risk_high->index_4h` score `1.2321` n `32` status `ready` deltaP `21.4939` edge `0.0583` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.216` n `32` status `ready` deltaP `24.0091` edge `0.1597` maxDD `-10.1088`
- `news_risk_high->crypto_major_4h` score `1.1246` n `32` status `ready` deltaP `14.3293` edge `0.1974` maxDD `-9.2335`
- `news_risk_high->crypto_alt_1h` score `0.8925` n `41` status `ready` deltaP `21.7358` edge `0.0633` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6328` n `41` status `ready` deltaP `21.7358` edge `0.0414` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.3246` n `41` status `ready` deltaP `-6.5028` edge `0.0352` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3653` n `88` status `ready` deltaP `3.797` edge `0.0119` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3911` n `88` status `ready` deltaP `2.8375` edge `-0.0008` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6727` n `88` status `ready` deltaP `1.8847` edge `0.0118` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
