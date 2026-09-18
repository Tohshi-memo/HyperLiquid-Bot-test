# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T20:52:38.281187+00:00`
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

- `market_context_high->unknown_4h` score `37.81` n `149` status `ready` deltaP `-0.9208` edge `3.1803` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `36.0617` n `40` status `ready` deltaP `34.0278` edge `2.9162` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `35.5658` n `40` status `ready` deltaP `13.9236` edge `2.9869` maxDD `-6.6058`
- `risk_on_high->unknown_4h` score `11.6887` n `52` status `ready` deltaP `-8.1614` edge `1.051` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.6887` n `52` status `ready` deltaP `-8.1614` edge `1.051` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.5877` n `52` status `ready` deltaP `47.9167` edge `0.3962` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5877` n `52` status `ready` deltaP `47.9167` edge `0.3962` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.1874` n `85` status `ready` deltaP `26.9978` edge `0.6149` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.2886` n `149` status `ready` deltaP `41.2053` edge `0.3852` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `5.6717` n `40` status `ready` deltaP `21.8403` edge `0.424` maxDD `-3.4232`
- `risk_on_high->commodity_4h` score `2.8441` n `52` status `ready` deltaP `32.9972` edge `0.052` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8441` n `52` status `ready` deltaP `32.9972` edge `0.052` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7438` n `149` status `ready` deltaP `29.4995` edge `0.0738` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `2.287` n `85` status `ready` deltaP `17.8246` edge `0.3441` maxDD `-10.9113`
- `news_risk_high->equity_4h` score `1.9012` n `85` status `ready` deltaP `17.344` edge `0.1328` maxDD `-4.1995`
- `news_risk_high->metal_24h` score `1.5432` n `40` status `ready` deltaP `11.4583` edge `0.0805` maxDD `-0.2629`
- `market_context_high->commodity_1h` score `1.1505` n `149` status `ready` deltaP `16.5103` edge `0.0235` maxDD `-0.3491`
- `news_risk_high->crypto_alt_1h` score `1.0559` n `85` status `ready` deltaP `11.8193` edge `0.1353` maxDD `-3.6312`
- `news_risk_high->equity_1h` score `1.0415` n `85` status `ready` deltaP `12.9517` edge `0.041` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `0.9026` n `85` status `ready` deltaP `10.9182` edge `0.0299` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
