# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T03:37:31.469431+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `3574.9789` n `48` status `ready` deltaP `22.0486` edge `297.81` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.9143` n `40` status `ready` deltaP `51.4583` edge `0.8562` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.145` n `40` status `ready` deltaP `51.3194` edge `0.5994` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `2.9627` n `48` status `ready` deltaP `5.5894` edge `0.286` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.2466` n `48` status `ready` deltaP `11.9918` edge `0.062` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.4229` n `46` status `ready` deltaP `6.0976` edge `0.0982` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.3666` n `47` status `ready` deltaP `7.5646` edge `0.034` maxDD `-1.3282`
- `news_risk_high->metal_4h` score `0.3604` n `48` status `ready` deltaP `9.1972` edge `0.02` maxDD `-0.8085`
- `market_context_high->fx_4h` score `0.1946` n `46` status `ready` deltaP `14.7866` edge `0.0` maxDD `-1.589`
- `news_risk_high->metal_1h` score `0.1777` n `48` status `ready` deltaP `6.6866` edge `0.0102` maxDD `-0.5599`
- `news_risk_high->index_1h` score `0.1169` n `48` status `ready` deltaP `5.9381` edge `0.0077` maxDD `-0.5845`
- `news_risk_high->equity_1h` score `0.0903` n `48` status `ready` deltaP `4.1417` edge `0.0622` maxDD `-2.916`
- `market_context_high->fx_1h` score `-0.0162` n `47` status `ready` deltaP `6.8161` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->fx_1h` score `-0.0551` n `48` status `ready` deltaP `3.5803` edge `0.0038` maxDD `-0.2475`
- `market_context_high->crypto_alt_4h` score `-0.0607` n `46` status `ready` deltaP `3.1615` edge `0.0617` maxDD `-4.9116`
- `news_risk_high->commodity_1h` score `-0.1955` n `48` status `ready` deltaP `6.4122` edge `-0.0173` maxDD `-1.7076`
- `news_risk_high->crypto_alt_1h` score `-0.3232` n `48` status `ready` deltaP `3.4306` edge `0.0039` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `-0.3262` n `48` status `ready` deltaP `4.3699` edge `0.0248` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.4443` n `48` status `ready` deltaP `3.73` edge `-0.0098` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.7031` n `40` status `ready` deltaP `0.6597` edge `0.035` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
