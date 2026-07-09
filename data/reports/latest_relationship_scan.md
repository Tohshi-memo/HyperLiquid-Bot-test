# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T01:07:29.865749+00:00`
- Price records: `672`
- Market context records: `6143`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `11.4689` n `30` status `ready` deltaP `40.9027` edge `0.6978` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7493` n `30` status `ready` deltaP `68.5764` edge `0.1886` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3323` n `32` status `ready` deltaP `45.1982` edge `0.0643` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4554` n `32` status `ready` deltaP `29.491` edge `0.0219` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.443` n `195` status `ready` deltaP `0.6549` edge `0.2167` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.1958` n `32` status `ready` deltaP `12.9304` edge `0.1138` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6284` n `32` status `ready` deltaP `8.3271` edge `0.0712` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.3188` n `195` status `ready` deltaP `3.5976` edge `0.0943` maxDD `-2.671`
- `news_risk_high->crypto_major_24h` score `0.0081` n `30` status `ready` deltaP `11.25` edge `0.004` maxDD `-4.2368`
- `news_risk_high->index_24h` score `-0.2087` n `30` status `ready` deltaP `7.5` edge `0.0104` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2341` n `195` status `ready` deltaP `2.1833` edge `0.0` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3629` n `195` status `ready` deltaP `-2.6118` edge `0.2404` maxDD `-11.925`
- `news_risk_high->commodity_24h` score `-0.5983` n `30` status `ready` deltaP `14.0973` edge `-0.1233` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.5998` n `195` status `ready` deltaP `3.847` edge `0.0162` maxDD `-3.4996`
- `market_context_high->metal_24h` score `-0.6841` n `195` status `ready` deltaP `16.7308` edge `0.0576` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.7607` n `195` status `ready` deltaP `-2.1388` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7839` n `32` status `ready` deltaP `-3.2934` edge `-0.0288` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8404` n `195` status `ready` deltaP `2.0912` edge `-0.0041` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8429` n `195` status `ready` deltaP `-1.1577` edge `0.0112` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9475` n `195` status `ready` deltaP `3.3111` edge `0.0317` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
