# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T02:07:28.243614+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.8039` n `60` status `ready` deltaP `33.5413` edge `432.2188` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.6634` n `53` status `ready` deltaP `60.737` edge `1.1901` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8093` n `68` status `ready` deltaP `17.1359` edge `0.3629` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.7367` n `68` status `ready` deltaP `16.6786` edge `0.0716` maxDD `-0.3783`
- `market_context_high->commodity_24h` score `1.7088` n `53` status `ready` deltaP `27.4844` edge `0.2217` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.7594` n `53` status `ready` deltaP `9.805` edge `0.1277` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.7067` n `68` status `ready` deltaP `10.0916` edge `0.0739` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.2699` n `53` status `ready` deltaP `14.6255` edge `0.0167` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.1359` n `53` status `ready` deltaP `10.3528` edge `0.0464` maxDD `-2.506`
- `news_risk_high->metal_4h` score `0.1219` n `68` status `ready` deltaP `5.165` edge `0.0288` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0632` n `68` status `ready` deltaP `6.0321` edge `0.0361` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `0.0373` n `68` status `ready` deltaP `11.3791` edge `0.023` maxDD `-0.6604`
- `market_context_high->commodity_1h` score `-0.0099` n `53` status `ready` deltaP `5.0757` edge `0.019` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0149` n `53` status `ready` deltaP `7.2026` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0536` n `68` status `ready` deltaP `2.6154` edge `0.008` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.1113` n `68` status `ready` deltaP `2.0694` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1217` n `68` status `ready` deltaP `2.7651` edge `0.0063` maxDD `-0.5599`
- `market_context_high->commodity_4h` score `-0.2317` n `53` status `ready` deltaP `3.4198` edge `0.035` maxDD `-3.0005`
- `news_risk_high->crypto_major_1h` score `-0.2513` n `68` status `ready` deltaP `1.6203` edge `0.029` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.6428` n `68` status `ready` deltaP `3.7161` edge `-0.0292` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
