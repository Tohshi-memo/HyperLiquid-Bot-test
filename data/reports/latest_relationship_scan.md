# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T11:16:06.494241+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11908`

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

- `risk_on_high->crypto_alt_24h` score `16.8681` n `91` status `ready` deltaP `34.0888` edge `1.2014` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.8681` n `91` status `ready` deltaP `34.0888` edge `1.2014` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `12.2794` n `201` status `ready` deltaP `25.653` edge `0.935` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.0231` n `91` status `ready` deltaP `40.269` edge `0.4373` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.0231` n `91` status `ready` deltaP `40.269` edge `0.4373` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.2938` n `91` status `ready` deltaP `30.0674` edge `0.4099` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.2938` n `91` status `ready` deltaP `30.0674` edge `0.4099` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.7286` n `91` status `ready` deltaP `22.9377` edge `0.9883` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.7286` n `91` status `ready` deltaP `22.9377` edge `0.9883` maxDD `-24.5429`
- `risk_on_high->index_24h` score `3.3531` n `91` status `ready` deltaP `34.8977` edge `0.051` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.3531` n `91` status `ready` deltaP `34.8977` edge `0.051` maxDD `-0.0051`
- `market_context_high->equity_24h` score `3.245` n `201` status `ready` deltaP `19.0972` edge `0.1431` maxDD `0.0`
- `market_context_high->index_24h` score `2.4813` n `201` status `ready` deltaP `29.2392` edge `0.0512` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.1202` n `91` status `ready` deltaP `26.9432` edge `0.0064` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.1202` n `91` status `ready` deltaP `26.9432` edge `0.0064` maxDD `-0.0802`
- `market_context_high->commodity_24h` score `1.8268` n `201` status `ready` deltaP `18.2784` edge `0.0443` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.8106` n `91` status `ready` deltaP `17.9449` edge `0.0406` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.8106` n `91` status `ready` deltaP `17.9449` edge `0.0406` maxDD `-0.0811`
- `risk_on_high->equity_24h` score `1.6394` n `91` status `ready` deltaP `19.0972` edge `0.0093` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6394` n `91` status `ready` deltaP `19.0972` edge `0.0093` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
