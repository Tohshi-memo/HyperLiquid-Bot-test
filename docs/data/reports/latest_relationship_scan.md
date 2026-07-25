# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T13:07:28.329639+00:00`
- Price records: `672`
- Market context records: `7880`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14671`

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

- `market_context_high->equity_24h` score `13.6145` n `112` status `ready` deltaP `29.4039` edge `1.0727` maxDD `-6.0681`
- `market_context_high->equity_4h` score `4.6014` n `112` status `ready` deltaP `13.705` edge `0.3897` maxDD `-5.1426`
- `market_context_high->metal_24h` score `3.9378` n `112` status `ready` deltaP `20.2947` edge `0.2974` maxDD `-1.0304`
- `market_context_high->crypto_alt_4h` score `1.6388` n `112` status `ready` deltaP `14.037` edge `0.1547` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.5654` n `112` status `ready` deltaP `16.2386` edge `0.194` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.5357` n `112` status `ready` deltaP `21.379` edge `0.1438` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.1731` n `114` status `ready` deltaP `13.0832` edge `0.0514` maxDD `-1.6021`
- `market_context_high->fx_24h` score `1.1296` n `112` status `ready` deltaP `30.7626` edge `0.0485` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.8807` n `114` status `ready` deltaP `12.4609` edge `0.1116` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.515` n `112` status `ready` deltaP `8.6205` edge `0.0448` maxDD `-1.0817`
- `market_context_high->index_4h` score `0.4966` n `112` status `ready` deltaP `13.8577` edge `0.0581` maxDD `-1.0614`
- `market_context_high->crypto_alt_1h` score `0.3768` n `114` status `ready` deltaP `5.0783` edge `0.0408` maxDD `-1.4603`
- `market_context_high->index_1h` score `0.3728` n `114` status `ready` deltaP `8.4418` edge `0.0178` maxDD `-0.7743`
- `market_context_high->metal_4h` score `0.2407` n `112` status `ready` deltaP `8.1526` edge `0.0957` maxDD `-1.0661`
- `market_context_high->commodity_1h` score `0.0497` n `114` status `ready` deltaP `5.5262` edge `0.0132` maxDD `-0.6722`
- `market_context_high->index_24h` score `-0.3831` n `112` status `ready` deltaP `-0.3497` edge `0.116` maxDD `-1.6473`
- `market_context_high->fx_1h` score `-0.4065` n `114` status `ready` deltaP `0.7194` edge `-0.0002` maxDD `-0.4112`
- `market_context_high->metal_1h` score `-0.5659` n `114` status `ready` deltaP `0.7316` edge `0.0233` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-0.8492` n `112` status `ready` deltaP `0.4144` edge `0.0001` maxDD `-1.605`
- `market_context_high->crypto_alt_24h` score `-1.6558` n `112` status `ready` deltaP `12.3672` edge `0.2348` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
