# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T06:37:28.413973+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10647`

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

- `news_risk_high->crypto_alt_24h` score `8.5382` n `30` status `ready` deltaP `35.9028` edge `0.4766` maxDD `-0.0214`
- `news_risk_high->crypto_major_24h` score `5.968` n `30` status `ready` deltaP `24.0277` edge `0.4408` maxDD `-6.6257`
- `news_risk_high->crypto_major_4h` score `5.4401` n `30` status `ready` deltaP `28.435` edge `0.2839` maxDD `-0.6101`
- `news_risk_high->commodity_24h` score `4.0147` n `30` status `ready` deltaP `20.1389` edge `0.2003` maxDD `0.0`
- `news_risk_high->commodity_4h` score `2.7622` n `30` status `ready` deltaP `16.8902` edge `0.1335` maxDD `-0.2737`
- `news_risk_high->metal_4h` score `2.5021` n `30` status `ready` deltaP `23.9431` edge `0.071` maxDD `-0.7692`
- `risk_on_high->crypto_major_24h` score `2.2096` n `92` status `ready` deltaP `13.7379` edge `0.9243` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `2.2096` n `92` status `ready` deltaP `13.7379` edge `0.9243` maxDD `-47.9416`
- `news_risk_high->fx_24h` score `2.1122` n `30` status `ready` deltaP `30.6945` edge `0.0419` maxDD `-2.9744`
- `news_risk_high->index_1h` score `1.4692` n `30` status `ready` deltaP `17.1557` edge `0.0173` maxDD `-0.0724`
- `market_context_high->equity_24h` score `1.3276` n `175` status `ready` deltaP `13.2103` edge `0.3764` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.2398` n `30` status `ready` deltaP `6.1477` edge `0.1014` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `0.7561` n `30` status `ready` deltaP `8.1637` edge `0.0279` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.5147` n `30` status `ready` deltaP `-0.5589` edge `0.0649` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.1806` n `30` status `ready` deltaP `3.8623` edge `0.0158` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.1486` n `30` status `ready` deltaP `2.3171` edge `0.0298` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `0.0409` n `30` status `ready` deltaP `6.7465` edge `0.0049` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1363` n `145` status `ready` deltaP `8.0487` edge `0.0001` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
