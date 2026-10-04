# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T17:22:24.850065+00:00`
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

- `market_context_high->unknown_1h` score `96.254` n `97` status `ready` deltaP `-0.6096` edge `8.0667` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.2804` n `97` status `ready` deltaP `2.2991` edge `6.5392` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.6411` n `65` status `ready` deltaP `37.887` edge `0.6545` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `9.5137` n `46` status `ready` deltaP `31.4915` edge `0.6481` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `9.4683` n `46` status `ready` deltaP `25.0529` edge `0.7493` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `7.6096` n `65` status `ready` deltaP `22.492` edge `0.4942` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.5148` n `65` status `ready` deltaP `24.8171` edge `0.5952` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `4.9745` n `97` status `ready` deltaP `21.868` edge `0.3391` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8657` n `65` status `ready` deltaP `26.7361` edge `0.1439` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8502` n `65` status `ready` deltaP `26.0647` edge `0.2081` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.2463` n `65` status `ready` deltaP `35.4198` edge `0.0606` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8705` n `65` status `ready` deltaP `12.4113` edge `0.192` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6768` n `65` status `ready` deltaP `23.3467` edge `0.109` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1944` n `65` status `ready` deltaP `26.9645` edge `0.0181` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.132` n `97` status `ready` deltaP `15.3297` edge `0.1205` maxDD `-2.2692`
- `market_context_high->crypto_alt_4h` score `1.628` n `97` status `ready` deltaP `6.6728` edge `0.2701` maxDD `-7.6465`
- `news_risk_high->crypto_alt_1h` score `1.6074` n `65` status `ready` deltaP `5.6172` edge `0.1484` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4336` n `97` status `ready` deltaP `25.4306` edge `0.0256` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3638` n `46` status `ready` deltaP `25.536` edge `0.1064` maxDD `-1.8102`
- `market_context_high->equity_24h` score `1.0683` n `46` status `ready` deltaP `2.5588` edge `0.1711` maxDD `-6.264`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
