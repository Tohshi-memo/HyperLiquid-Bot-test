# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T05:52:28.160198+00:00`
- Price records: `672`
- Market context records: `5530`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11432`

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

- `market_context_high->equity_24h` score `3.9512` n `189` status `ready` deltaP `14.6495` edge `0.7395` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.6683` n `192` status `ready` deltaP `13.6814` edge `0.3604` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.5281` n `189` status `ready` deltaP `16.0797` edge `0.5575` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `2.0415` n `192` status `ready` deltaP `9.286` edge `0.2723` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.7712` n `192` status `ready` deltaP `9.9848` edge `0.2449` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.4672` n `189` status `ready` deltaP `13.674` edge `0.0405` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.2088` n `192` status `ready` deltaP `7.1888` edge `0.066` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0202` n `192` status `ready` deltaP `5.1241` edge `0.0135` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.3117` n `192` status `ready` deltaP `1.4066` edge `0.0608` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3863` n `192` status `ready` deltaP `-0.0062` edge `-0.0006` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4383` n `192` status `ready` deltaP `2.8381` edge `0.0691` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6587` n `192` status `ready` deltaP `0.6643` edge `0.0082` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.9425` n `192` status `ready` deltaP `1.6896` edge `0.0036` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.2118` n `192` status `ready` deltaP `4.4461` edge `0.0303` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6957` n `192` status `ready` deltaP `-5.2083` edge `-0.0118` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8549` n `189` status `ready` deltaP `13.9468` edge `0.0679` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.6545` n `192` status `ready` deltaP `-12.0935` edge `-0.0548` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7179` n `192` status `ready` deltaP `-10.1372` edge `-0.0594` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.1443` n `189` status `ready` deltaP `7.0437` edge `0.2274` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3829` n `189` status `ready` deltaP `-4.5387` edge `-0.1785` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
