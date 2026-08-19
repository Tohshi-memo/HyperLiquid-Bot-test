# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T09:52:26.657375+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->crypto_major_24h` score `2.1958` n `96` status `ready` deltaP `7.4652` edge `0.254` maxDD `-4.9964`
- `market_context_high->equity_4h` score `1.7653` n `96` status `ready` deltaP `10.2388` edge `0.1677` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.6845` n `96` status `ready` deltaP `14.4025` edge `0.0745` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.3734` n `96` status `ready` deltaP `19.3089` edge `0.0433` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `1.1561` n `96` status `ready` deltaP `11.9156` edge `0.119` maxDD `-3.1677`
- `market_context_high->commodity_24h` score `0.9818` n `96` status `ready` deltaP `12.6736` edge `0.2247` maxDD `-4.666`
- `market_context_high->index_1h` score `0.939` n `96` status `ready` deltaP `16.0616` edge `0.0099` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.2192` n `96` status `ready` deltaP `8.3084` edge `-0.0144` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.2123` n `96` status `ready` deltaP `6.5681` edge `0.0126` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `0.212` n `96` status `ready` deltaP `9.9085` edge `0.0786` maxDD `-5.4926`
- `market_context_high->index_4h` score `0.0875` n `96` status `ready` deltaP `7.6473` edge `0.0218` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0692` n `96` status `ready` deltaP `8.1046` edge `0.0051` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `0.0157` n `96` status `ready` deltaP `16.1458` edge `-0.0557` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3518` n `96` status `ready` deltaP `-1.7715` edge `0.0026` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3674` n `96` status `ready` deltaP `2.9815` edge `0.0175` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4408` n `96` status `ready` deltaP `1.7777` edge `0.0118` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.5386` n `96` status `ready` deltaP `1.3466` edge `0.007` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9203` n `96` status `ready` deltaP `-8.1899` edge `-0.0068` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2035` n `96` status `ready` deltaP `-3.6458` edge `0.0726` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.1044` n `96` status `ready` deltaP `-23.9583` edge `-0.024` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
