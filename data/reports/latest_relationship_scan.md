# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T07:38:40.590074+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8284`

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

- `market_context_high->unknown_4h` score `39.8404` n `149` status `ready` deltaP `-0.0061` edge `3.3434` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7191` n `52` status `ready` deltaP `-7.2467` edge `1.2141` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7191` n `52` status `ready` deltaP `-7.2467` edge `1.2141` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8876` n `52` status `ready` deltaP `50.0` edge `0.4073` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8876` n `52` status `ready` deltaP `50.0` edge `0.4073` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5885` n `149` status `ready` deltaP `43.2886` edge `0.3963` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8751` n `52` status `ready` deltaP `32.8447` edge `0.0556` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8751` n `52` status `ready` deltaP `32.8447` edge `0.0556` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7748` n `149` status `ready` deltaP `29.347` edge `0.0774` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.7487` n `74` status `ready` deltaP `17.4852` edge `0.4509` maxDD `-12.8718`
- `market_context_high->commodity_1h` score `1.2236` n `149` status `ready` deltaP `17.1091` edge `0.0256` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `1.173` n `52` status `ready` deltaP `20.4727` edge `-0.0345` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.173` n `52` status `ready` deltaP `20.4727` edge `-0.0345` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.0381` n `149` status `ready` deltaP `17.6978` edge `-0.0099` maxDD `-0.0593`
- `news_risk_high->equity_4h` score `0.9098` n `74` status `ready` deltaP `12.7101` edge `0.1156` maxDD `-3.3619`
- `risk_on_high->commodity_1h` score `0.6003` n `52` status `ready` deltaP `10.1912` edge `0.0173` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6003` n `52` status `ready` deltaP `10.1912` edge `0.0173` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.4514` n `86` status `ready` deltaP `12.2615` edge `0.0283` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.1495` n `74` status `ready` deltaP `6.0646` edge `0.0234` maxDD `-0.2398`
- `news_risk_high->index_1h` score `0.0306` n `86` status `ready` deltaP `4.9506` edge `0.0011` maxDD `-0.5244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
