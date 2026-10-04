# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T21:22:26.787180+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5012`

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

- `market_context_high->unknown_1h` score `97.3016` n `97` status `ready` deltaP `-0.1605` edge `8.151` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.707` n `97` status `ready` deltaP `2.7564` edge `6.5717` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.2846` n `65` status `ready` deltaP `35.9053` edge `0.638` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `8.3627` n `46` status `ready` deltaP `28.7137` edge `0.5707` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `7.7772` n `46` status `ready` deltaP `22.2751` edge `0.6269` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.3383` n `65` status `ready` deltaP `23.75` edge `0.5876` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.281` n `65` status `ready` deltaP `19.7143` edge `0.402` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.618` n `97` status `ready` deltaP `19.8863` edge `0.3226` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.7606` n `65` status `ready` deltaP `26.5625` edge `0.1363` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.6189` n `65` status `ready` deltaP `24.3879` edge `0.2` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1966` n `65` status `ready` deltaP `34.9625` edge `0.0595` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.771` n `65` status `ready` deltaP `11.5131` edge `0.1897` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5118` n `65` status `ready` deltaP `21.9747` edge `0.1044` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1824` n `65` status `ready` deltaP `26.8148` edge `0.0181` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.0325` n `97` status `ready` deltaP `14.4315` edge `0.1182` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5978` n `65` status `ready` deltaP `5.6172` edge `0.1476` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.4515` n `97` status `ready` deltaP `5.6057` edge `0.2625` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.4238` n `97` status `ready` deltaP `25.2782` edge `0.0258` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3685` n `46` status `ready` deltaP `25.536` edge `0.107` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.924` n `97` status `ready` deltaP `14.5672` edge `0.0063` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
