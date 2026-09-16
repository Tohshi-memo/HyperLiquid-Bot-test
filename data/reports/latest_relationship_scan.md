# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T18:07:31.400517+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11689`

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

- `news_risk_high->unknown_4h` score `366.091` n `83` status `ready` deltaP `-21.0531` edge `30.7374` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `20.426` n `81` status `ready` deltaP `44.5409` edge `1.514` maxDD `-7.0349`
- `news_risk_high->crypto_major_24h` score `18.5682` n `81` status `ready` deltaP `36.7863` edge `1.4851` maxDD `-11.9724`
- `news_risk_high->equity_24h` score `13.9413` n `81` status `ready` deltaP `45.0424` edge `1.0389` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.2497` n `81` status `ready` deltaP `50.4823` edge `0.2852` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `5.9535` n `52` status `ready` deltaP `36.9792` edge `0.2496` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9535` n `52` status `ready` deltaP `36.9792` edge `0.2496` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.7573` n `81` status `ready` deltaP `34.5293` edge `0.295` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.6544` n `149` status `ready` deltaP `30.2678` edge `0.2386` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3897` n `52` status `ready` deltaP `31.9311` edge `-0.0095` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3897` n `52` status `ready` deltaP `31.9311` edge `-0.0095` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.2988` n `52` status `ready` deltaP `28.8813` edge `0.034` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2988` n `52` status `ready` deltaP `28.8813` edge `0.034` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.2548` n `149` status `ready` deltaP `29.1562` edge `0.0151` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.1985` n `149` status `ready` deltaP `25.3836` edge `0.0558` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9` n `149` status `ready` deltaP `14.1151` edge `0.0186` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.3936` n `52` status `ready` deltaP `9.6975` edge `0.1473` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.3936` n `52` status `ready` deltaP `9.6975` edge `0.1473` maxDD `-6.2526`
- `news_risk_high->index_4h` score `0.3733` n `83` status `ready` deltaP `12.1933` edge `0.0294` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2768` n `52` status `ready` deltaP `7.1972` edge `0.0103` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
