# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T07:22:24.782874+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10695`

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

- `news_risk_high->crypto_alt_24h` score `8.3976` n `30` status `ready` deltaP `35.5556` edge `0.4672` maxDD `-0.0214`
- `news_risk_high->crypto_major_24h` score `5.6803` n `30` status `ready` deltaP `23.5069` edge `0.4203` maxDD `-6.6257`
- `news_risk_high->crypto_major_4h` score `5.3903` n `30` status `ready` deltaP `27.9777` edge `0.2828` maxDD `-0.6101`
- `news_risk_high->commodity_24h` score `4.0255` n `30` status `ready` deltaP `20.1389` edge `0.2012` maxDD `0.0`
- `news_risk_high->commodity_4h` score `2.7232` n `30` status `ready` deltaP `16.4329` edge `0.1333` maxDD `-0.2737`
- `news_risk_high->metal_4h` score `2.4765` n `30` status `ready` deltaP `23.6382` edge `0.0709` maxDD `-0.7692`
- `risk_on_high->crypto_major_24h` score `2.3384` n `95` status `ready` deltaP `14.3841` edge `0.9365` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `2.3384` n `95` status `ready` deltaP `14.3841` edge `0.9365` maxDD `-47.9416`
- `news_risk_high->fx_24h` score `2.1086` n `30` status `ready` deltaP `30.6945` edge `0.0416` maxDD `-2.9744`
- `news_risk_high->index_1h` score `1.4692` n `30` status `ready` deltaP `17.1557` edge `0.0173` maxDD `-0.0724`
- `news_risk_high->equity_1h` score `1.2146` n `30` status `ready` deltaP `5.8483` edge `0.1013` maxDD `-0.7924`
- `market_context_high->equity_24h` score `1.2077` n `178` status `ready` deltaP `13.017` edge `0.3677` maxDD `-16.9737`
- `news_risk_high->metal_1h` score `0.7801` n `30` status `ready` deltaP `8.4631` edge `0.0279` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.5207` n `30` status `ready` deltaP `-0.5589` edge `0.0654` maxDD `-0.4628`
- `news_risk_high->crypto_alt_4h` score `0.1994` n `30` status `ready` deltaP `2.622` edge `0.032` maxDD `-1.296`
- `news_risk_high->crypto_alt_1h` score `0.1854` n `30` status `ready` deltaP `3.8623` edge `0.0162` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `0.0402` n `30` status `ready` deltaP `6.7465` edge `0.0048` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1208` n `145` status `ready` deltaP `8.3481` edge `0.0001` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
