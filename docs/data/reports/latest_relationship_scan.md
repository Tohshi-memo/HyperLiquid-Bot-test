# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T04:22:30.939777+00:00`
- Price records: `672`
- Market context records: `5735`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8882`

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

- `market_context_high->equity_24h` score `0.8758` n `218` status `ready` deltaP `15.3558` edge `0.5178` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1438` n `285` status `ready` deltaP `7.6728` edge `0.1247` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.1983` n `285` status `ready` deltaP `3.2351` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4377` n `285` status `ready` deltaP `1.7849` edge `-0.0005` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6094` n `285` status `ready` deltaP `0.737` edge `0.0038` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6657` n `285` status `ready` deltaP `2.7629` edge `0.0268` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.8002` n `285` status `ready` deltaP `-2.3369` edge `-0.0063` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8572` n `285` status `ready` deltaP `2.7813` edge `0.0335` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.9216` n `285` status `ready` deltaP `1.6352` edge `0.0327` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.0803` n `218` status `ready` deltaP `11.5555` edge `0.0428` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1733` n `285` status `ready` deltaP `1.1703` edge `0.0105` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2468` n `285` status `ready` deltaP `2.8616` edge `0.0056` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.655` n `285` status `ready` deltaP `-7.9985` edge `-0.0495` maxDD `-11.6719`
- `market_context_high->crypto_major_4h` score `-2.9508` n `285` status `ready` deltaP `6.8448` edge `0.139` maxDD `-25.1094`
- `market_context_high->index_24h` score `-3.0072` n `218` status `ready` deltaP `0.1848` edge `0.0277` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.6981` n `285` status `ready` deltaP `-2.0587` edge `-0.0269` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-4.1039` n `285` status `ready` deltaP `4.8775` edge `0.0945` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.144` n `218` status `ready` deltaP `8.0642` edge `0.0466` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6973` n `218` status `ready` deltaP `-8.1231` edge `-0.2442` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.6271` n `218` status `ready` deltaP `-11.616` edge `-0.0775` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
