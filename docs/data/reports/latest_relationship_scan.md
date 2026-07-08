# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T07:22:31.264374+00:00`
- Price records: `672`
- Market context records: `6064`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11108`

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

- `news_risk_high->fx_24h` score `8.1414` n `30` status `ready` deltaP `72.7431` edge `0.1935` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3805` n `30` status `ready` deltaP `45.3354` edge `0.0674` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `2.9071` n `30` status `ready` deltaP `28.5764` edge `0.0665` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.3885` n `31` status `ready` deltaP `28.6845` edge `0.0217` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `1.5231` n `30` status `ready` deltaP `21.9098` edge `0.0014` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.4181` n `206` status `ready` deltaP `8.4892` edge `0.1533` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.0569` n `31` status `ready` deltaP `12.7197` edge `0.0974` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.4362` n `31` status `ready` deltaP `7.4657` edge `0.0523` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0852` n `30` status `ready` deltaP `9.2361` edge `0.0365` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4789` n `206` status `ready` deltaP `2.5318` edge `0.0016` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5067` n `206` status `ready` deltaP `0.6075` edge `-0.0006` maxDD `-0.6538`
- `news_risk_high->metal_1h` score `-0.7085` n `31` status `ready` deltaP `-1.6805` edge `-0.0361` maxDD `-1.4819`
- `market_context_high->commodity_1h` score `-0.7398` n `206` status `ready` deltaP `-2.2818` edge `-0.0018` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8176` n `206` status `ready` deltaP `4.9997` edge `0.0386` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8547` n `206` status `ready` deltaP `4.2556` edge `0.0373` maxDD `-9.3536`
- `market_context_high->index_4h` score `-0.965` n `206` status `ready` deltaP `1.6532` edge `0.0186` maxDD `-1.9335`
- `market_context_high->equity_1h` score `-1.0361` n `206` status `ready` deltaP `0.9302` edge `0.0203` maxDD `-4.3608`
- `news_risk_high->index_1h` score `-1.1264` n `31` status `ready` deltaP `-10.2424` edge `-0.0198` maxDD `-1.1725`
- `market_context_high->metal_4h` score `-1.1696` n `206` status `ready` deltaP `3.2664` edge `-0.0005` maxDD `-3.4996`
- `market_context_high->commodity_4h` score `-1.2733` n `206` status `ready` deltaP `-4.9506` edge `-0.0233` maxDD `-2.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
