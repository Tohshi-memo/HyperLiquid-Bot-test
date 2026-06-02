# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T14:22:29.228756+00:00`
- Price records: `672`
- Market context records: `2670`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9240`

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

- `market_context_high->crypto_alt_24h` score `9.1469` n `111` status `ready` deltaP `16.0051` edge `1.0049` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5234` n `111` status `ready` deltaP `17.1312` edge `0.6289` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.657` n `124` status `ready` deltaP `23.4904` edge `0.4966` maxDD `-15.2094`
- `market_context_high->crypto_major_4h` score `2.5246` n `124` status `ready` deltaP `11.1133` edge `0.3173` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.4803` n `124` status `ready` deltaP `7.7596` edge `0.1766` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.5617` n `133` status `ready` deltaP `8.4969` edge `0.1089` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `-0.0797` n `133` status `ready` deltaP `5.19` edge `0.0746` maxDD `-4.2199`
- `market_context_high->fx_24h` score `-0.1133` n `111` status `ready` deltaP `11.1674` edge `0.0033` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-0.1155` n `133` status `ready` deltaP `2.492` edge `0.0317` maxDD `-1.9684`
- `market_context_high->index_4h` score `-0.1471` n `124` status `ready` deltaP `7.7842` edge `0.0134` maxDD `-2.3986`
- `market_context_high->index_24h` score `-0.1657` n `111` status `ready` deltaP `7.3152` edge `0.0355` maxDD `-2.5127`
- `market_context_high->index_1h` score `-0.2243` n `133` status `ready` deltaP `2.196` edge `0.006` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3378` n `133` status `ready` deltaP `3.5298` edge `0.0085` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.3754` n `133` status `ready` deltaP `-1.1177` edge `0.0037` maxDD `-0.2164`
- `market_context_high->commodity_24h` score `-0.4999` n `111` status `ready` deltaP `7.9627` edge `0.1922` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-0.5085` n `124` status `ready` deltaP `1.485` edge `0.0131` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-0.7146` n `133` status `ready` deltaP `-1.2809` edge `-0.0031` maxDD `-2.7313`
- `market_context_high->metal_4h` score `-0.9663` n `124` status `ready` deltaP `0.3884` edge `-0.0014` maxDD `-5.0058`
- `market_context_high->commodity_4h` score `-1.2441` n `124` status `ready` deltaP `3.4667` edge `0.0094` maxDD `-10.0279`
- `market_context_high->crypto_major_24h` score `-1.3416` n `111` status `ready` deltaP `5.9967` edge `0.5443` maxDD `-44.169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
