# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T22:07:28.664170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9520`

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

- `market_context_high->unknown_4h` score `45.4296` n `46` status `ready` deltaP `6.5549` edge `3.7421` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6077` n `46` status `ready` deltaP `13.1869` edge `2.395` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2109` n `46` status `ready` deltaP `12.1453` edge `1.28` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.5698` n `46` status `ready` deltaP `10.9375` edge `1.0579` maxDD `0.0`
- `market_context_high->index_24h` score `5.5059` n `46` status `ready` deltaP `19.6105` edge `0.3368` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.0144` n `96` status `ready` deltaP `37.6736` edge `0.2846` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.9141` n `96` status `ready` deltaP `-9.5486` edge `1.159` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `2.8977` n `96` status `ready` deltaP `14.1768` edge `0.2047` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.6567` n `96` status `ready` deltaP `10.2134` edge `0.2531` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.9637` n `97` status `ready` deltaP `11.0702` edge `0.1294` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8206` n `46` status `ready` deltaP `21.7921` edge `0.0198` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.4452` n `97` status `ready` deltaP `13.166` edge `0.072` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3134` n `96` status `ready` deltaP `19.7917` edge `0.0411` maxDD `-0.421`
- `market_context_high->metal_24h` score `0.7859` n `46` status `ready` deltaP `20.5314` edge `-0.048` maxDD `-0.2042`
- `news_risk_high->fx_24h` score `0.6952` n `96` status `ready` deltaP `21.7014` edge `0.1034` maxDD `-1.7159`
- `news_risk_high->metal_1h` score `0.6888` n `97` status `ready` deltaP `15.8297` edge `0.0112` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.683` n `46` status `ready` deltaP `6.1638` edge `0.0401` maxDD `-0.2751`
- `news_risk_high->crypto_alt_24h` score `0.6789` n `96` status `ready` deltaP `-8.8542` edge `0.6037` maxDD `-32.7147`
- `market_context_high->index_1h` score `0.6315` n `46` status `ready` deltaP `10.2057` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->metal_24h` score `0.3418` n `96` status `ready` deltaP `17.3611` edge `0.0125` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
