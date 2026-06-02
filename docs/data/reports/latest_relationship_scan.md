# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T00:37:21.322830+00:00`
- Price records: `672`
- Market context records: `2613`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.9974` n `146` status `ready` deltaP `18.2958` edge `0.5773` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.1895` n `146` status `ready` deltaP `25.0439` edge `0.5334` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.4249` n `146` status `ready` deltaP `14.6112` edge `0.369` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.3496` n `146` status `ready` deltaP `11.4306` edge `0.155` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0567` n `146` status `ready` deltaP `7.6846` edge `0.1418` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.7329` n `146` status `ready` deltaP `8.8631` edge `0.1214` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.7086` n `146` status `ready` deltaP `8.6282` edge `0.0996` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.5776` n `146` status `ready` deltaP `2.0643` edge `0.6722` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2` n `146` status `ready` deltaP `8.8227` edge `0.042` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0916` n `146` status `ready` deltaP `4.3905` edge `0.0125` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4051` n `146` status `ready` deltaP `5.502` edge `0.0174` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4704` n `146` status `ready` deltaP `1.8005` edge `0.0151` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.5901` n `146` status `ready` deltaP `1.5606` edge `0.0152` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6377` n `146` status `ready` deltaP `-0.5352` edge `0.0039` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7605` n `146` status `ready` deltaP `-0.0779` edge `0.021` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.7628` n `146` status `ready` deltaP `4.1973` edge `0.0472` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.8878` n `146` status `ready` deltaP `4.062` edge `-0.0017` maxDD `-1.6157`
- `market_context_high->fx_4h` score `-0.9094` n `146` status `ready` deltaP `-0.2255` edge `0.0115` maxDD `-0.8621`
- `market_context_high->commodity_4h` score `-1.0481` n `146` status `ready` deltaP `3.6439` edge `0.0356` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.3794` n `146` status `ready` deltaP `1.6497` edge `0.0145` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
