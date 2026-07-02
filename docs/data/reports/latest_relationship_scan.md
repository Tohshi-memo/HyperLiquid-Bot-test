# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T14:07:32.590003+00:00`
- Price records: `672`
- Market context records: `5461`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11444`

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

- `market_context_high->crypto_major_24h` score `3.8396` n `196` status `ready` deltaP `17.0245` edge `0.6605` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.4815` n `199` status `ready` deltaP `14.7506` edge `0.3377` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.9985` n `199` status `ready` deltaP `11.8205` edge `0.2516` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8941` n `199` status `ready` deltaP `9.8442` edge `0.2563` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.2028` n `199` status `ready` deltaP `7.564` edge `0.063` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0755` n `199` status `ready` deltaP `6.1851` edge `0.0144` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0348` n `196` status `ready` deltaP `9.7541` edge `0.0306` maxDD `-1.0847`
- `market_context_high->equity_24h` score `-0.0712` n `196` status `ready` deltaP `8.064` edge `0.4482` maxDD `-31.6316`
- `market_context_high->metal_1h` score `-0.342` n `199` status `ready` deltaP `3.5123` edge `0.0156` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5297` n `199` status `ready` deltaP `0.7109` edge `0.0` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.5924` n `199` status `ready` deltaP `0.2084` edge `0.0454` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7842` n `199` status `ready` deltaP `1.3954` edge `0.0499` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.9201` n `199` status `ready` deltaP `6.8629` edge `0.0385` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.0178` n `199` status `ready` deltaP `1.9342` edge `0.0048` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.3732` n `199` status `ready` deltaP `-2.1221` edge `-0.0055` maxDD `-3.5831`
- `market_context_high->index_24h` score `-2.0189` n `196` status `ready` deltaP `12.1279` edge `0.059` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.5696` n `199` status `ready` deltaP `-7.5124` edge `-0.0269` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.1296` n `199` status `ready` deltaP `-5.1132` edge `-0.0386` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-6.9442` n `196` status `ready` deltaP `8.4042` edge `0.235` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-6.9538` n `196` status `ready` deltaP `-2.4978` edge `-0.1371` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
