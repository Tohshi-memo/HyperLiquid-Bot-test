# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T10:07:35.259444+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5903`

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

- `market_context_high->crypto_alt_24h` score `12.4047` n `40` status `ready` deltaP `51.4583` edge `0.7304` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.8707` n `40` status `ready` deltaP `51.1458` edge `0.5777` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.8064` n `31` status `ready` deltaP `-6.668` edge `0.2634` maxDD `-2.8064`
- `news_risk_high->fx_24h` score `0.9293` n `31` status `ready` deltaP `12.192` edge `0.0614` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9116` n `31` status `ready` deltaP `19.3886` edge `0.0088` maxDD `-0.6947`
- `news_risk_high->index_4h` score `0.3209` n `31` status `ready` deltaP `0.2409` edge `0.0632` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `0.3167` n `31` status `ready` deltaP `13.7047` edge `-0.0149` maxDD `-1.6728`
- `market_context_high->commodity_1h` score `0.3097` n `47` status `ready` deltaP `6.9658` edge `0.0307` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.283` n `47` status `ready` deltaP `4.5764` edge `0.0904` maxDD `-2.7703`
- `news_risk_high->fx_4h` score `0.1612` n `31` status `ready` deltaP `5.1977` edge `0.0363` maxDD `-0.356`
- `news_risk_high->crypto_alt_1h` score `0.1257` n `31` status `ready` deltaP `12.3382` edge `-0.0021` maxDD `-3.1233`
- `news_risk_high->index_1h` score `0.0379` n `31` status `ready` deltaP `3.9405` edge `-0.0016` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.0334` n `47` status `ready` deltaP `6.5167` edge `-0.0088` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.1157` n `47` status `ready` deltaP `12.1984` edge `-0.0053` maxDD `-1.8531`
- `market_context_high->crypto_alt_4h` score `-0.2132` n `47` status `ready` deltaP `2.4487` edge `0.0469` maxDD `-4.9116`
- `news_risk_high->fx_1h` score `-0.2443` n `31` status `ready` deltaP `-0.4153` edge `0.0026` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.5996` n `31` status `ready` deltaP `-2.3614` edge `-0.0023` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.6827` n `40` status `ready` deltaP `0.6597` edge `0.0367` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.7231` n `31` status `ready` deltaP `3.8584` edge `-0.0464` maxDD `-3.762`
- `news_risk_high->equity_1h` score `-0.951` n `31` status `ready` deltaP `-9.7112` edge `0.0251` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
