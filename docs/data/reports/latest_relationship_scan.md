# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T04:22:26.614853+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `51.7227` n `51` status `ready` deltaP `17.0139` edge `4.1968` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3959` n `51` status `ready` deltaP `40.237` edge `1.0245` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9545` n `51` status `ready` deltaP `23.4965` edge `0.9275` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.8252` n `51` status `ready` deltaP `48.9481` edge `0.1743` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.3287` n `51` status `ready` deltaP `25.2511` edge `0.1861` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.2407` n `51` status `ready` deltaP `15.8858` edge `0.1946` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2115` n `51` status `ready` deltaP `37.778` edge `0.0292` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.1988` n `145` status `ready` deltaP `21.3194` edge `0.0548` maxDD `-0.0956`
- `news_risk_high->metal_24h` score `1.993` n `51` status `ready` deltaP `36.4073` edge `-0.0724` maxDD `-0.0053`
- `news_risk_high->crypto_alt_24h` score `1.8289` n `51` status `ready` deltaP `26.0417` edge `-0.0212` maxDD `0.0`
- `news_risk_high->fx_1h` score `1.2446` n `51` status `ready` deltaP `16.9954` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8945` n `51` status `ready` deltaP `17.7439` edge `0.0328` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8147` n `51` status `ready` deltaP `12.6345` edge `0.0234` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.618` n `157` status `ready` deltaP `9.3291` edge `0.0342` maxDD `-1.5916`
- `news_risk_high->index_1h` score `0.2317` n `51` status `ready` deltaP `9.1229` edge `0.0042` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2195` n `51` status `ready` deltaP `8.8382` edge `-0.0098` maxDD `-0.4666`
- `market_context_high->fx_24h` score `0.0031` n `92` status `ready` deltaP `10.2129` edge `0.0132` maxDD `-1.4708`
- `news_risk_high->metal_4h` score `-0.0525` n `51` status `ready` deltaP `8.435` edge `-0.0075` maxDD `-0.249`
- `market_context_high->commodity_24h` score `-0.0725` n `92` status `ready` deltaP `-4.3101` edge `0.0807` maxDD `-1.9009`
- `news_risk_high->metal_1h` score `-0.1302` n `51` status `ready` deltaP `1.8933` edge `-0.007` maxDD `-0.1184`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
