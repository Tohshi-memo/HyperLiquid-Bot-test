# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T14:22:25.046366+00:00`
- Price records: `672`
- Market context records: `2771`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `4.1021` n `136` status `ready` deltaP `8.5069` edge `0.3316` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.5419` n `136` status `ready` deltaP `4.4935` edge `0.6876` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `1.0594` n `142` status `ready` deltaP `6.9478` edge `0.1473` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.2114` n `136` status `ready` deltaP `9.7018` edge `0.2718` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.059` n `142` status `ready` deltaP `10.8618` edge `0.0193` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0481` n `142` status `ready` deltaP `4.0314` edge `0.0422` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1459` n `142` status `ready` deltaP `3.4495` edge `0.0077` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.565` n `142` status `ready` deltaP `0.6157` edge `-0.0012` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5862` n `142` status `ready` deltaP `-1.1364` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.7019` n `142` status `ready` deltaP `-0.1666` edge `-0.0043` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7264` n `142` status `ready` deltaP `5.2459` edge `0.0479` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9763` n `142` status `ready` deltaP `3.4769` edge `0.0386` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1449` n `142` status `ready` deltaP `-3.7973` edge `0.0132` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.2007` n `142` status `ready` deltaP `-4.3627` edge `0.0069` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3516` n `136` status `ready` deltaP `-0.7863` edge `-0.0202` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.3597` n `142` status `ready` deltaP `14.1854` edge `0.2262` maxDD `-28.7261`
- `market_context_high->commodity_4h` score `-1.551` n `142` status `ready` deltaP `0.161` edge `-0.0079` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.0249` n `142` status `ready` deltaP `-0.4766` edge `-0.0276` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.4171` n `142` status `ready` deltaP `-2.6` edge `-0.0375` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.6303` n `142` status `ready` deltaP `5.1249` edge `0.1192` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
