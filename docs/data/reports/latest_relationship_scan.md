# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T08:09:34.559845+00:00`
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

- `market_context_high->crypto_alt_24h` score `12.8235` n `40` status `ready` deltaP `51.4583` edge `0.7653` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.9734` n `40` status `ready` deltaP `51.3194` edge `0.5851` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.3039` n `32` status `ready` deltaP `-8.0793` edge `0.2368` maxDD `-3.2755`
- `news_risk_high->commodity_1h` score `0.8218` n `32` status `ready` deltaP `17.5711` edge `0.0094` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.7647` n `32` status `ready` deltaP `11.2847` edge `0.0579` maxDD `-1.5526`
- `news_risk_high->commodity_4h` score `0.5609` n `32` status `ready` deltaP `15.1677` edge `-0.0043` maxDD `-1.6728`
- `market_context_high->commodity_1h` score `0.3323` n `47` status `ready` deltaP `7.2652` edge `0.0316` maxDD `-1.3282`
- `news_risk_high->crypto_alt_1h` score `0.2947` n `32` status `ready` deltaP `13.6976` edge `0.0105` maxDD `-3.1233`
- `market_context_high->commodity_4h` score `0.2792` n `47` status `ready` deltaP `4.7289` edge `0.0889` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.1329` n `32` status `ready` deltaP `-1.5244` edge `0.0593` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.111` n `32` status `ready` deltaP `4.9543` edge `0.0359` maxDD `-0.3761`
- `news_risk_high->index_1h` score `0.0701` n `32` status `ready` deltaP `4.6033` edge `-0.0019` maxDD `-0.5845`
- `market_context_high->fx_1h` score `0.0235` n `47` status `ready` deltaP `7.5646` edge `-0.0085` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.0207` n `47` status `ready` deltaP `13.2655` edge `-0.0045` maxDD `-1.8531`
- `market_context_high->crypto_alt_4h` score `-0.2377` n `47` status `ready` deltaP `2.1439` edge `0.0458` maxDD `-4.9116`
- `news_risk_high->metal_1h` score `-0.3323` n `32` status `ready` deltaP `-1.1976` edge `-0.0027` maxDD `-0.5538`
- `news_risk_high->fx_1h` score `-0.4118` n `32` status `ready` deltaP `-0.8795` edge `0.0027` maxDD `-0.1588`
- `news_risk_high->crypto_major_1h` score `-0.5532` n `32` status `ready` deltaP `5.2208` edge `-0.0337` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.6815` n `40` status `ready` deltaP `0.6597` edge `0.0368` maxDD `-2.506`
- `news_risk_high->equity_1h` score `-0.9119` n `32` status `ready` deltaP `-8.7949` edge `0.024` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
