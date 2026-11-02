# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T03:52:34.334784+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8064`

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

- `market_context_high->unknown_24h` score `7296.0511` n `45` status `ready` deltaP `1.3889` edge `607.995` maxDD `0.0`
- `market_context_high->unknown_4h` score `435.7161` n `47` status `ready` deltaP `9.1463` edge `36.2487` maxDD `0.0`
- `market_context_high->unknown_1h` score `58.9989` n `50` status `ready` deltaP `5.4192` edge `4.8915` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.4597` n `45` status `ready` deltaP `42.3959` edge `1.3626` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.763` n `94` status `ready` deltaP `33.7396` edge `1.0576` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.7334` n `45` status `ready` deltaP `45.0` edge `0.2922` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.565` n `47` status `ready` deltaP `28.2466` edge `0.3882` maxDD `-1.6876`
- `market_context_high->index_24h` score `6.3522` n `45` status `ready` deltaP `49.1319` edge `0.2018` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.3741` n `47` status `ready` deltaP `29.3202` edge `0.286` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.6608` n `47` status `ready` deltaP `3.9407` edge `0.349` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3455` n `47` status `ready` deltaP `32.5214` edge `0.082` maxDD `-0.6017`
- `news_risk_high->crypto_alt_4h` score `2.2554` n `126` status `ready` deltaP `9.0132` edge `0.2665` maxDD `-7.4246`
- `market_context_high->equity_1h` score `2.2505` n `50` status `ready` deltaP `7.4012` edge `0.1907` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.8909` n `50` status `ready` deltaP `5.8503` edge `0.1798` maxDD `-2.2314`
- `market_context_high->crypto_major_1h` score `1.725` n `50` status `ready` deltaP `7.2515` edge `0.1463` maxDD `-1.4048`
- `market_context_high->metal_4h` score `1.4244` n `47` status `ready` deltaP `17.0375` edge `0.0476` maxDD `-0.7323`
- `market_context_high->crypto_alt_24h` score `1.3188` n `45` status `ready` deltaP `-7.9862` edge `0.3741` maxDD `-8.8096`
- `market_context_high->fx_1h` score `1.2603` n `50` status `ready` deltaP `17.1018` edge `0.0086` maxDD `-0.0736`
- `market_context_high->crypto_major_24h` score `1.1361` n `45` status `ready` deltaP `2.7778` edge `0.1948` maxDD `-3.0799`
- `market_context_high->metal_1h` score `0.6882` n `50` status `ready` deltaP `9.8922` edge `0.0171` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
