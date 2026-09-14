# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T22:52:25.952616+00:00`
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

- `news_risk_high->unknown_4h` score `397.6556` n `78` status `ready` deltaP `-22.4554` edge `33.377` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.9427` n `78` status `ready` deltaP `18.9236` edge `1.9524` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.5387` n `78` status `ready` deltaP `45.1656` edge `1.5329` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.0349` n `78` status `ready` deltaP `32.265` edge `1.2682` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.0263` n `78` status `ready` deltaP `43.2559` edge `1.0585` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7315` n `78` status `ready` deltaP `61.9391` edge `0.3323` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4433` n `78` status `ready` deltaP `37.7938` edge `0.3304` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.8616` n `52` status `ready` deltaP `36.8056` edge `0.2431` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8616` n `52` status `ready` deltaP `36.8056` edge `0.2431` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.5468` n `131` status `ready` deltaP `33.7522` edge `0.2589` maxDD `-0.4011`
- `risk_on_high->fx_24h` score `4.3635` n `52` status `ready` deltaP `49.1186` edge `0.0404` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.3635` n `52` status `ready` deltaP `49.1186` edge `0.0404` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.955` n `131` status `ready` deltaP `45.6982` edge `0.0465` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0497` n `52` status `ready` deltaP `26.4423` edge `0.0295` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0497` n `52` status `ready` deltaP `26.4423` edge `0.0295` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.85` n `137` status `ready` deltaP `21.8522` edge `0.0503` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.755` n `137` status `ready` deltaP `12.5126` edge `0.0172` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.693` n `78` status `ready` deltaP `16.8113` edge `0.0396` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2396` n `52` status `ready` deltaP `6.8978` edge `0.0092` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2396` n `52` status `ready` deltaP `6.8978` edge `0.0092` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
