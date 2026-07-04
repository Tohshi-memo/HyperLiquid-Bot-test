# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T13:22:27.165200+00:00`
- Price records: `672`
- Market context records: `5666`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8670`

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

- `market_context_high->equity_24h` score `2.1479` n `194` status `ready` deltaP `15.8075` edge `0.5815` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8533` n `244` status `ready` deltaP `11.228` edge `0.2255` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.3836` n `244` status `ready` deltaP `6.9497` edge `0.1495` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.3233` n `244` status `ready` deltaP `8.2742` edge `0.1567` maxDD `-9.46`
- `market_context_high->fx_24h` score `-0.1348` n `194` status `ready` deltaP `16.6953` edge `0.0518` maxDD `-2.6136`
- `market_context_high->fx_1h` score `-0.2699` n `256` status `ready` deltaP `1.8034` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4514` n `256` status `ready` deltaP `4.767` edge `0.0313` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.4927` n `256` status `ready` deltaP `2.4748` edge `0.0386` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.5039` n `256` status `ready` deltaP `0.4818` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.7201` n `256` status `ready` deltaP `3.7565` edge `0.0395` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.8576` n `256` status `ready` deltaP `1.1976` edge `-0.0029` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.9058` n `256` status `ready` deltaP `0.938` edge `0.0051` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.208` n `244` status `ready` deltaP `3.2787` edge `0.0067` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2967` n `244` status `ready` deltaP `-1.152` edge `0.0086` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3904` n `194` status `ready` deltaP `7.9986` edge `0.0389` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9798` n `244` status `ready` deltaP `-13.4197` edge `-0.0542` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.7206` n `244` status `ready` deltaP `-1.4994` edge `-0.0325` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.938` n `194` status `ready` deltaP `3.3935` edge `0.0199` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4265` n `194` status `ready` deltaP `-13.939` edge `-0.2513` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.3542` n `194` status `ready` deltaP `-11.8235` edge `-0.0898` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
