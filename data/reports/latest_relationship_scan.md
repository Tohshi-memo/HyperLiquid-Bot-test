# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T03:22:34.166982+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_4h` score `13.1048` n `35` status `ready` deltaP `29.7256` edge `0.8939` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.7061` n `35` status `ready` deltaP `47.2561` edge `0.2438` maxDD `0.0`
- `news_risk_high->unknown_1h` score `5.1439` n `47` status `ready` deltaP `26.7868` edge `0.2619` maxDD `-0.2787`
- `news_risk_high->fx_4h` score `3.1838` n `35` status `ready` deltaP `37.3127` edge `0.03` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `2.1229` n `35` status `ready` deltaP `27.3302` edge `0.0031` maxDD `-0.0045`
- `market_context_high->unknown_1h` score `1.5417` n `135` status `ready` deltaP `6.314` edge `0.1091` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.5035` n `47` status `ready` deltaP `20.2765` edge `0.0071` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1956` n `47` status `ready` deltaP `23.3023` edge `0.0261` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.964` n `135` status `ready` deltaP `20.096` edge `-0.0323` maxDD `-0.3736`
- `news_risk_high->index_4h` score `0.5258` n `35` status `ready` deltaP `12.2866` edge `0.0241` maxDD `-0.0884`
- `news_risk_high->commodity_1h` score `0.4044` n `47` status `ready` deltaP `11.1352` edge `-0.0097` maxDD `-0.4666`
- `news_risk_high->metal_1h` score `0.1064` n `47` status `ready` deltaP `6.3989` edge `-0.0067` maxDD `-0.1184`
- `market_context_high->fx_4h` score `0.0959` n `135` status `ready` deltaP `8.1063` edge `0.0085` maxDD `-0.3527`
- `news_risk_high->index_1h` score `0.0152` n `47` status `ready` deltaP `5.1694` edge `0.0028` maxDD `-0.1583`
- `market_context_high->index_1h` score `-0.0626` n `135` status `ready` deltaP `6.1466` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1747` n `135` status `ready` deltaP `1.364` edge `0.0044` maxDD `-0.2043`
- `news_risk_high->crypto_major_4h` score `-0.2975` n `35` status `ready` deltaP `-1.4722` edge `0.1217` maxDD `-6.9344`
- `market_context_high->equity_1h` score `-0.3416` n `135` status `ready` deltaP `4.4844` edge `0.0333` maxDD `-5.2257`
- `news_risk_high->commodity_4h` score `-0.3874` n `35` status `ready` deltaP `3.6716` edge `-0.0238` maxDD `-1.0273`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
