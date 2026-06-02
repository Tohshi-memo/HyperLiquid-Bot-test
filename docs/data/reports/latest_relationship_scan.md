# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T14:37:26.280328+00:00`
- Price records: `672`
- Market context records: `2671`
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

- `market_context_high->crypto_alt_24h` score `9.1025` n `111` status `ready` deltaP `16.0051` edge `1.0012` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5433` n `111` status `ready` deltaP `17.3048` edge `0.6294` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.445` n `125` status `ready` deltaP `22.9549` edge `0.4825` maxDD `-15.2094`
- `market_context_high->crypto_major_4h` score `2.3543` n `125` status `ready` deltaP `10.6488` edge `0.3062` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.5215` n `125` status `ready` deltaP `8.0951` edge `0.1778` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.3743` n `134` status `ready` deltaP `8.0593` edge `0.0962` maxDD `-6.1656`
- `market_context_high->index_4h` score `-0.1278` n `125` status `ready` deltaP `8.0939` edge `0.0138` maxDD `-2.3986`
- `market_context_high->fx_24h` score `-0.1332` n `111` status `ready` deltaP `10.9938` edge `0.0028` maxDD `-0.6418`
- `market_context_high->crypto_major_1h` score `-0.1652` n `134` status `ready` deltaP `4.7748` edge `0.0664` maxDD `-4.2199`
- `market_context_high->index_24h` score `-0.1976` n `111` status `ready` deltaP `7.1415` edge `0.034` maxDD `-2.5127`
- `market_context_high->unknown_1h` score `-0.1987` n `134` status `ready` deltaP `2.2321` edge `0.0265` maxDD `-1.9684`
- `market_context_high->index_1h` score `-0.2071` n `134` status `ready` deltaP `2.3773` edge `0.007` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3496` n `134` status `ready` deltaP `3.2867` edge `0.0086` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.3642` n `134` status `ready` deltaP `-0.9027` edge `0.0037` maxDD `-0.2164`
- `market_context_high->fx_4h` score `-0.4796` n `125` status `ready` deltaP `1.8463` edge `0.0131` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.4999` n `111` status `ready` deltaP `7.9627` edge `0.1922` maxDD `-12.4171`
- `market_context_high->metal_1h` score `-0.754` n `134` status `ready` deltaP `-1.64` edge `-0.0041` maxDD `-2.8644`
- `market_context_high->metal_4h` score `-1.0837` n `125` status `ready` deltaP `0.0207` edge `-0.0048` maxDD `-5.4081`
- `market_context_high->commodity_4h` score `-1.2301` n `125` status `ready` deltaP `3.6756` edge `0.0098` maxDD `-10.0279`
- `market_context_high->crypto_major_24h` score `-1.3525` n `111` status `ready` deltaP `5.9967` edge `0.5429` maxDD `-44.169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
