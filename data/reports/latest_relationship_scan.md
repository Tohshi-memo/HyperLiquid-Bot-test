# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T14:07:20.264984+00:00`
- Price records: `672`
- Market context records: `2251`
- Flow alert records: `8373`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9227`

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

- `news_risk_high->crypto_alt_24h` score `24.0313` n `43` status `ready` deltaP `54.5502` edge `1.6978` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.2182` n `43` status `ready` deltaP `44.2022` edge `1.1008` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.8009` n `43` status `ready` deltaP `35.1744` edge `1.1137` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `13.5072` n `43` status `ready` deltaP `25.1493` edge `1.016` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `10.2304` n `115` status `ready` deltaP `31.4085` edge `0.6843` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `9.7939` n `43` status `ready` deltaP `35.453` edge `0.6024` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `9.6561` n `134` status `ready` deltaP `29.3684` edge `0.8156` maxDD `-11.8702`
- `market_context_high->crypto_major_4h` score `8.9542` n `134` status `ready` deltaP `34.8175` edge `0.6521` maxDD `-7.7094`
- `market_context_high->crypto_major_24h` score `7.058` n `115` status `ready` deltaP `18.8602` edge `1.1684` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.2654` n `134` status `ready` deltaP `20.3176` edge `0.3643` maxDD `-1.8773`
- `market_context_high->index_4h` score `4.055` n `134` status `ready` deltaP `31.1522` edge `0.1676` maxDD `-0.3228`
- `news_risk_high->index_24h` score `3.9107` n `43` status `ready` deltaP `13.2712` edge `0.2793` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.8236` n `43` status `ready` deltaP `32.6148` edge `0.3399` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6651` n `43` status `ready` deltaP `37.2295` edge `0.0757` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.521` n `115` status `ready` deltaP `15.071` edge `0.2447` maxDD `-1.4737`
- `market_context_high->equity_24h` score `3.4398` n `115` status `ready` deltaP `22.7174` edge `0.2879` maxDD `-6.8828`
- `news_risk_high->commodity_24h` score `2.9718` n `43` status `ready` deltaP `2.0309` edge `0.3158` maxDD `-3.202`
- `market_context_high->equity_4h` score `2.8439` n `134` status `ready` deltaP `20.5042` edge `0.2202` maxDD `-4.2589`
- `news_risk_high->fx_4h` score `2.0819` n `43` status `ready` deltaP `26.5173` edge `0.0151` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.9276` n `146` status `ready` deltaP `13.227` edge `0.1892` maxDD `-6.0065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
