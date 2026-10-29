# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T18:22:40.793800+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6816`

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

- `market_context_high->unknown_24h` score `1619.9238` n `134` status `ready` deltaP `-0.881` edge `135.0425` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `64.9574` n `134` status `ready` deltaP `6.3615` edge `5.384` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.0988` n `134` status `ready` deltaP `26.236` edge `0.0183` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3306` n `134` status `ready` deltaP `10.4545` edge `0.0106` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1677` n `134` status `ready` deltaP `12.4135` edge `0.0531` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0823` n `134` status `ready` deltaP `13.087` edge `0.0129` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.0769` n `134` status `ready` deltaP `4.0285` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3715` n `134` status `ready` deltaP `1.0457` edge `0.0135` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4506` n `134` status `ready` deltaP `0.7463` edge `-0.0029` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.4832` n `134` status `ready` deltaP `5.0697` edge `0.0287` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.4937` n `134` status `ready` deltaP `1.4881` edge `0.0365` maxDD `-2.3383`
- `market_context_high->fx_24h` score `-0.9444` n `134` status `ready` deltaP `6.0557` edge `0.014` maxDD `-0.9792`
- `market_context_high->index_1h` score `-0.9864` n `134` status `ready` deltaP `-3.5928` edge `-0.0024` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.1986` n `134` status `ready` deltaP `1.8009` edge `0.0208` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.6112` n `134` status `ready` deltaP `-2.9441` edge `-0.0285` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.7084` n `134` status `ready` deltaP `3.9257` edge `0.0195` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.465` n `134` status `ready` deltaP `-7.349` edge `-0.0244` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.8049` n `134` status `ready` deltaP `4.3502` edge `-0.0591` maxDD `-19.0267`
- `market_context_high->equity_24h` score `-3.2375` n `134` status `ready` deltaP `8.6728` edge `-0.0519` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.5741` n `134` status `ready` deltaP `0.2099` edge `-0.0288` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
