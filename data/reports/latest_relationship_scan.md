# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T00:37:22.318981+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10829`

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

- `market_context_high->equity_4h` score `2.1523` n `96` status `ready` deltaP `11.6107` edge `0.1908` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7457` n `96` status `ready` deltaP `14.2528` edge `0.0806` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9486` n `96` status `ready` deltaP `16.0616` edge `0.0107` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3656` n `96` status `ready` deltaP `11.9918` edge `0.0081` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2834` n `96` status `ready` deltaP `9.7815` edge `0.0239` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1716` n `96` status `ready` deltaP `6.4236` edge `0.1625` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0098` n `96` status `ready` deltaP `7.0376` edge `0.0046` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0789` n `96` status `ready` deltaP `4.0232` edge `0.0053` maxDD `-0.4291`
- `market_context_high->unknown_1h` score `-0.1872` n `96` status `ready` deltaP `5.9132` edge `-0.0323` maxDD `-0.4843`
- `market_context_high->unknown_24h` score `-0.3021` n `96` status `ready` deltaP `17.7083` edge `-0.0926` maxDD `-1.0505`
- `market_context_high->fx_1h` score `-0.3463` n `96` status `ready` deltaP `-1.6218` edge `0.0023` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.7176` n `96` status `ready` deltaP `-1.8546` edge `0.0054` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8282` n `96` status `ready` deltaP `-0.1684` edge `-0.0249` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9265` n `96` status `ready` deltaP `1.3348` edge `-0.0432` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9414` n `96` status `ready` deltaP `-8.639` edge `-0.0065` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.1462` n `96` status `ready` deltaP `3.2012` edge `-0.0732` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.4667` n `96` status `ready` deltaP `5.3607` edge `-0.1392` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.155` n `96` status `ready` deltaP `-15.4514` edge `-0.0016` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-3.5412` n `96` status `ready` deltaP `-11.8056` edge `-0.0445` maxDD `-11.4635`
- `market_context_high->index_24h` score `-3.7896` n `96` status `ready` deltaP `-0.8681` edge `-0.0633` maxDD `-18.3411`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
