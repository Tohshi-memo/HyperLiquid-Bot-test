# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T18:07:30.320363+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5058`

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

- `market_context_high->unknown_1h` score `96.4868` n `97` status `ready` deltaP `-0.6096` edge `8.0861` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.432` n `97` status `ready` deltaP `2.604` edge `6.5498` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.6205` n `65` status `ready` deltaP `37.7345` edge `0.6538` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `9.3485` n `46` status `ready` deltaP `30.9707` edge `0.6378` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `9.2082` n `46` status `ready` deltaP `24.532` edge `0.7311` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.556` n `65` status `ready` deltaP `25.122` edge `0.5966` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `7.3723` n `65` status `ready` deltaP `21.9712` edge `0.4779` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.9539` n `97` status `ready` deltaP `21.7155` edge `0.3384` maxDD `-3.294`
- `news_risk_high->equity_4h` score `3.8526` n `65` status `ready` deltaP `26.0647` edge `0.2083` maxDD `-2.881`
- `news_risk_high->index_24h` score `3.8513` n `65` status `ready` deltaP `26.7361` edge `0.1427` maxDD `0.0`
- `news_risk_high->index_4h` score `3.2853` n `65` status `ready` deltaP `35.8771` edge `0.0608` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8909` n `65` status `ready` deltaP `12.4113` edge `0.1937` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6768` n `65` status `ready` deltaP `23.3467` edge `0.109` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.2196` n `65` status `ready` deltaP `27.2639` edge `0.0182` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.1524` n `97` status `ready` deltaP `15.3297` edge `0.1222` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.6745` n `65` status `ready` deltaP `6.0663` edge `0.151` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.6692` n `97` status `ready` deltaP `6.9777` edge `0.2715` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.4068` n `97` status `ready` deltaP `25.1257` edge `0.0254` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3638` n `46` status `ready` deltaP `25.536` edge `0.1064` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9384` n `97` status `ready` deltaP `14.7169` edge `0.0065` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
