# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T21:07:31.265462+00:00`
- Price records: `672`
- Market context records: `5595`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.6895` n `174` status `ready` deltaP `15.0084` edge `0.7153` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.3351` n `209` status `ready` deltaP `12.2855` edge `0.2586` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.1177` n `174` status `ready` deltaP `20.2227` edge `0.0557` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.6333` n `209` status `ready` deltaP `7.344` edge `0.1679` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.5898` n `209` status `ready` deltaP `6.7977` edge `0.1677` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.3007` n `221` status `ready` deltaP `1.138` edge `0.0011` maxDD `-0.4457`
- `market_context_high->equity_1h` score `-0.3611` n `221` status `ready` deltaP `5.4008` edge `0.0346` maxDD `-5.0555`
- `market_context_high->crypto_major_24h` score `-0.3843` n `174` status `ready` deltaP `11.7158` edge `0.3439` maxDD `-29.6555`
- `market_context_high->index_1h` score `-0.4858` n `221` status `ready` deltaP `1.604` edge `0.0065` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.53` n `221` status `ready` deltaP `4.4517` edge `0.0507` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.5318` n `221` status `ready` deltaP `1.4611` edge `0.0421` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.5911` n `221` status `ready` deltaP `-1.2843` edge `0.0003` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-1.1284` n `209` status `ready` deltaP `3.3004` edge `0.0086` maxDD `-0.9711`
- `market_context_high->commodity_1h` score `-1.2197` n `221` status `ready` deltaP `-2.6384` edge `-0.0075` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5194` n `209` status `ready` deltaP `3.0167` edge `0.0142` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.2721` n `174` status `ready` deltaP `11.1291` edge `0.0332` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9269` n `209` status `ready` deltaP `-11.9384` edge `-0.0573` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1511` n `209` status `ready` deltaP `-5.1254` edge `-0.0442` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0486` n `174` status `ready` deltaP `-8.501` edge `-0.2391` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-10.4723` n `174` status `ready` deltaP `1.5026` edge `-0.013` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
