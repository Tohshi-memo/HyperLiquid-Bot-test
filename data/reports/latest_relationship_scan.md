# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T13:37:30.221337+00:00`
- Price records: `672`
- Market context records: `2667`
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

- `market_context_high->crypto_alt_24h` score `9.0232` n `112` status `ready` deltaP `15.749` edge `0.9963` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.4427` n `112` status `ready` deltaP `17.1875` edge `0.6218` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.6104` n `122` status `ready` deltaP `23.2532` edge `0.4943` maxDD `-15.2094`
- `market_context_high->crypto_major_4h` score `2.629` n `122` status `ready` deltaP `11.3979` edge `0.3241` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.2573` n `122` status `ready` deltaP `7.0721` edge `0.1626` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.7341` n `132` status `ready` deltaP `8.7915` edge `0.1213` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.0698` n `132` status `ready` deltaP `6.0697` edge `0.0879` maxDD `-4.2199`
- `market_context_high->index_24h` score `-0.0496` n `112` status `ready` deltaP `7.9117` edge `0.0412` maxDD `-2.5127`
- `market_context_high->fx_24h` score `-0.1177` n `112` status `ready` deltaP `11.0367` edge `0.0038` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-0.1686` n `132` status `ready` deltaP `2.6084` edge `0.0265` maxDD `-1.9684`
- `market_context_high->index_4h` score `-0.2926` n `122` status `ready` deltaP `7.1496` edge `0.0121` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.3672` n `132` status `ready` deltaP `1.8599` edge `0.0064` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3705` n `132` status `ready` deltaP `3.3206` edge `0.0057` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.4415` n `122` status `ready` deltaP `2.2316` edge `0.0137` maxDD `-0.5631`
- `market_context_high->fx_1h` score `-0.5429` n `132` status `ready` deltaP `-0.7303` edge `0.004` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6074` n `132` status `ready` deltaP `-1.0661` edge `-0.0004` maxDD `-1.9622`
- `market_context_high->commodity_24h` score `-0.7055` n `112` status `ready` deltaP `7.4157` edge `0.1792` maxDD `-13.1939`
- `market_context_high->metal_4h` score `-0.9365` n `122` status `ready` deltaP `1.142` edge `0.0079` maxDD `-3.4847`
- `market_context_high->commodity_4h` score `-1.2855` n `122` status `ready` deltaP `3.0313` edge `0.007` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.3119` n `132` status `ready` deltaP `-5.0353` edge `0.0081` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
