# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T15:52:27.966121+00:00`
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

- `market_context_high->crypto_alt_24h` score `12.0943` n `39` status `ready` deltaP `52.2035` edge `0.6772` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.4509` n `39` status `ready` deltaP `53.6458` edge `0.5966` maxDD `0.0`
- `news_risk_high->equity_4h` score `1.088` n `31` status `ready` deltaP `-7.2777` edge `0.2076` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9498` n `31` status `ready` deltaP `19.9874` edge `0.0097` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9473` n `31` status `ready` deltaP `12.192` edge `0.0629` maxDD `-1.5526`
- `market_context_high->commodity_1h` score `0.3955` n `48` status `ready` deltaP `8.4955` edge `0.0315` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3583` n `46` status `ready` deltaP `5.3354` edge `0.095` maxDD `-2.7703`
- `news_risk_high->commodity_4h` score `0.2743` n `31` status `ready` deltaP `13.3999` edge `-0.0164` maxDD `-1.6728`
- `market_context_high->fx_1h` score `0.2207` n `48` status `ready` deltaP `9.0818` edge `-0.0074` maxDD `-0.7804`
- `news_risk_high->index_4h` score `0.145` n `31` status `ready` deltaP `-0.3688` edge `0.0526` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1383` n `31` status `ready` deltaP `4.8928` edge `0.0354` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.0555` n `31` status `ready` deltaP `2.7429` edge `-0.0056` maxDD `-0.5845`
- `market_context_high->fx_4h` score `-0.0634` n `46` status `ready` deltaP `12.9573` edge `-0.006` maxDD `-1.8531`
- `news_risk_high->crypto_alt_1h` score `-0.0988` n `31` status `ready` deltaP `10.3921` edge `-0.0179` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2684` n `31` status `ready` deltaP `-0.8644` edge `0.0025` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.5708` n `31` status `ready` deltaP `-2.2117` edge `-0.0009` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.5895` n `39` status `ready` deltaP `1.1084` edge `0.0399` maxDD `-2.3798`
- `news_risk_high->metal_4h` score `-0.9039` n `31` status `ready` deltaP `-3.9241` edge `-0.0146` maxDD `-0.7654`
- `news_risk_high->crypto_major_1h` score `-0.9491` n `31` status `ready` deltaP `2.062` edge `-0.0634` maxDD `-3.762`
- `news_risk_high->index_24h` score `-1.1625` n `31` status `ready` deltaP `7.4429` edge `-0.1062` maxDD `-3.7303`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
