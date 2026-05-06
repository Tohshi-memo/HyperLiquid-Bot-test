# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T17:52:18.258534+00:00`
- Price records: `475`
- Market context records: `567`
- Flow alert records: `1599`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.9332` n `144` status `ready` deltaP `7.485` edge `0.366` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.9295` n `144` status `ready` deltaP `9.8725` edge `0.2117` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0106` n `146` status `ready` deltaP `9.8676` edge `0.02` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3117` n `146` status `ready` deltaP `2.0313` edge `0.0043` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5548` n `146` status `ready` deltaP `1.9067` edge `0.0385` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6404` n `146` status `ready` deltaP `0.7876` edge `-0.002` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1547` n `146` status `ready` deltaP `-3.7635` edge `-0.0108` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2166` n `146` status `ready` deltaP `-1.5679` edge `-0.0099` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3671` n `146` status `ready` deltaP `4.0864` edge `-0.0097` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.7308` n `144` status `ready` deltaP `-5.5389` edge `0.0922` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9632` n `146` status `ready` deltaP `3.7504` edge `-0.0163` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.0603` n `146` status `ready` deltaP `1.3322` edge `-0.0283` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.2158` n `146` status `ready` deltaP `2.8546` edge `0.0533` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.0924` n `146` status `ready` deltaP `-2.6238` edge `-0.025` maxDD `-10.5498`
- `market_context_high->crypto_major_4h` score `-3.1654` n `146` status `ready` deltaP `10.262` edge `0.0384` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2408` n `146` status `ready` deltaP `-4.1605` edge `-0.0464` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5534` n `146` status `ready` deltaP `-5.9732` edge `0.0938` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.5677` n `144` status `ready` deltaP `-9.8` edge `0.0285` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.5511` n `144` status `ready` deltaP `-5.5` edge `-0.0418` maxDD `-20.0671`
- `market_context_high->unknown_4h` score `-5.3691` n `146` status `ready` deltaP `-0.1358` edge `-0.2587` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
