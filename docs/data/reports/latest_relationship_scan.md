# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T15:48:27.207825+00:00`
- Price records: `672`
- Market context records: `2676`
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

- `market_context_high->crypto_alt_24h` score `9.0557` n `111` status `ready` deltaP `16.0051` edge `0.9973` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6443` n `111` status `ready` deltaP `17.652` edge `0.6355` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `2.9387` n `130` status `ready` deltaP `20.4011` edge `0.374` maxDD `-15.2094`
- `market_context_high->unknown_4h` score `1.3622` n `130` status `ready` deltaP `7.228` edge `0.1703` maxDD `-3.7312`
- `market_context_high->crypto_major_4h` score `0.2831` n `130` status `ready` deltaP `8.4334` edge `0.2142` maxDD `-14.3965`
- `market_context_high->index_4h` score `0.0496` n `130` status `ready` deltaP `9.5708` edge `0.0267` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1508` n `138` status `ready` deltaP `3.0548` edge `0.0097` maxDD `-1.2855`
- `market_context_high->fx_24h` score `-0.2115` n `111` status `ready` deltaP `10.2994` edge `0.0009` maxDD `-0.6418`
- `market_context_high->index_24h` score `-0.4098` n `111` status `ready` deltaP `6.2735` edge `0.0221` maxDD `-2.5127`
- `market_context_high->commodity_1h` score `-0.4526` n `138` status `ready` deltaP `1.9222` edge `0.0045` maxDD `-4.3601`
- `market_context_high->commodity_24h` score `-0.5062` n `111` status `ready` deltaP `7.9627` edge `0.1914` maxDD `-12.4171`
- `market_context_high->fx_1h` score `-0.5165` n `138` status `ready` deltaP `-0.371` edge `0.0038` maxDD `-0.2164`
- `market_context_high->fx_4h` score `-0.5463` n `130` status `ready` deltaP `1.1023` edge `0.0125` maxDD `-0.5631`
- `market_context_high->unknown_1h` score `-0.6412` n `138` status `ready` deltaP `1.5274` edge `0.0092` maxDD `-3.1587`
- `market_context_high->crypto_alt_1h` score `-0.6702` n `138` status `ready` deltaP `6.372` edge `0.0476` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7238` n `138` status `ready` deltaP `-1.4493` edge `-0.0008` maxDD `-2.9203`
- `market_context_high->crypto_major_1h` score `-1.0685` n `138` status `ready` deltaP `3.1741` edge `0.0288` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.2576` n `130` status `ready` deltaP `3.4029` edge `0.0081` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2757` n `138` status `ready` deltaP `-4.9574` edge `0.0106` maxDD `-2.7085`
- `market_context_high->crypto_major_24h` score `-1.3205` n `111` status `ready` deltaP `5.9967` edge `0.547` maxDD `-44.169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
