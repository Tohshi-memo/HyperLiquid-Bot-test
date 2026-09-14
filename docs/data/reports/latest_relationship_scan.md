# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T16:07:35.697070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11022`

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

- `news_risk_high->unknown_4h` score `395.197` n `78` status `ready` deltaP `-21.3883` edge `33.165` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.7379` n `78` status `ready` deltaP `46.3809` edge `1.5414` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.3872` n `78` status `ready` deltaP `34.3483` edge `1.367` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.0177` n `78` status `ready` deltaP `38.5684` edge `1.0057` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6768` n `78` status `ready` deltaP `61.7655` edge `0.3289` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.0015` n `110` status `ready` deltaP `38.8889` edge `0.3242` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.3341` n `78` status `ready` deltaP `37.7938` edge `0.3213` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.2407` n `50` status `ready` deltaP `38.8889` edge `0.2608` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2407` n `50` status `ready` deltaP `38.8889` edge `0.2608` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.7892` n `50` status `ready` deltaP `53.5556` edge `0.0463` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.7892` n `50` status `ready` deltaP `53.5556` edge `0.0463` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.366` n `110` status `ready` deltaP `50.1011` edge `0.0514` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9229` n `52` status `ready` deltaP `25.8325` edge `0.023` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9229` n `52` status `ready` deltaP `25.8325` edge `0.023` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7232` n `137` status `ready` deltaP `21.2424` edge `0.0438` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7574` n `137` status `ready` deltaP `12.6623` edge `0.0164` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6532` n `78` status `ready` deltaP `15.8966` edge `0.0406` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.242` n `52` status `ready` deltaP `7.0475` edge `0.0084` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.242` n `52` status `ready` deltaP `7.0475` edge `0.0084` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2194` n `137` status `ready` deltaP `10.1589` edge `0.008` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
