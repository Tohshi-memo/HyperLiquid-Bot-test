# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T07:37:26.507064+00:00`
- Price records: `672`
- Market context records: `5537`
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

- `market_context_high->equity_24h` score `4.0932` n `190` status `ready` deltaP `14.7442` edge `0.7507` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.4092` n `192` status `ready` deltaP `12.7668` edge `0.3449` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.316` n `190` status `ready` deltaP `16.2189` edge `0.5389` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.8543` n `192` status `ready` deltaP `8.3714` edge `0.2628` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.596` n `192` status `ready` deltaP `9.0701` edge `0.2364` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5084` n `190` status `ready` deltaP `14.3201` edge `0.0418` maxDD `-1.2585`
- `market_context_high->equity_1h` score `0.2232` n `192` status `ready` deltaP `7.1888` edge `0.0672` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0573` n `192` status `ready` deltaP `4.8247` edge `0.0124` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2829` n `192` status `ready` deltaP `1.2569` edge `0.0642` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3302` n `192` status `ready` deltaP `0.892` edge `0.0006` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.3616` n `192` status `ready` deltaP `3.1375` edge `0.0735` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6311` n `192` status `ready` deltaP `0.814` edge `0.0095` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.8502` n `192` status `ready` deltaP `2.6042` edge `0.0052` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.3692` n `192` status `ready` deltaP `3.379` edge `0.0243` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7473` n `192` status `ready` deltaP `-5.6574` edge `-0.0131` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.9529` n `190` status `ready` deltaP `12.8874` edge `0.0624` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5384` n `192` status `ready` deltaP `-11.3313` edge `-0.0502` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.8416` n `192` status `ready` deltaP `-11.2043` edge `-0.0626` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.1762` n `190` status `ready` deltaP `7.2442` edge `0.2234` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3477` n `190` status `ready` deltaP `-4.2379` edge `-0.176` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
