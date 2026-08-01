# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T20:01:49.675970+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5189.3226` n `60` status `ready` deltaP `32.6747` edge `432.2678` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.4342` n `53` status `ready` deltaP `56.5776` edge `1.1154` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.4965` n `65` status `ready` deltaP `19.4114` edge `0.3925` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1438` n `65` status `ready` deltaP `18.954` edge `0.0763` maxDD `-0.2539`
- `market_context_high->commodity_24h` score `1.856` n `53` status `ready` deltaP `28.3509` edge `0.2348` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.6848` n `53` status `ready` deltaP `9.1953` edge `0.1222` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6744` n `68` status `ready` deltaP `9.3431` edge `0.0762` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.247` n `53` status `ready` deltaP `14.3207` edge `0.0158` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.2254` n `65` status `ready` deltaP `6.6463` edge `0.0322` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1435` n `68` status `ready` deltaP `6.7806` edge `0.0414` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `0.0835` n `65` status `ready` deltaP `11.9114` edge `0.0233` maxDD `-0.6604`
- `market_context_high->fx_1h` score `-0.0029` n `53` status `ready` deltaP `7.3523` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0668` n `68` status `ready` deltaP `2.316` edge `0.0083` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.1035` n `68` status `ready` deltaP `2.2191` edge `0.0042` maxDD `-0.2475`
- `market_context_high->commodity_1h` score `-0.1057` n `53` status `ready` deltaP `3.7284` edge `0.0157` maxDD `-1.3282`
- `market_context_high->fx_24h` score `-0.1178` n `53` status `ready` deltaP `6.1933` edge `0.0416` maxDD `-2.506`
- `news_risk_high->metal_1h` score `-0.1427` n `68` status `ready` deltaP `2.316` edge `0.0066` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1571` n `68` status `ready` deltaP `2.5185` edge `0.0351` maxDD `-3.762`
- `news_risk_high->crypto_major_4h` score `-0.2486` n `65` status `ready` deltaP `3.9704` edge `0.1016` maxDD `-9.7953`
- `market_context_high->commodity_4h` score `-0.2738` n `53` status `ready` deltaP `3.4198` edge `0.0296` maxDD `-3.0005`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
