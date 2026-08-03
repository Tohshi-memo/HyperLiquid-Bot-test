# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T07:53:03.914071+00:00`
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

- `market_context_high->crypto_alt_24h` score `12.8799` n `40` status `ready` deltaP `51.4583` edge `0.77` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.9854` n `40` status `ready` deltaP `51.3194` edge `0.5861` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.2967` n `32` status `ready` deltaP `-8.0793` edge `0.2362` maxDD `-3.2755`
- `news_risk_high->commodity_1h` score `0.8335` n `32` status `ready` deltaP `17.7208` edge `0.0099` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.7647` n `32` status `ready` deltaP `11.2847` edge `0.0579` maxDD `-1.5526`
- `news_risk_high->commodity_4h` score `0.5779` n `32` status `ready` deltaP `15.3201` edge `-0.0039` maxDD `-1.6728`
- `market_context_high->commodity_1h` score `0.344` n `47` status `ready` deltaP `7.4149` edge `0.0321` maxDD `-1.3282`
- `news_risk_high->crypto_alt_1h` score `0.2978` n `32` status `ready` deltaP `13.6976` edge `0.0109` maxDD `-3.1233`
- `market_context_high->commodity_4h` score `0.2903` n `47` status `ready` deltaP `4.8813` edge `0.0893` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.1317` n `32` status `ready` deltaP `-1.5244` edge `0.0592` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1189` n `32` status `ready` deltaP `5.1067` edge `0.0359` maxDD `-0.3761`
- `news_risk_high->index_1h` score `0.0615` n `32` status `ready` deltaP `4.4536` edge `-0.002` maxDD `-0.5845`
- `market_context_high->fx_1h` score `0.0149` n `47` status `ready` deltaP `7.4149` edge `-0.0086` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.0085` n `47` status `ready` deltaP `13.4179` edge `-0.0045` maxDD `-1.8531`
- `market_context_high->crypto_alt_4h` score `-0.2369` n `47` status `ready` deltaP `2.1439` edge `0.0459` maxDD `-4.9116`
- `news_risk_high->metal_1h` score `-0.3238` n `32` status `ready` deltaP `-1.0479` edge `-0.0026` maxDD `-0.5538`
- `news_risk_high->fx_1h` score `-0.425` n `32` status `ready` deltaP `-1.0292` edge `0.0026` maxDD `-0.1588`
- `news_risk_high->crypto_major_1h` score `-0.5516` n `32` status `ready` deltaP `5.2208` edge `-0.0335` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.6815` n `40` status `ready` deltaP `0.6597` edge `0.0368` maxDD `-2.506`
- `news_risk_high->equity_1h` score `-0.9244` n `32` status `ready` deltaP `-8.9446` edge `0.0234` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
