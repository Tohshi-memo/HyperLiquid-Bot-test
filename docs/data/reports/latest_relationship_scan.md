# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T02:52:25.234232+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_4h` score `12.565` n `33` status `ready` deltaP `29.878` edge `0.8479` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.6977` n `33` status `ready` deltaP `47.2561` edge `0.2431` maxDD `0.0`
- `news_risk_high->unknown_1h` score `5.5143` n `45` status `ready` deltaP `28.3865` edge `0.2821` maxDD `-0.2787`
- `news_risk_high->fx_4h` score `3.1557` n `33` status `ready` deltaP `36.9457` edge `0.0301` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `2.0537` n `33` status `ready` deltaP `26.4644` edge `0.0031` maxDD `-0.0045`
- `market_context_high->unknown_1h` score `1.5297` n `135` status `ready` deltaP `6.1643` edge `0.1091` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.4366` n `45` status `ready` deltaP `19.4411` edge `0.0071` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3664` n `45` status `ready` deltaP `26.4072` edge `0.0273` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `1.053` n `135` status `ready` deltaP `20.2484` edge `-0.0259` maxDD `-0.3736`
- `news_risk_high->commodity_1h` score `0.4026` n `45` status `ready` deltaP `13.6727` edge `-0.0087` maxDD `-0.4666`
- `news_risk_high->index_4h` score `0.3911` n `33` status `ready` deltaP `9.8624` edge `0.023` maxDD `-0.0884`
- `news_risk_high->metal_1h` score `0.1159` n `45` status `ready` deltaP `6.5802` edge `-0.0067` maxDD `-0.1184`
- `market_context_high->fx_4h` score `0.1039` n `135` status `ready` deltaP `8.2588` edge `0.0085` maxDD `-0.3527`
- `news_risk_high->index_1h` score `0.0197` n `45` status `ready` deltaP `5.2562` edge `0.0028` maxDD `-0.1583`
- `news_risk_high->crypto_major_4h` score `0.0172` n `33` status `ready` deltaP `-3.4183` edge `0.1609` maxDD `-6.9344`
- `market_context_high->index_1h` score `-0.0703` n `135` status `ready` deltaP `5.9969` edge `0.0041` maxDD `-0.9144`
- `news_risk_high->commodity_4h` score `-0.0872` n `33` status `ready` deltaP `7.6543` edge `-0.0202` maxDD `-1.0273`
- `market_context_high->fx_1h` score `-0.1591` n `135` status `ready` deltaP `1.6634` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3595` n `135` status `ready` deltaP `4.185` edge `0.033` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
