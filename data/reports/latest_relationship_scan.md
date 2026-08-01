# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T20:22:29.537428+00:00`
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

- `news_risk_high->unknown_24h` score `5189.2163` n `60` status `ready` deltaP `32.5014` edge `432.2601` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.4793` n `53` status `ready` deltaP `56.7509` edge `1.118` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `5.2655` n `66` status `ready` deltaP `18.4682` edge `0.3837` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9929` n `66` status `ready` deltaP `18.0109` edge `0.0747` maxDD `-0.2957`
- `market_context_high->commodity_24h` score `1.8345` n `53` status `ready` deltaP `28.1776` edge `0.2332` maxDD `-10.2019`
- `market_context_high->crypto_alt_4h` score `0.6942` n `53` status `ready` deltaP `9.1953` edge `0.1234` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6876` n `68` status `ready` deltaP `9.4928` edge `0.0763` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.247` n `53` status `ready` deltaP `14.3207` edge `0.0158` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.2436` n `66` status `ready` deltaP `7.1` edge `0.0315` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `0.1389` n `66` status `ready` deltaP `12.634` edge `0.0231` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `0.131` n `68` status `ready` deltaP `6.6309` edge `0.0408` maxDD `-3.1233`
- `market_context_high->fx_1h` score `-0.0029` n `53` status `ready` deltaP `7.3523` edge `0.001` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.059` n `68` status `ready` deltaP `2.4657` edge `0.0083` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.1035` n `68` status `ready` deltaP `2.2191` edge `0.0042` maxDD `-0.2475`
- `market_context_high->fx_24h` score `-0.1072` n `53` status `ready` deltaP `6.3666` edge `0.0418` maxDD `-2.506`
- `market_context_high->commodity_1h` score `-0.115` n `53` status `ready` deltaP `3.5787` edge `0.0155` maxDD `-1.3282`
- `news_risk_high->metal_1h` score `-0.1341` n `68` status `ready` deltaP `2.4657` edge `0.0067` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1695` n `68` status `ready` deltaP `2.3688` edge `0.0345` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.2833` n `53` status `ready` deltaP `3.2674` edge `0.0294` maxDD `-3.0005`
- `news_risk_high->crypto_major_4h` score `-0.5375` n `66` status `ready` deltaP `3.2012` edge `0.0867` maxDD `-10.8232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
