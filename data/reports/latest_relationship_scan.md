# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T18:07:31.554805+00:00`
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

- `market_context_high->unknown_24h` score `45.8147` n `39` status `ready` deltaP `30.2083` edge `3.6165` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.5793` n `39` status `ready` deltaP `50.641` edge `0.6447` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.2589` n `39` status `ready` deltaP `53.6458` edge `0.5806` maxDD `0.0`
- `news_risk_high->fx_24h` score `0.9617` n `31` status `ready` deltaP `12.192` edge `0.0641` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9178` n `31` status `ready` deltaP `19.5383` edge `0.0086` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.7844` n `31` status `ready` deltaP `-7.2777` edge `0.1823` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.3368` n `57` status `ready` deltaP `7.9368` edge `0.0277` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.2503` n `46` status `ready` deltaP `3.9634` edge `0.0903` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.1988` n `57` status `ready` deltaP `8.4935` edge `-0.0053` maxDD `-0.7804`
- `news_risk_high->fx_4h` score `0.1296` n `31` status `ready` deltaP `4.7404` edge `0.0353` maxDD `-0.356`
- `news_risk_high->index_4h` score `0.1258` n `31` status `ready` deltaP `-0.3688` edge `0.051` maxDD `-0.3783`
- `news_risk_high->commodity_4h` score `0.1081` n `31` status `ready` deltaP `12.0279` edge `-0.0211` maxDD `-1.6728`
- `market_context_high->fx_4h` score `-0.0768` n `46` status `ready` deltaP `12.8049` edge `-0.0061` maxDD `-1.8531`
- `news_risk_high->index_1h` score `-0.0929` n `31` status `ready` deltaP `2.1441` edge `-0.0064` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1463` n `31` status `ready` deltaP `9.6436` edge `-0.019` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2778` n `31` status `ready` deltaP `-1.0141` edge `0.0023` maxDD `-0.1588`
- `market_context_high->crypto_alt_1h` score `-0.3403` n `57` status `ready` deltaP `2.7393` edge `0.005` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.4869` n `57` status `ready` deltaP `1.6914` edge `-0.0203` maxDD `-1.6054`
- `market_context_high->fx_24h` score `-0.5751` n `39` status `ready` deltaP `1.1084` edge `0.0411` maxDD `-2.3798`
- `news_risk_high->metal_1h` score `-0.6163` n `31` status `ready` deltaP `-2.6608` edge `-0.0017` maxDD `-0.5538`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
