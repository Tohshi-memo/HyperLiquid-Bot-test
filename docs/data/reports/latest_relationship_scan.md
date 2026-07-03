# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T06:52:25.222025+00:00`
- Price records: `672`
- Market context records: `5534`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11398`

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

- `market_context_high->equity_24h` score `4.0556` n `189` status `ready` deltaP `14.6495` edge `0.7482` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.5658` n `192` status `ready` deltaP `13.2241` edge `0.3549` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.3481` n `189` status `ready` deltaP `16.0797` edge `0.5425` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.9773` n `192` status `ready` deltaP `8.8287` edge `0.27` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.6842` n `192` status `ready` deltaP `9.5274` edge `0.2407` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5257` n `189` status `ready` deltaP `14.1948` edge `0.0419` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.2256` n `192` status `ready` deltaP `7.1888` edge `0.0674` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.019` n `192` status `ready` deltaP `5.1241` edge `0.0136` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2625` n `192` status `ready` deltaP `1.4066` edge `0.0649` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.352` n `192` status `ready` deltaP `3.1375` edge `0.0743` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3567` n `192` status `ready` deltaP `0.4429` edge `0.0002` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.6024` n `192` status `ready` deltaP `1.1134` edge `0.0099` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.8975` n `192` status `ready` deltaP `2.1469` edge `0.0043` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.299` n `192` status `ready` deltaP `3.8363` edge `0.0271` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7413` n `192` status `ready` deltaP `-5.6574` edge `-0.0126` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.9175` n `189` status `ready` deltaP `13.2523` edge `0.0645` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5662` n `192` status `ready` deltaP `-11.4838` edge `-0.0515` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7955` n `192` status `ready` deltaP `-10.747` edge `-0.0618` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.2031` n `189` status `ready` deltaP `7.0437` edge `0.2225` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3946` n `189` status `ready` deltaP `-4.5387` edge `-0.18` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
