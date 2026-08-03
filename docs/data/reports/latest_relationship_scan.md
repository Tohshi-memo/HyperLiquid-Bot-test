# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T17:22:25.579958+00:00`
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

- `market_context_high->unknown_24h` score `45.1062` n `39` status `ready` deltaP `30.3819` edge `3.5563` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.7842` n `39` status `ready` deltaP `51.1619` edge `0.6583` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.3129` n `39` status `ready` deltaP `53.6458` edge `0.5851` maxDD `0.0`
- `news_risk_high->fx_24h` score `0.9557` n `31` status `ready` deltaP `12.192` edge `0.0636` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9186` n `31` status `ready` deltaP `19.5383` edge `0.0087` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.8864` n `31` status `ready` deltaP `-7.2777` edge `0.1908` maxDD `-2.8064`
- `market_context_high->commodity_1h` score `0.4151` n `54` status `ready` deltaP `9.2038` edge `0.0293` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.285` n `46` status `ready` deltaP `4.4207` edge `0.0917` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.2804` n `54` status `ready` deltaP `9.5587` edge `-0.0056` maxDD `-0.7804`
- `news_risk_high->commodity_4h` score `0.1615` n `31` status `ready` deltaP `12.4852` edge `-0.0197` maxDD `-1.6728`
- `news_risk_high->fx_4h` score `0.1383` n `31` status `ready` deltaP `4.8928` edge `0.0354` maxDD `-0.356`
- `news_risk_high->index_4h` score `0.1354` n `31` status `ready` deltaP `-0.3688` edge `0.0518` maxDD `-0.3783`
- `market_context_high->fx_4h` score `-0.0634` n `46` status `ready` deltaP `12.9573` edge `-0.006` maxDD `-1.8531`
- `news_risk_high->index_1h` score `-0.0906` n `31` status `ready` deltaP `2.1441` edge `-0.0061` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.105` n `31` status `ready` deltaP `10.0927` edge `-0.0167` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2941` n `31` status `ready` deltaP `-1.3135` edge `0.0022` maxDD `-0.1588`
- `market_context_high->crypto_alt_1h` score `-0.4955` n `54` status `ready` deltaP `0.6543` edge `-0.001` maxDD `-3.0178`
- `market_context_high->fx_24h` score `-0.5811` n `39` status `ready` deltaP `1.1084` edge `0.0406` maxDD `-2.3798`
- `news_risk_high->metal_1h` score `-0.6032` n `31` status `ready` deltaP `-2.5111` edge `-0.0016` maxDD `-0.5538`
- `news_risk_high->metal_4h` score `-0.9319` n `31` status `ready` deltaP `-4.2289` edge `-0.0149` maxDD `-0.7654`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
