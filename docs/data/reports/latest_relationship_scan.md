# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T00:22:30.681669+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.2454` n `47` status `ready` deltaP `10.5651` edge `5.9571` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `35.3802` n `46` status `ready` deltaP `22.3883` edge `2.8147` maxDD `-0.5817`
- `market_context_high->equity_24h` score `20.5564` n `46` status `ready` deltaP `19.7841` edge `1.5912` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `19.2773` n `46` status `ready` deltaP `17.3611` edge `1.4907` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `9.7241` n `97` status `ready` deltaP `-1.099` edge `1.5035` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.9177` n `46` status `ready` deltaP `28.8119` edge `0.3931` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `5.3866` n `97` status `ready` deltaP `-3.2575` edge `0.9587` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.8973` n `103` status `ready` deltaP `14.5365` edge `0.411` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.597` n `103` status `ready` deltaP `17.4328` edge `0.3246` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.5845` n `103` status `ready` deltaP `13.6068` edge `0.1737` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.4454` n `47` status `ready` deltaP `28.8434` edge `0.0269` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.4203` n `97` status `ready` deltaP `24.0424` edge `0.1593` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.0025` n `103` status `ready` deltaP `15.5529` edge `0.1067` maxDD `-1.8141`
- `market_context_high->metal_24h` score `1.804` n `46` status `ready` deltaP `22.7884` edge `0.0218` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.6112` n `103` status `ready` deltaP `23.5289` edge `0.041` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.3551` n `47` status `ready` deltaP `10.8945` edge `0.0821` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.1094` n `97` status `ready` deltaP `27.6221` edge `0.1212` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `0.8346` n `97` status `ready` deltaP `18.8663` edge `0.073` maxDD `-3.0086`
- `market_context_high->index_1h` score `0.781` n `47` status `ready` deltaP `12.664` edge `0.0085` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6589` n `103` status `ready` deltaP `15.502` edge `0.0109` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
