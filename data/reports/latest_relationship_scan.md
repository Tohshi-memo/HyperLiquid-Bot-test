# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T06:37:25.611470+00:00`
- Price records: `672`
- Market context records: `5955`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11184`

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

- `news_risk_high->fx_24h` score `6.9204` n `30` status `ready` deltaP `63.1944` edge `0.1554` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4337` n `30` status `ready` deltaP `39.0973` edge `0.2127` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8576` n `30` status `ready` deltaP `40.0` edge `0.0594` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0945` n `30` status `ready` deltaP `25.2794` edge `0.0199` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5001` n `224` status `ready` deltaP `9.7125` edge `0.1697` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.884` n `30` status `ready` deltaP `10.6387` edge `0.0891` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2504` n `30` status `ready` deltaP `5.7685` edge `0.0398` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1866` n `30` status `ready` deltaP `6.9791` edge `0.0167` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3339` n `30` status `ready` deltaP `2.7345` edge `-0.0244` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.3383` n `236` status `ready` deltaP `5.0061` edge `0.0361` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4835` n `236` status `ready` deltaP `2.3673` edge `0.0021` maxDD `-2.0564`
- `market_context_high->equity_24h` score `-0.5865` n `213` status `ready` deltaP `20.2685` edge `0.2973` maxDD `-31.2762`
- `market_context_high->commodity_1h` score `-0.6221` n `236` status `ready` deltaP `-3.3645` edge `-0.0016` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6302` n `236` status `ready` deltaP `0.8475` edge `0.0049` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6683` n `236` status `ready` deltaP `-0.5963` edge `-0.0006` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.0843` n `30` status `ready` deltaP `-10.0` edge `-0.0209` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1126` n `236` status `ready` deltaP `1.9664` edge `0.021` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1128` n `236` status `ready` deltaP `2.0679` edge `0.0188` maxDD `-9.3536`
- `market_context_high->metal_4h` score `-1.5539` n `224` status `ready` deltaP `-1.753` edge `-0.0243` maxDD `-5.725`
- `market_context_high->commodity_4h` score `-1.6531` n `224` status `ready` deltaP `-3.7348` edge `-0.0157` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
