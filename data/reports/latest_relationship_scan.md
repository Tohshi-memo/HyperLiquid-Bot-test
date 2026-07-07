# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T06:07:26.611217+00:00`
- Price records: `672`
- Market context records: `5953`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11184`

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

- `news_risk_high->fx_24h` score `6.9005` n `30` status `ready` deltaP `63.0208` edge `0.1549` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.456` n `30` status `ready` deltaP `39.2709` edge `0.2134` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.832` n `30` status `ready` deltaP `39.6951` edge `0.0593` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0945` n `30` status `ready` deltaP `25.2794` edge `0.0199` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5872` n `222` status `ready` deltaP `10.2917` edge `0.1731` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.9104` n `30` status `ready` deltaP `10.9381` edge `0.0905` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2808` n `30` status `ready` deltaP `6.0679` edge `0.0417` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1937` n `30` status `ready` deltaP `6.9791` edge `0.0158` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3285` n `30` status `ready` deltaP `2.8842` edge `-0.0247` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.3667` n `234` status `ready` deltaP `4.8045` edge `0.0338` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5037` n `234` status `ready` deltaP `2.115` edge `0.0012` maxDD `-2.0564`
- `market_context_high->index_1h` score `-0.649` n `234` status `ready` deltaP `0.5771` edge `0.0043` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-0.6506` n `213` status `ready` deltaP `19.9213` edge `0.2914` maxDD `-31.2762`
- `market_context_high->commodity_1h` score `-0.6561` n `234` status `ready` deltaP `-3.8244` edge `-0.0029` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.7066` n `234` status `ready` deltaP `-1.0454` edge `-0.0008` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.0742` n `30` status `ready` deltaP `-9.8503` edge `-0.0206` maxDD `-1.1161`
- `market_context_high->crypto_alt_1h` score `-1.1267` n `234` status `ready` deltaP `1.9653` edge `0.0177` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-1.1289` n `234` status `ready` deltaP `1.8783` edge `0.0195` maxDD `-9.807`
- `market_context_high->metal_4h` score `-1.5363` n `222` status `ready` deltaP `-1.5793` edge `-0.0232` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.6867` n `222` status `ready` deltaP `1.1508` edge `0.0205` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
