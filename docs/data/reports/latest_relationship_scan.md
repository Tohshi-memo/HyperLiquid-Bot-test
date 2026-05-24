# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T22:52:17.176923+00:00`
- Price records: `672`
- Market context records: `1785`
- Flow alert records: `7034`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8882`

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

- `market_context_high->metal_24h` score `7.1708` n `186` status `ready` deltaP `28.3154` edge `0.6514` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.0842` n `30` status `ready` deltaP `27.7338` edge `0.3876` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.85` n `194` status `ready` deltaP `21.7076` edge `0.5194` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.4476` n `194` status `ready` deltaP `22.935` edge `0.4583` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.7369` n `194` status `ready` deltaP `15.7546` edge `0.4335` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.1523` n `30` status `ready` deltaP `24.2715` edge `0.1326` maxDD `-1.2043`
- `market_context_high->index_24h` score `3.095` n `186` status `ready` deltaP `15.9387` edge `0.2745` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.0551` n `194` status `ready` deltaP `16.6269` edge `0.2532` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8531` n `186` status `ready` deltaP `15.9554` edge `0.5379` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.3258` n `186` status `ready` deltaP `13.1889` edge `0.5546` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9235` n `194` status `ready` deltaP `12.4591` edge `0.1028` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8079` n `30` status `ready` deltaP `20.2643` edge `-0.0043` maxDD `-0.1774`
- `news_risk_high->unknown_4h` score `0.5384` n `30` status `ready` deltaP `11.0467` edge `0.0677` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.5279` n `197` status `ready` deltaP `7.5033` edge `0.1042` maxDD `-4.8183`
- `market_context_high->crypto_major_1h` score `0.1197` n `197` status `ready` deltaP `4.5488` edge `0.087` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0524` n `197` status `ready` deltaP `4.893` edge `0.0526` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1859` n `197` status `ready` deltaP `4.0017` edge `0.021` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2537` n `194` status `ready` deltaP `12.8646` edge `0.1509` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.4176` n `186` status `ready` deltaP `8.6413` edge `0.0125` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4364` n `30` status `ready` deltaP `17.006` edge `-0.1221` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
