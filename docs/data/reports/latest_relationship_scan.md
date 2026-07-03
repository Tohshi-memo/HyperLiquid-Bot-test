# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T07:07:25.542615+00:00`
- Price records: `672`
- Market context records: `5535`
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

- `market_context_high->equity_24h` score `4.0736` n `189` status `ready` deltaP `14.6495` edge `0.7497` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.5164` n `192` status `ready` deltaP `13.0716` edge `0.3518` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.2821` n `189` status `ready` deltaP `16.0797` edge `0.537` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.9399` n `192` status `ready` deltaP `8.6763` edge `0.2679` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.6576` n `192` status `ready` deltaP `9.375` edge `0.2395` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5444` n `189` status `ready` deltaP `14.3684` edge `0.0423` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.24` n `192` status `ready` deltaP `7.3385` edge `0.0676` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0202` n `192` status `ready` deltaP `5.1241` edge `0.0135` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2601` n `192` status `ready` deltaP `1.4066` edge `0.0651` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.334` n `192` status `ready` deltaP `3.2872` edge `0.0748` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3473` n `192` status `ready` deltaP `0.5926` edge `0.0004` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.6167` n `192` status `ready` deltaP `0.9637` edge `0.0097` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.8829` n `192` status `ready` deltaP `2.2993` edge `0.0045` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.322` n `192` status `ready` deltaP `3.6839` edge `0.0262` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7437` n `192` status `ready` deltaP `-5.6574` edge `-0.0128` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.9351` n `189` status `ready` deltaP `13.0787` edge `0.0634` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5602` n `192` status `ready` deltaP `-11.4838` edge `-0.051` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.8136` n `192` status `ready` deltaP `-10.8994` edge `-0.0623` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.2379` n `189` status `ready` deltaP `7.0437` edge `0.2196` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4024` n `189` status `ready` deltaP `-4.5387` edge `-0.181` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
