# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T08:07:27.570400+00:00`
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

- `market_context_high->unknown_4h` score `39.8284` n `149` status `ready` deltaP `-0.0061` edge `3.3424` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7071` n `52` status `ready` deltaP `-7.2467` edge `1.2131` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7071` n `52` status `ready` deltaP `-7.2467` edge `1.2131` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.884` n `52` status `ready` deltaP `50.0` edge `0.407` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.884` n `52` status `ready` deltaP `50.0` edge `0.407` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5849` n `149` status `ready` deltaP `43.2886` edge `0.396` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8679` n `52` status `ready` deltaP `32.8447` edge `0.055` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8679` n `52` status `ready` deltaP `32.8447` edge `0.055` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7676` n `149` status `ready` deltaP `29.347` edge `0.0768` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.6989` n `76` status `ready` deltaP `17.8915` edge `0.4418` maxDD `-12.8718`
- `market_context_high->commodity_1h` score `1.2236` n `149` status `ready` deltaP `17.1091` edge `0.0256` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `1.132` n `52` status `ready` deltaP `20.1255` edge `-0.0356` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.132` n `52` status `ready` deltaP `20.1255` edge `-0.0356` maxDD `-0.0054`
- `news_risk_high->equity_4h` score `1.0144` n `76` status `ready` deltaP `13.4468` edge `0.1241` maxDD `-3.3619`
- `market_context_high->fx_24h` score `0.9972` n `149` status `ready` deltaP `17.3506` edge `-0.011` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.6003` n `52` status `ready` deltaP `10.1912` edge `0.0173` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6003` n `52` status `ready` deltaP `10.1912` edge `0.0173` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.425` n `88` status `ready` deltaP `11.874` edge `0.0275` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.1807` n `76` status `ready` deltaP `6.7555` edge `0.0228` maxDD `-0.2398`
- `news_risk_high->index_1h` score `0.0927` n `88` status `ready` deltaP `5.6818` edge `0.0014` maxDD `-0.5244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
