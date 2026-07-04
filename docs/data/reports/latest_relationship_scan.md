# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T12:52:30.661662+00:00`
- Price records: `672`
- Market context records: `5664`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.2077` n `192` status `ready` deltaP `15.625` edge `0.5877` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8511` n `242` status `ready` deltaP `10.9164` edge `0.2274` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4456` n `242` status `ready` deltaP `7.4543` edge `0.1513` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.2787` n `242` status `ready` deltaP `7.9558` edge `0.1551` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.0375` n `192` status `ready` deltaP `17.1875` edge `0.0529` maxDD `-2.4818`
- `market_context_high->fx_1h` score `-0.2478` n `254` status `ready` deltaP `2.2125` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4569` n `254` status `ready` deltaP `4.6973` edge `0.0313` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.5084` n `254` status `ready` deltaP `2.3681` edge `0.038` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.5249` n `254` status `ready` deltaP `0.0943` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.7647` n `254` status `ready` deltaP `3.3936` edge `0.0382` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.8512` n `254` status `ready` deltaP `1.2919` edge `-0.003` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.9356` n `254` status `ready` deltaP `0.5658` edge `0.0051` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.2146` n `242` status `ready` deltaP `3.1534` edge `0.0067` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2999` n `242` status `ready` deltaP `-1.2434` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3769` n `192` status `ready` deltaP `8.3333` edge `0.0384` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9941` n `242` status `ready` deltaP `-13.6364` edge `-0.0546` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.7403` n `242` status `ready` deltaP `-1.6857` edge `-0.0329` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.8573` n `192` status `ready` deltaP `3.4722` edge `0.0261` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4482` n `192` status `ready` deltaP `-14.2361` edge `-0.2521` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.4431` n `192` status `ready` deltaP `-12.5` edge `-0.0927` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
