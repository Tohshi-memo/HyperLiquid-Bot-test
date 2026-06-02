# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T13:52:23.567456+00:00`
- Price records: `672`
- Market context records: `2668`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->crypto_alt_24h` score `9.2844` n `111` status `ready` deltaP `16.1787` edge `1.0152` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.497` n `111` status `ready` deltaP `17.1312` edge `0.6267` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.8342` n `122` status `ready` deltaP `23.9204` edge `0.5085` maxDD `-15.2094`
- `market_context_high->crypto_major_4h` score `2.7808` n `122` status `ready` deltaP `12.0652` edge `0.3323` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.2537` n `122` status `ready` deltaP `7.0721` edge `0.1623` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.6789` n `132` status `ready` deltaP `8.7915` edge `0.1167` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `-0.0258` n `132` status `ready` deltaP `5.4618` edge `0.0797` maxDD `-4.2199`
- `market_context_high->fx_24h` score `-0.0759` n `111` status `ready` deltaP `11.5147` edge `0.0041` maxDD `-0.6418`
- `market_context_high->index_24h` score `-0.1067` n `111` status `ready` deltaP `7.6624` edge `0.0381` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.2003` n `122` status `ready` deltaP `7.1496` edge `0.0108` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.2535` n `132` status `ready` deltaP `1.8599` edge `0.0045` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2616` n `132` status `ready` deltaP `2.0006` edge `0.0228` maxDD `-1.9684`
- `market_context_high->commodity_1h` score `-0.3603` n `132` status `ready` deltaP `3.3206` edge `0.007` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.4427` n `122` status `ready` deltaP `2.2316` edge `0.0136` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.4843` n `111` status `ready` deltaP `7.9627` edge `0.1942` maxDD `-12.4171`
- `market_context_high->fx_1h` score `-0.5429` n `132` status `ready` deltaP `-0.7303` edge `0.004` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6489` n `132` status `ready` deltaP `-1.0661` edge `-0.0013` maxDD `-2.3164`
- `market_context_high->metal_4h` score `-0.684` n `122` status `ready` deltaP `1.142` edge `0.0075` maxDD `-3.8913`
- `market_context_high->commodity_4h` score `-1.28` n `122` status `ready` deltaP `3.0313` edge `0.0077` maxDD `-10.0279`
- `market_context_high->crypto_major_24h` score `-1.3198` n `111` status `ready` deltaP `5.9967` edge `0.5471` maxDD `-44.169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
