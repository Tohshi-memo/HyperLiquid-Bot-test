# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T23:52:31.608151+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10512`

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

- `news_risk_high->unknown_4h` score `397.8764` n `78` status `ready` deltaP `-22.4554` edge `33.3954` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.7855` n `78` status `ready` deltaP `18.9236` edge `1.9393` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.3981` n `78` status `ready` deltaP `44.8184` edge `1.5235` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.8609` n `78` status `ready` deltaP `32.265` edge `1.2537` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.1112` n `78` status `ready` deltaP `43.7767` edge `1.0621` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7291` n `78` status `ready` deltaP `61.9391` edge `0.3321` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4457` n `78` status `ready` deltaP `37.7938` edge `0.3306` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9292` n `52` status `ready` deltaP `37.5` edge `0.2441` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9292` n `52` status `ready` deltaP `37.5` edge `0.2441` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9461` n `135` status `ready` deltaP `31.5741` edge `0.2443` maxDD `-0.7426`
- `risk_on_high->fx_24h` score `4.2971` n `52` status `ready` deltaP `48.4241` edge `0.0395` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.2971` n `52` status `ready` deltaP `48.4241` edge `0.0395` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.8965` n `135` status `ready` deltaP `45.162` edge `0.0452` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9841` n `52` status `ready` deltaP `25.8325` edge `0.0281` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9841` n `52` status `ready` deltaP `25.8325` edge `0.0281` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7844` n `137` status `ready` deltaP `21.2424` edge `0.0489` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7407` n `137` status `ready` deltaP `12.3629` edge `0.017` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7238` n `78` status `ready` deltaP `17.2686` edge `0.0405` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2252` n `52` status `ready` deltaP `6.7481` edge `0.009` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2252` n `52` status `ready` deltaP `6.7481` edge `0.009` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
