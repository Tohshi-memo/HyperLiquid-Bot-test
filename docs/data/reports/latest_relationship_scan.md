# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T08:22:27.542783+00:00`
- Price records: `672`
- Market context records: `5963`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11184`

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

- `news_risk_high->fx_24h` score `7.0356` n `30` status `ready` deltaP `64.4097` edge `0.1569` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.2584` n `30` status `ready` deltaP `37.882` edge `0.2062` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.843` n `30` status `ready` deltaP `39.8476` edge `0.0592` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.122` n `30` status `ready` deltaP `25.5788` edge `0.0202` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.476` n `231` status `ready` deltaP `9.4717` edge `0.1693` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8388` n `30` status `ready` deltaP `10.1896` edge `0.0863` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2029` n `30` status `ready` deltaP `5.3194` edge `0.0367` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1578` n `30` status `ready` deltaP `6.9791` edge `0.0204` maxDD `-2.3058`
- `market_context_high->equity_24h` score `-0.3681` n `213` status `ready` deltaP `21.4838` edge `0.3172` maxDD `-31.2762`
- `market_context_high->equity_1h` score `-0.3776` n `241` status `ready` deltaP `4.4302` edge `0.0349` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.3853` n `30` status `ready` deltaP `1.986` edge `-0.026` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4694` n `241` status `ready` deltaP `2.5946` edge `0.0024` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5677` n `241` status `ready` deltaP `-2.5132` edge `-0.0003` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.653` n `241` status `ready` deltaP `0.4385` edge `0.0047` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6567` n `241` status `ready` deltaP `-0.4516` edge `-0.0006` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.117` n `30` status `ready` deltaP `-10.5988` edge `-0.0211` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1411` n `241` status `ready` deltaP `1.6281` edge `0.0196` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1457` n `241` status `ready` deltaP `1.7647` edge `0.0166` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.5018` n `231` status `ready` deltaP `-1.9356` edge `-0.0083` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.5706` n `231` status `ready` deltaP `-2.0153` edge `-0.0247` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
