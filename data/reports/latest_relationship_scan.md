# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T18:37:31.670576+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8742`

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

- `market_context_high->unknown_4h` score `38.4684` n `90` status `ready` deltaP `-5.4474` edge `3.2959` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8577` n `62` status `ready` deltaP `37.9841` edge `0.6719` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.2941` n `62` status `ready` deltaP `23.2572` edge `0.5872` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.1928` n `62` status `ready` deltaP `9.6384` edge `0.2951` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.1332` n `62` status `ready` deltaP `29.5848` edge `0.1472` maxDD `0.0`
- `news_risk_high->index_4h` score `2.9524` n `62` status `ready` deltaP `32.6307` edge `0.0547` maxDD `-0.4296`
- `market_context_high->crypto_major_24h` score `2.9001` n `90` status `ready` deltaP `8.143` edge `0.6149` maxDD `-16.7906`
- `news_risk_high->crypto_major_1h` score `2.5415` n `62` status `ready` deltaP `10.4742` edge `0.1775` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3528` n `90` status `ready` deltaP `16.0486` edge `0.1855` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1813` n `62` status `ready` deltaP `18.5803` edge `0.1177` maxDD `-2.7837`
- `news_risk_high->index_1h` score `2.0032` n `62` status `ready` deltaP `25.1739` edge `0.0141` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.422` n `62` status `ready` deltaP `20.1735` edge `0.0894` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.3193` n `62` status `ready` deltaP `4.0564` edge `0.1348` maxDD `-2.4854`
- `news_risk_high->unknown_4h` score `1.248` n `62` status `ready` deltaP `-8.4224` edge `0.2847` maxDD `-5.6309`
- `market_context_high->fx_4h` score `0.8682` n `90` status `ready` deltaP `19.669` edge `0.0159` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.8475` n `90` status `ready` deltaP `19.0426` edge `0.1302` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.7525` n `90` status `ready` deltaP `12.5449` edge `0.0033` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1869` n `90` status `ready` deltaP `10.4025` edge `0.0435` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1197` n `62` status `ready` deltaP `6.6013` edge `0.0078` maxDD `-1.0132`
- `market_context_high->commodity_1h` score `-0.0072` n `90` status `ready` deltaP `4.3812` edge `0.0078` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
