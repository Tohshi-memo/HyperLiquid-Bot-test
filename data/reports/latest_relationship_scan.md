# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T05:52:28.281581+00:00`
- Price records: `672`
- Market context records: `5952`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `6.8981` n `30` status `ready` deltaP `63.0208` edge `0.1547` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4584` n `30` status `ready` deltaP `39.2709` edge `0.2136` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8186` n `30` status `ready` deltaP `39.5427` edge `0.0592` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0945` n `30` status `ready` deltaP `25.2794` edge `0.0199` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6407` n `221` status `ready` deltaP `10.5852` edge `0.1756` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.9213` n `30` status `ready` deltaP `11.0878` edge `0.0909` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2917` n `30` status `ready` deltaP `6.2176` edge `0.0421` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1968` n `30` status `ready` deltaP `6.9791` edge `0.0154` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3425` n `30` status `ready` deltaP `2.7345` edge `-0.0255` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.3814` n `233` status `ready` deltaP `4.7763` edge `0.0321` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4716` n `233` status `ready` deltaP `2.1909` edge `0.0005` maxDD `-2.0457`
- `market_context_high->index_1h` score `-0.6538` n `233` status `ready` deltaP `0.514` edge `0.0041` maxDD `-1.3078`
- `market_context_high->commodity_1h` score `-0.6729` n `233` status `ready` deltaP `-4.0573` edge `-0.0035` maxDD `-1.4578`
- `market_context_high->equity_24h` score `-0.683` n `213` status `ready` deltaP `19.7477` edge `0.2884` maxDD `-31.2762`
- `market_context_high->fx_1h` score `-0.726` n `233` status `ready` deltaP `-1.2728` edge `-0.0009` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.0641` n `30` status `ready` deltaP `-9.7006` edge `-0.0203` maxDD `-1.1161`
- `market_context_high->crypto_alt_1h` score `-1.1319` n `233` status `ready` deltaP `1.9114` edge `0.0174` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-1.1337` n `233` status `ready` deltaP `1.8318` edge `0.0192` maxDD `-9.807`
- `market_context_high->metal_4h` score `-1.5308` n `221` status `ready` deltaP `-1.4892` edge `-0.0231` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.6622` n `221` status `ready` deltaP `1.3974` edge `0.0209` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
