# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T15:52:31.651546+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4470`

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

- `market_context_high->unknown_1h` score `30242.4618` n `48` status `ready` deltaP `-0.3868` edge `2520.2239` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `20707.9008` n `48` status `ready` deltaP `3.7601` edge `1725.6472` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1271.8186` n `31` status `ready` deltaP `3.5783` edge `105.9786` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1096.4578` n `31` status `ready` deltaP `4.701` edge `91.3458` maxDD `-0.119`
- `news_risk_high->equity_24h` score `43.3997` n `31` status `ready` deltaP `47.9167` edge `3.2972` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.4281` n `31` status `ready` deltaP `48.6111` edge `2.7116` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.302` n `31` status `ready` deltaP `48.7847` edge `2.3666` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.0319` n `31` status `ready` deltaP `48.7008` edge `0.7888` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.8862` n `31` status `ready` deltaP `21.8823` edge `0.765` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.4531` n `31` status `ready` deltaP `31.7369` edge `0.6244` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.7748` n `31` status `ready` deltaP `46.1806` edge `0.2567` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.1021` n `31` status `ready` deltaP `51.2601` edge `0.1796` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.8886` n `31` status `ready` deltaP `11.2903` edge `0.8214` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2061` n `31` status `ready` deltaP `18.0413` edge `0.1656` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.1255` n `31` status `ready` deltaP `33.5661` edge `0.0627` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.6781` n `48` status `ready` deltaP `32.5711` edge `0.0345` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5452` n `31` status `ready` deltaP `30.3458` edge `0.0183` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.1507` n `31` status `ready` deltaP `8.9627` edge `0.2621` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8171` n `31` status `ready` deltaP `7.9148` edge `0.2159` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.462` n `31` status `ready` deltaP `28.5348` edge `0.0251` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
