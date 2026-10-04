# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T11:37:29.165259+00:00`
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

- `market_context_high->unknown_4h` score `148.8351` n `76` status `ready` deltaP `7.9028` edge `12.3646` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `121.9628` n `88` status `ready` deltaP `0.558` edge `10.2013` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `11.8385` n `46` status `ready` deltaP `29.0459` edge `0.9202` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `11.2804` n `46` status `ready` deltaP `35.4846` edge `0.7687` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.8101` n `65` status `ready` deltaP `38.6492` edge `0.6635` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `9.896` n `59` status `ready` deltaP `25.8592` edge `0.6623` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.2915` n `65` status `ready` deltaP `23.75` edge `0.5837` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.2886` n `76` status `ready` deltaP `25.2889` edge `0.4258` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.4419` n `59` status `ready` deltaP `29.5139` edge `0.1734` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.9118` n `65` status `ready` deltaP `26.8269` edge `0.2084` maxDD `-2.9013`
- `market_context_high->crypto_alt_4h` score `3.6475` n `76` status `ready` deltaP `12.1711` edge `0.3559` maxDD `-7.6465`
- `news_risk_high->index_4h` score `3.1404` n `65` status `ready` deltaP `34.2003` edge `0.0599` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9832` n `65` status `ready` deltaP `12.8604` edge `0.1984` maxDD `-1.5096`
- `market_context_high->equity_24h` score `2.9219` n `46` status `ready` deltaP `6.5519` edge `0.2995` maxDD `-6.3081`
- `market_context_high->crypto_major_1h` score `2.5065` n `88` status `ready` deltaP `17.1611` edge `0.1395` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5012` n `65` status `ready` deltaP `21.2125` edge `0.1086` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1094` n `65` status `ready` deltaP `25.9166` edge `0.018` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6218` n `65` status `ready` deltaP `5.3178` edge `0.1516` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3689` n `46` status `ready` deltaP `25.7096` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9863` n `88` status `ready` deltaP `15.2558` edge `0.0069` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
