# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T16:26:51.901947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5901`

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

- `news_risk_high->unknown_24h` score `4543.0038` n `66` status `ready` deltaP `26.4047` edge `378.4497` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.3015` n `40` status `ready` deltaP `57.7083` edge `1.0968` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.905` n `40` status `ready` deltaP `51.3194` edge `0.5794` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.8062` n `68` status `ready` deltaP `18.5078` edge `0.3535` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7837` n `68` status `ready` deltaP `17.7456` edge `0.0684` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0247` n `40` status `ready` deltaP `13.1402` edge `0.1284` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.7402` n `68` status `ready` deltaP `10.6904` edge `0.0727` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.7303` n `40` status `ready` deltaP `9.2683` edge `0.1224` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6186` n `40` status `ready` deltaP `19.8476` edge `0.0266` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.6015` n `40` status `ready` deltaP `11.3473` edge `0.0389` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.4707` n `40` status `ready` deltaP `14.2964` edge `0.0028` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.266` n `68` status `ready` deltaP `13.8182` edge `0.0258` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1996` n `68` status `ready` deltaP `6.6894` edge `0.0286` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1474` n `68` status `ready` deltaP `7.08` edge `0.0399` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.0341` n `68` status `ready` deltaP `3.0645` edge `0.0075` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.0412` n `68` status `ready` deltaP `3.267` edge `0.0052` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1069` n `68` status `ready` deltaP `3.0645` edge `0.0062` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1096` n `68` status `ready` deltaP `3.7161` edge `0.0332` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.3607` n `40` status `ready` deltaP `1.1976` edge `0.0085` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6755` n `68` status `ready` deltaP `2.8179` edge `-0.0274` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
