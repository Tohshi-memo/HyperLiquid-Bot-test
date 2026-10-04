# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T09:37:29.386825+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4964`

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

- `market_context_high->unknown_4h` score `187.095` n `68` status `ready` deltaP `8.4469` edge `15.5493` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `150.482` n `80` status `ready` deltaP `2.268` edge `12.5665` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `12.9228` n `46` status `ready` deltaP `30.4348` edge `1.0013` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `12.1199` n `46` status `ready` deltaP `36.8735` edge `0.8294` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `11.06` n `65` status `ready` deltaP `39.8687` edge `0.6762` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.5124` n `59` status `ready` deltaP `27.2481` edge `0.7044` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.4019` n `65` status `ready` deltaP `23.75` edge `0.5929` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.3632` n `68` status `ready` deltaP `24.0316` edge `0.4404` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.1935` n `68` status `ready` deltaP `20.2206` edge `0.4269` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6046` n `59` status `ready` deltaP `30.9028` edge `0.1777` maxDD `0.0`
- `news_risk_high->equity_4h` score `4.0103` n `65` status `ready` deltaP `27.894` edge `0.2095` maxDD `-2.9013`
- `market_context_high->equity_24h` score `3.5382` n `46` status `ready` deltaP `7.9408` edge `0.3416` maxDD `-6.3081`
- `news_risk_high->index_4h` score `3.2306` n `65` status `ready` deltaP `35.2674` edge `0.0603` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `3.0024` n `65` status `ready` deltaP `13.0101` edge `0.199` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.6841` n `80` status `ready` deltaP `18.1063` edge `0.148` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5024` n `65` status `ready` deltaP `21.2125` edge `0.1087` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.2064` n `65` status `ready` deltaP `27.1142` edge `0.0181` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `1.8481` n `80` status `ready` deltaP `11.4072` edge `0.1526` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.5739` n `65` status `ready` deltaP `4.8687` edge `0.1506` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.2928` n `46` status `ready` deltaP `24.3207` edge `0.1054` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
