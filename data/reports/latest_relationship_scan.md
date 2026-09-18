# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T20:37:27.569960+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8194`

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

- `market_context_high->unknown_4h` score `37.8544` n `149` status `ready` deltaP `-0.9208` edge `3.184` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `36.1877` n `40` status `ready` deltaP `34.0278` edge `2.9267` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `35.7333` n `40` status `ready` deltaP `14.0972` edge `2.9997` maxDD `-6.6058`
- `risk_on_high->unknown_4h` score `11.7331` n `52` status `ready` deltaP `-8.1614` edge `1.0547` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.7331` n `52` status `ready` deltaP `-8.1614` edge `1.0547` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.5901` n `52` status `ready` deltaP `47.9167` edge `0.3964` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5901` n `52` status `ready` deltaP `47.9167` edge `0.3964` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2308` n `85` status `ready` deltaP `27.1503` edge `0.6175` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.291` n `149` status `ready` deltaP `41.2053` edge `0.3854` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `5.7168` n `40` status `ready` deltaP `22.0139` edge `0.4266` maxDD `-3.4232`
- `risk_on_high->commodity_4h` score `2.8453` n `52` status `ready` deltaP `32.9972` edge `0.0521` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8453` n `52` status `ready` deltaP `32.9972` edge `0.0521` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.745` n `149` status `ready` deltaP `29.4995` edge `0.0739` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `2.3105` n `85` status `ready` deltaP `17.977` edge `0.3461` maxDD `-10.9113`
- `news_risk_high->equity_4h` score `1.9156` n `85` status `ready` deltaP `17.344` edge `0.134` maxDD `-4.1995`
- `news_risk_high->metal_24h` score `1.5504` n `40` status `ready` deltaP `11.4583` edge `0.0811` maxDD `-0.2629`
- `market_context_high->commodity_1h` score `1.1517` n `149` status `ready` deltaP `16.5103` edge `0.0236` maxDD `-0.3491`
- `news_risk_high->crypto_alt_1h` score `1.059` n `85` status `ready` deltaP `11.8193` edge `0.1357` maxDD `-3.6312`
- `news_risk_high->equity_1h` score `1.057` n `85` status `ready` deltaP `13.1014` edge `0.0413` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `0.916` n `85` status `ready` deltaP `11.0707` edge `0.03` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
