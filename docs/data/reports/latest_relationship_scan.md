# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T14:37:27.901355+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5897`

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

- `market_context_high->unknown_24h` score `155.7402` n `40` status `ready` deltaP `30.3819` edge `12.7758` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.1719` n `40` status `ready` deltaP `50.7639` edge `0.6323` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.7843` n `40` status `ready` deltaP `51.1458` edge `0.5705` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.2502` n `31` status `ready` deltaP `-7.1253` edge `0.2201` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9809` n `31` status `ready` deltaP `20.4365` edge `0.0107` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9413` n `31` status `ready` deltaP `12.192` edge `0.0624` maxDD `-1.5526`
- `market_context_high->commodity_1h` score `0.379` n `47` status `ready` deltaP `8.0137` edge `0.0326` maxDD `-1.3282`
- `news_risk_high->commodity_4h` score `0.3592` n `31` status `ready` deltaP `14.1621` edge `-0.0144` maxDD `-1.6728`
- `market_context_high->commodity_4h` score `0.3107` n `47` status `ready` deltaP `5.0338` edge `0.0909` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.1789` n `31` status `ready` deltaP `-0.0639` edge `0.0534` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1383` n `31` status `ready` deltaP `4.8928` edge `0.0354` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.0143` n `31` status `ready` deltaP `3.3417` edge `-0.0043` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.024` n `47` status `ready` deltaP `6.6664` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->crypto_alt_1h` score `-0.0684` n `31` status `ready` deltaP `10.8412` edge `-0.017` maxDD `-3.1233`
- `market_context_high->fx_4h` score `-0.1509` n `47` status `ready` deltaP `11.8935` edge `-0.0062` maxDD `-1.8531`
- `news_risk_high->fx_1h` score `-0.235` n `31` status `ready` deltaP `-0.2656` edge `0.0028` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.572` n `31` status `ready` deltaP `-2.2117` edge `-0.001` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.6707` n `40` status `ready` deltaP `0.6597` edge `0.0377` maxDD `-2.506`
- `market_context_high->crypto_alt_4h` score `-0.7099` n `47` status `ready` deltaP `-0.1427` edge `0.0005` maxDD `-4.9116`
- `news_risk_high->crypto_major_1h` score `-0.8969` n `31` status `ready` deltaP `2.6608` edge `-0.0607` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
