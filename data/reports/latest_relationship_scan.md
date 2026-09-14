# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T13:52:40.971629+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11232`

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

- `news_risk_high->unknown_4h` score `388.9239` n `79` status `ready` deltaP `-19.9869` edge `32.6329` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.3513` n `79` status `ready` deltaP `45.1037` edge `1.5177` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.4893` n `79` status `ready` deltaP `34.9046` edge `1.3718` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.7054` n `79` status `ready` deltaP `37.3792` edge `0.9876` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5925` n `79` status `ready` deltaP `61.5967` edge `0.323` maxDD `-0.075`
- `market_context_high->commodity_24h` score `7.1587` n `101` status `ready` deltaP `40.1042` edge `0.3292` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.1577` n `79` status `ready` deltaP `36.7133` edge `0.3138` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1375` n `41` status `ready` deltaP `40.1042` edge `0.2441` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1375` n `41` status `ready` deltaP `40.1042` edge `0.2441` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.8563` n `41` status `ready` deltaP `54.6791` edge `0.0444` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.8563` n `41` status `ready` deltaP `54.6791` edge `0.0444` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.4665` n `101` status `ready` deltaP `51.1775` edge `0.0526` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9849` n `52` status `ready` deltaP `26.4423` edge `0.0241` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9849` n `52` status `ready` deltaP `26.4423` edge `0.0241` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7852` n `137` status `ready` deltaP `21.8522` edge `0.0449` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6999` n `137` status `ready` deltaP `12.0635` edge `0.0156` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6437` n `79` status `ready` deltaP `15.79` edge `0.0401` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2709` n `137` status `ready` deltaP `11.0735` edge `0.0085` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.1845` n `52` status `ready` deltaP `6.4487` edge `0.0076` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1845` n `52` status `ready` deltaP `6.4487` edge `0.0076` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
