# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T21:22:34.603114+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5931`

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

- `market_context_high->unknown_24h` score `44.3716` n `40` status `ready` deltaP `28.8194` edge `3.5055` maxDD `0.0`
- `market_context_high->unknown_4h` score `14.3987` n `58` status `ready` deltaP `9.7614` edge `1.1812` maxDD `-1.3777`
- `market_context_high->crypto_alt_24h` score `10.8274` n `40` status `ready` deltaP `48.5764` edge `0.5958` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `10.5288` n `40` status `ready` deltaP `50.9722` edge `0.5436` maxDD `-0.1479`
- `news_risk_high->fx_24h` score `1.0025` n `31` status `ready` deltaP `12.192` edge `0.0675` maxDD `-1.5526`
- `market_context_high->commodity_4h` score `0.9192` n `58` status `ready` deltaP `11.0597` edge `0.0875` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.896` n `31` status `ready` deltaP `19.2389` edge `0.0078` maxDD `-0.6947`
- `market_context_high->commodity_1h` score `0.3717` n `70` status `ready` deltaP `7.2113` edge `0.0245` maxDD `-1.3282`
- `news_risk_high->equity_4h` score `0.3675` n `31` status `ready` deltaP `-8.6497` edge `0.1567` maxDD `-2.8064`
- `market_context_high->fx_1h` score `0.3135` n `70` status `ready` deltaP `9.5509` edge `-0.0027` maxDD `-0.7878`
- `news_risk_high->fx_4h` score `0.1074` n `31` status `ready` deltaP `4.2831` edge `0.0355` maxDD `-0.356`
- `market_context_high->fx_4h` score `0.0878` n `58` status `ready` deltaP `14.0717` edge `-0.0005` maxDD `-1.8797`
- `news_risk_high->index_4h` score `-0.038` n `31` status `ready` deltaP `-1.7408` edge `0.0465` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `-0.0474` n `31` status `ready` deltaP `10.5035` edge `-0.0239` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.0898` n `31` status `ready` deltaP `2.1441` edge `-0.006` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1206` n `31` status `ready` deltaP `10.0927` edge `-0.0187` maxDD `-3.1233`
- `market_context_high->crypto_alt_4h` score `-0.1298` n `58` status `ready` deltaP `7.3539` edge `0.0249` maxDD `-4.9116`
- `market_context_high->crypto_alt_1h` score `-0.3294` n `70` status `ready` deltaP `1.6595` edge `0.0136` maxDD `-3.0178`
- `news_risk_high->fx_1h` score `-0.3338` n `31` status `ready` deltaP `-2.062` edge `0.0021` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.3609` n `70` status `ready` deltaP `3.0197` edge `-0.013` maxDD `-1.6054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
