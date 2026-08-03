# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T17:52:28.921587+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5913`

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

- `market_context_high->unknown_24h` score `45.843` n `39` status `ready` deltaP `30.3819` edge `3.6177` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.6484` n `39` status `ready` deltaP `50.8146` edge `0.6493` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.2757` n `39` status `ready` deltaP `53.6458` edge `0.582` maxDD `0.0`
- `news_risk_high->fx_24h` score `0.9605` n `31` status `ready` deltaP `12.192` edge `0.064` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9178` n `31` status `ready` deltaP `19.5383` edge `0.0086` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.8168` n `31` status `ready` deltaP `-7.2777` edge `0.185` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.3998` n `56` status `ready` deltaP `8.9393` edge `0.0291` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.272` n `56` status `ready` deltaP `9.3777` edge `-0.0051` maxDD `-0.7804`
- `market_context_high->commodity_4h` score `0.2606` n `46` status `ready` deltaP `4.1159` edge `0.0906` maxDD `-2.7703`
- `news_risk_high->fx_4h` score `0.1376` n `31` status `ready` deltaP `4.8928` edge `0.0353` maxDD `-0.356`
- `news_risk_high->index_4h` score `0.1294` n `31` status `ready` deltaP `-0.3688` edge `0.0513` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `0.1239` n `31` status `ready` deltaP `12.1804` edge `-0.0208` maxDD `-1.6728`
- `market_context_high->fx_4h` score `-0.0646` n `46` status `ready` deltaP `12.9573` edge `-0.0061` maxDD `-1.8531`
- `news_risk_high->index_1h` score `-0.0921` n `31` status `ready` deltaP `2.1441` edge `-0.0063` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1322` n `31` status `ready` deltaP `9.7933` edge `-0.0182` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2856` n `31` status `ready` deltaP `-1.1638` edge `0.0023` maxDD `-0.1588`
- `market_context_high->crypto_alt_1h` score `-0.3936` n `56` status `ready` deltaP `2.0744` edge `0.0026` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.5503` n `56` status `ready` deltaP `0.8768` edge `-0.023` maxDD `-1.6054`
- `market_context_high->fx_24h` score `-0.5763` n `39` status `ready` deltaP `1.1084` edge `0.041` maxDD `-2.3798`
- `news_risk_high->metal_1h` score `-0.6032` n `31` status `ready` deltaP `-2.5111` edge `-0.0016` maxDD `-0.5538`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
