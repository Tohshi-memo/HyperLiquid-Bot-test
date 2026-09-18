# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T04:22:30.364681+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8616`

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

- `market_context_high->unknown_4h` score `39.2104` n `149` status `ready` deltaP `-0.0061` edge `3.2909` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.0891` n `52` status `ready` deltaP `-7.2467` edge `1.1616` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.0891` n `52` status `ready` deltaP `-7.2467` edge `1.1616` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.968` n `52` status `ready` deltaP `50.0` edge `0.414` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.968` n `52` status `ready` deltaP `50.0` edge `0.414` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6689` n `149` status `ready` deltaP `43.2886` edge `0.403` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `3.8553` n `33` status `ready` deltaP `23.8479` edge `0.3002` maxDD `-9.3661`
- `news_risk_high->unknown_1h` score `3.1876` n `78` status `ready` deltaP `2.2148` edge `0.2753` maxDD `-0.9543`
- `risk_on_high->commodity_4h` score `2.9667` n `52` status `ready` deltaP `33.1496` edge `0.0612` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9667` n `52` status `ready` deltaP `33.1496` edge `0.0612` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8664` n `149` status `ready` deltaP `29.6519` edge `0.083` maxDD `-0.345`
- `news_risk_high->index_24h` score `2.3871` n `33` status `ready` deltaP `18.2292` edge `0.095` maxDD `-0.075`
- `risk_on_high->fx_24h` score `1.4268` n `52` status `ready` deltaP `22.7297` edge `-0.0284` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.4268` n `52` status `ready` deltaP `22.7297` edge `-0.0284` maxDD `-0.0054`
- `news_risk_high->crypto_alt_4h` score `1.3642` n `68` status `ready` deltaP `13.6837` edge `0.3093` maxDD `-13.05`
- `market_context_high->fx_24h` score `1.2919` n `149` status `ready` deltaP `19.9548` edge `-0.0038` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2463` n `149` status `ready` deltaP `17.2588` edge `0.0265` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6231` n `52` status `ready` deltaP `10.3409` edge `0.0182` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6231` n `52` status `ready` deltaP `10.3409` edge `0.0182` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.4845` n `68` status `ready` deltaP `9.7292` edge `0.0592` maxDD `-3.3619`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
