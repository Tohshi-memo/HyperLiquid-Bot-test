# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T19:52:30.407379+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8314`

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

- `market_context_high->unknown_4h` score `38.3368` n `149` status `ready` deltaP `-0.9208` edge `3.2242` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `34.5379` n `38` status `ready` deltaP `33.3699` edge `2.7936` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `21.9407` n `38` status `ready` deltaP `12.6919` edge `2.8442` maxDD `-6.6058`
- `risk_on_high->unknown_4h` score `12.2155` n `52` status `ready` deltaP `-8.1614` edge `1.0949` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `12.2155` n `52` status `ready` deltaP `-8.1614` edge `1.0949` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.5985` n `52` status `ready` deltaP `47.9167` edge `0.3971` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5985` n `52` status `ready` deltaP `47.9167` edge `0.3971` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.3298` n `85` status `ready` deltaP `27.6076` edge `0.6227` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.2994` n `149` status `ready` deltaP `41.2053` edge `0.3861` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `5.1861` n `38` status `ready` deltaP `20.8242` edge `0.3903` maxDD `-3.4232`
- `risk_on_high->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7426` n `149` status `ready` deltaP `29.4995` edge `0.0737` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `2.3686` n `85` status `ready` deltaP `18.4343` edge `0.3505` maxDD `-10.9113`
- `news_risk_high->equity_4h` score `2.0014` n `85` status `ready` deltaP `17.8013` edge `0.1381` maxDD `-4.1995`
- `news_risk_high->metal_24h` score `1.2497` n `38` status `ready` deltaP `9.4846` edge `0.0692` maxDD `-0.2629`
- `market_context_high->commodity_1h` score `1.1792` n `149` status `ready` deltaP `16.8097` edge `0.0239` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `1.1134` n `85` status `ready` deltaP `13.5505` edge `0.043` maxDD `-0.9112`
- `news_risk_high->crypto_alt_1h` score `1.0489` n `85` status `ready` deltaP `11.8193` edge `0.1344` maxDD `-3.6312`
- `news_risk_high->fx_4h` score `0.955` n `85` status `ready` deltaP `11.528` edge `0.0302` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
