# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T18:22:36.567827+00:00`
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

- `market_context_high->unknown_24h` score `45.7888` n `39` status `ready` deltaP `30.0347` edge `3.6155` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.5103` n `39` status `ready` deltaP `50.4674` edge `0.6401` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.2421` n `39` status `ready` deltaP `53.6458` edge `0.5792` maxDD `0.0`
- `news_risk_high->fx_24h` score `0.9641` n `31` status `ready` deltaP `12.192` edge `0.0643` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9093` n `31` status `ready` deltaP `19.3886` edge `0.0085` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.7604` n `31` status `ready` deltaP `-7.2777` edge `0.1803` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.3644` n `58` status `ready` deltaP `8.5433` edge `0.0272` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.2401` n `46` status `ready` deltaP `3.811` edge `0.09` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.1285` n `58` status `ready` deltaP `7.6451` edge `-0.0055` maxDD `-0.7804`
- `news_risk_high->index_4h` score `0.1222` n `31` status `ready` deltaP `-0.3688` edge `0.0507` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1217` n `31` status `ready` deltaP `4.5879` edge `0.0353` maxDD `-0.356`
- `news_risk_high->commodity_4h` score `0.0923` n `31` status `ready` deltaP `11.8755` edge `-0.0214` maxDD `-1.6728`
- `market_context_high->fx_4h` score `-0.089` n `46` status `ready` deltaP `12.6524` edge `-0.0061` maxDD `-1.8531`
- `news_risk_high->index_1h` score `-0.0921` n `31` status `ready` deltaP `2.1441` edge `-0.0063` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.1587` n `31` status `ready` deltaP `9.4939` edge `-0.0196` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2692` n `31` status `ready` deltaP `-0.8644` edge `0.0024` maxDD `-0.1588`
- `market_context_high->crypto_alt_1h` score `-0.2713` n `58` status `ready` deltaP `3.376` edge `0.0096` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.4343` n `58` status `ready` deltaP `2.4778` edge `-0.0188` maxDD `-1.6054`
- `market_context_high->fx_24h` score `-0.5727` n `39` status `ready` deltaP `1.1084` edge `0.0413` maxDD `-2.3798`
- `news_risk_high->metal_1h` score `-0.6163` n `31` status `ready` deltaP `-2.6608` edge `-0.0017` maxDD `-0.5538`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
