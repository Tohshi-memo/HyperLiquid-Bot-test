# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T13:52:31.630838+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3916`

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

- `news_risk_high->equity_24h` score `0.492` n `115` status `ready` deltaP `24.9331` edge `1.0555` maxDD `-86.0244`
- `news_risk_high->index_4h` score `0.056` n `115` status `ready` deltaP `10.1074` edge `0.0136` maxDD `-1.9047`
- `news_risk_high->index_1h` score `-0.2668` n `115` status `ready` deltaP `5.7381` edge `0.0017` maxDD `-0.9325`
- `news_risk_high->fx_1h` score `-0.3505` n `115` status `ready` deltaP `-0.7277` edge `-0.0001` maxDD `-0.1984`
- `news_risk_high->index_24h` score `-0.5159` n `115` status `ready` deltaP `-1.8233` edge `0.1295` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.5804` n `115` status `ready` deltaP `1.8107` edge `0.0363` maxDD `-5.8225`
- `news_risk_high->crypto_alt_4h` score `-0.6328` n `115` status `ready` deltaP `3.2582` edge `0.1608` maxDD `-14.0916`
- `news_risk_high->crypto_major_1h` score `-0.8928` n `115` status `ready` deltaP `-2.8079` edge `0.0048` maxDD `-4.7103`
- `news_risk_high->metal_1h` score `-0.9055` n `115` status `ready` deltaP `-2.3236` edge `-0.0096` maxDD `-1.0293`
- `news_risk_high->crypto_major_4h` score `-1.0716` n `115` status `ready` deltaP `-2.7559` edge `0.0621` maxDD `-9.1553`
- `news_risk_high->fx_4h` score `-1.1126` n `115` status `ready` deltaP `-1.5576` edge `-0.0014` maxDD `-0.4745`
- `news_risk_high->fx_24h` score `-1.2634` n `115` status `ready` deltaP `-14.3899` edge `-0.0026` maxDD `-0.4086`
- `news_risk_high->equity_4h` score `-1.3051` n `115` status `ready` deltaP `10.5647` edge `0.1272` maxDD `-20.178`
- `news_risk_high->equity_1h` score `-1.3725` n `115` status `ready` deltaP `-0.5845` edge `0.0182` maxDD `-10.2217`
- `news_risk_high->metal_4h` score `-2.225` n `115` status `ready` deltaP `-5.4653` edge `-0.0433` maxDD `-2.4548`
- `news_risk_high->commodity_1h` score `-2.784` n `115` status `ready` deltaP `-13.5069` edge `-0.0053` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.2989` n `115` status `ready` deltaP `-2.9441` edge `-0.2137` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.9762` n `115` status `ready` deltaP `-24.0827` edge `-0.0187` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.2068` n `115` status `ready` deltaP `-16.624` edge `0.1654` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.3246` n `115` status `ready` deltaP `-23.8438` edge `0.0016` maxDD `-38.9084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
