# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T08:07:33.308411+00:00`
- Price records: `672`
- Market context records: `5539`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11398`

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

- `market_context_high->equity_24h` score `4.1268` n `190` status `ready` deltaP `14.7442` edge `0.7535` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.2852` n `192` status `ready` deltaP `12.4619` edge `0.3366` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.1816` n `190` status `ready` deltaP `16.2189` edge `0.5277` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.7579` n `192` status `ready` deltaP `8.0665` edge `0.2568` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.5356` n `192` status `ready` deltaP `8.7652` edge `0.2334` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5446` n `190` status `ready` deltaP `14.6674` edge `0.0425` maxDD `-1.2585`
- `market_context_high->equity_1h` score `0.1824` n `192` status `ready` deltaP `6.8894` edge `0.0658` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0969` n `192` status `ready` deltaP `4.5253` edge `0.0111` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3216` n `192` status `ready` deltaP `1.0417` edge `0.0007` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.3261` n `192` status `ready` deltaP `0.9575` edge `0.0626` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4143` n `192` status `ready` deltaP `2.8381` edge `0.0711` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6323` n `192` status `ready` deltaP `0.814` edge `0.0094` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.8198` n `192` status `ready` deltaP `2.9091` edge `0.0057` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.4152` n `192` status `ready` deltaP `3.0742` edge `0.0225` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7473` n `192` status `ready` deltaP `-5.6574` edge `-0.0131` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.9873` n `190` status `ready` deltaP `12.5402` edge `0.0603` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5336` n `192` status `ready` deltaP `-11.3313` edge `-0.0498` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.8148` n `192` status `ready` deltaP `-10.8994` edge `-0.0624` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.2386` n `190` status `ready` deltaP `7.2442` edge `0.2182` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.368` n `190` status `ready` deltaP `-4.2379` edge `-0.1786` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
