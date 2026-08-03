# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T07:38:09.014183+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5903`

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

- `market_context_high->crypto_alt_24h` score `12.9327` n `40` status `ready` deltaP `51.4583` edge `0.7744` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.9938` n `40` status `ready` deltaP `51.3194` edge `0.5868` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.2919` n `32` status `ready` deltaP `-8.0793` edge `0.2358` maxDD `-3.2755`
- `news_risk_high->commodity_1h` score `0.8444` n `32` status `ready` deltaP `17.8705` edge `0.0103` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.7647` n `32` status `ready` deltaP `11.2847` edge `0.0579` maxDD `-1.5526`
- `news_risk_high->commodity_4h` score `0.5803` n `32` status `ready` deltaP `15.3201` edge `-0.0037` maxDD `-1.6728`
- `market_context_high->commodity_1h` score `0.3549` n `47` status `ready` deltaP `7.5646` edge `0.0325` maxDD `-1.3282`
- `news_risk_high->crypto_alt_1h` score `0.2986` n `32` status `ready` deltaP `13.6976` edge `0.011` maxDD `-3.1233`
- `market_context_high->commodity_4h` score `0.2918` n `47` status `ready` deltaP `4.8813` edge `0.0895` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.1317` n `32` status `ready` deltaP `-1.5244` edge `0.0592` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1268` n `32` status `ready` deltaP `5.2591` edge `0.0359` maxDD `-0.3761`
- `news_risk_high->index_1h` score `0.0615` n `32` status `ready` deltaP `4.4536` edge `-0.002` maxDD `-0.5845`
- `market_context_high->fx_1h` score `0.0063` n `47` status `ready` deltaP `7.2652` edge `-0.0087` maxDD `-0.7804`
- `market_context_high->fx_4h` score `0.0037` n `47` status `ready` deltaP `13.5703` edge `-0.0045` maxDD `-1.8531`
- `market_context_high->crypto_alt_4h` score `-0.2369` n `47` status `ready` deltaP `2.1439` edge `0.0459` maxDD `-4.9116`
- `news_risk_high->metal_1h` score `-0.3238` n `32` status `ready` deltaP `-1.0479` edge `-0.0026` maxDD `-0.5538`
- `news_risk_high->fx_1h` score `-0.4381` n `32` status `ready` deltaP `-1.1789` edge `0.0025` maxDD `-0.1588`
- `news_risk_high->crypto_major_1h` score `-0.5532` n `32` status `ready` deltaP `5.2208` edge `-0.0337` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.6815` n `40` status `ready` deltaP `0.6597` edge `0.0368` maxDD `-2.506`
- `news_risk_high->equity_1h` score `-0.9353` n `32` status `ready` deltaP `-9.0943` edge `0.023` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
