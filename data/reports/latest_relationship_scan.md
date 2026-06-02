# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T06:52:25.543353+00:00`
- Price records: `672`
- Market context records: `2638`
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

- `market_context_high->unknown_24h` score `7.5551` n `138` status `ready` deltaP `18.0178` edge `0.5423` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0829` n `138` status `ready` deltaP `24.5957` edge `0.5275` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.435` n `138` status `ready` deltaP `13.9581` edge `0.3742` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `2.5143` n `138` status `ready` deltaP `5.7367` edge `0.7243` maxDD `-34.9082`
- `market_context_high->index_24h` score `1.2386` n `138` status `ready` deltaP `11.564` edge `0.1242` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.1428` n `138` status `ready` deltaP `10.2708` edge `0.1455` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.053` n `138` status `ready` deltaP `6.9039` edge `0.1467` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.5985` n `138` status `ready` deltaP `7.4981` edge `0.1193` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.4656` n `138` status `ready` deltaP `10.5669` edge `0.0525` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0663` n `138` status `ready` deltaP `3.378` edge `0.0261` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.2157` n `138` status `ready` deltaP `3.0786` edge `0.0109` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.3697` n `138` status `ready` deltaP `3.6961` edge `0.0291` maxDD `-2.7641`
- `market_context_high->commodity_1h` score `-0.3819` n `138` status `ready` deltaP `5.5216` edge `0.0192` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5238` n `138` status `ready` deltaP `-0.3471` edge `0.0033` maxDD `-0.2373`
- `market_context_high->metal_1h` score `-0.6352` n `138` status `ready` deltaP `0.5988` edge `0.007` maxDD `-2.114`
- `market_context_high->fx_24h` score `-0.8237` n `138` status `ready` deltaP `3.7515` edge `-0.0018` maxDD `-1.0146`
- `market_context_high->fx_4h` score `-0.9461` n `138` status `ready` deltaP `-0.9522` edge `0.0106` maxDD `-0.6474`
- `market_context_high->commodity_4h` score `-0.9806` n `138` status `ready` deltaP `4.8074` edge `0.0365` maxDD `-10.2078`
- `market_context_high->equity_1h` score `-1.0305` n `138` status `ready` deltaP `-2.3583` edge `0.0137` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-1.2794` n `138` status `ready` deltaP `2.6445` edge `0.0162` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
