# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T13:37:31.874540+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10963`

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

- `risk_on_high->unknown_4h` score `22.5308` n `140` status `ready` deltaP `4.2595` edge `1.911` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.5308` n `140` status `ready` deltaP `4.2595` edge `1.911` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `10.6609` n `228` status `ready` deltaP `5.5252` edge `0.9246` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.4435` n `37` status `ready` deltaP `25.1783` edge `0.4794` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9023` n `37` status `ready` deltaP `20.8333` edge `0.1863` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.6486` n `37` status `ready` deltaP `17.1803` edge `0.2308` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3113` n `37` status `ready` deltaP `23.3891` edge `0.0588` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.9288` n `37` status `ready` deltaP `11.7337` edge `0.1026` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5847` n `37` status `ready` deltaP `13.0847` edge `0.0839` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2215` n `37` status `ready` deltaP `14.5655` edge `0.024` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1535` n `37` status `ready` deltaP `6.1661` edge `0.0733` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1131` n `37` status `ready` deltaP `13.9748` edge `0.013` maxDD `-0.0724`
- `news_risk_high->crypto_major_24h` score `1.0218` n `37` status `ready` deltaP `16.5776` edge `0.2981` maxDD `-18.2098`
- `news_risk_high->crypto_alt_1h` score `0.9261` n `37` status `ready` deltaP `9.0266` edge `0.0435` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.6347` n `37` status `ready` deltaP `6.3983` edge `0.0431` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.5013` n `37` status `ready` deltaP `15.0947` edge `0.0427` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.2611` n `189` status `ready` deltaP `15.4266` edge `0.3652` maxDD `-20.7654`
- `risk_on_high->crypto_major_24h` score `0.102` n `117` status `ready` deltaP `19.5113` edge `0.7574` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.102` n `117` status `ready` deltaP `19.5113` edge `0.7574` maxDD `-56.9519`
- `risk_on_high->metal_1h` score `0.0627` n `151` status `ready` deltaP `11.29` edge `0.0012` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
