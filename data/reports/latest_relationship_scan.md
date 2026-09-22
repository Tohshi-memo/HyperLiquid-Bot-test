# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T19:07:30.129653+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_4h` score `46.257` n `46` status `ready` deltaP `7.0122` edge `3.808` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5403` n `46` status `ready` deltaP `12.8397` edge `2.3917` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2848` n `46` status `ready` deltaP `12.3189` edge `1.285` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.2567` n `46` status `ready` deltaP `11.9792` edge `1.1082` maxDD `0.0`
- `market_context_high->index_24h` score `5.5637` n `46` status `ready` deltaP `19.9578` edge `0.3393` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.3695` n `96` status `ready` deltaP `39.7569` edge `0.3003` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.8468` n `96` status `ready` deltaP `-9.8958` edge `1.1557` maxDD `-46.1999`
- `news_risk_high->crypto_alt_4h` score `3.0706` n `96` status `ready` deltaP `12.0427` edge `0.2754` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `3.0683` n `96` status `ready` deltaP `15.2439` edge `0.2118` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.2834` n `96` status `ready` deltaP `12.8805` edge `0.1398` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.868` n `46` status `ready` deltaP `22.2494` edge `0.0207` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6009` n `96` status `ready` deltaP `14.2278` edge `0.0779` maxDD `-1.8141`
- `news_risk_high->crypto_alt_24h` score `1.3658` n `96` status `ready` deltaP `-7.8125` edge `0.654` maxDD `-32.7147`
- `news_risk_high->fx_4h` score `1.1832` n `96` status `ready` deltaP `18.4197` edge `0.0394` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.1026` n `46` status `ready` deltaP `22.6148` edge `-0.0355` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.7298` n `46` status `ready` deltaP `6.6129` edge `0.041` maxDD `-0.2751`
- `news_risk_high->metal_1h` score `0.6245` n `96` status `ready` deltaP `15.0262` edge `0.0112` maxDD `-0.7468`
- `market_context_high->index_1h` score `0.6171` n `46` status `ready` deltaP `10.056` edge `0.0097` maxDD `-0.0249`
- `news_risk_high->metal_24h` score `0.5476` n `96` status `ready` deltaP `19.4445` edge `0.025` maxDD `-2.4203`
- `news_risk_high->fx_24h` score `0.526` n `96` status `ready` deltaP `19.6181` edge `0.0956` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
