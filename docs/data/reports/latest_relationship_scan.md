# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T08:37:26.652331+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11722`

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

- `market_context_high->unknown_4h` score `81.0578` n `88` status `ready` deltaP `7.8298` edge `6.7474` maxDD `-0.9161`
- `market_context_high->equity_24h` score `33.4811` n `88` status `ready` deltaP `30.3503` edge `2.8269` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `13.0945` n `47` status `ready` deltaP `37.0816` edge `0.9562` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.7529` n `88` status `ready` deltaP `35.3693` edge `1.3958` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.0194` n `88` status `ready` deltaP `30.4608` edge `0.3448` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.0758` n `88` status `ready` deltaP `31.029` edge `0.1881` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.8829` n `47` status `ready` deltaP `23.4335` edge `0.3161` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6057` n `52` status `ready` deltaP `17.8835` edge `0.2525` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5052` n `47` status `ready` deltaP `34.954` edge `0.0967` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.2654` n `47` status `ready` deltaP `26.5893` edge `0.1202` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.0931` n `47` status `ready` deltaP `29.4726` edge `0.1049` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.3414` n `47` status `ready` deltaP `28.1461` edge `0.2764` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.5935` n `52` status `ready` deltaP `20.1059` edge `0.0242` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4087` n `52` status `ready` deltaP `18.3326` edge `0.0253` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7249` n `52` status `ready` deltaP `17.8028` edge `0.0469` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.5635` n `52` status `ready` deltaP `17.8028` edge `0.0515` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `-0.1863` n `52` status `ready` deltaP `-2.6946` edge `0.0359` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3544` n `88` status `ready` deltaP `3.4976` edge `0.0148` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3817` n `88` status `ready` deltaP `2.9872` edge `-0.0006` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.688` n `88` status `ready` deltaP `1.275` edge `0.0139` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
