# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T03:52:25.847730+00:00`
- Price records: `672`
- Market context records: `5733`
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

- `market_context_high->equity_24h` score `0.8895` n `218` status `ready` deltaP `15.5294` edge `0.5184` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1286` n `283` status `ready` deltaP `7.4372` edge `0.125` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2139` n `285` status `ready` deltaP `2.9357` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4214` n `285` status `ready` deltaP `2.0843` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6008` n `285` status `ready` deltaP `0.8867` edge `0.0039` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6381` n `285` status `ready` deltaP `3.0623` edge `0.0271` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.8096` n `285` status `ready` deltaP `-2.4866` edge `-0.0065` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8153` n `285` status `ready` deltaP `3.0807` edge `0.035` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.9` n `285` status `ready` deltaP `1.7849` edge `0.0335` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1` n `218` status `ready` deltaP `11.2083` edge `0.0426` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1688` n `283` status `ready` deltaP `1.2572` edge `0.0105` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2419` n `283` status `ready` deltaP `2.941` edge `0.0057` maxDD `-1.4288`
- `market_context_high->crypto_major_4h` score `-2.5405` n `283` status `ready` deltaP `6.9664` edge `0.1444` maxDD `-23.5375`
- `market_context_high->metal_4h` score `-2.6374` n `283` status `ready` deltaP `-7.6736` edge `-0.0494` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.9868` n `218` status `ready` deltaP `0.532` edge `0.028` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-3.6719` n `283` status `ready` deltaP `5.2966` edge `0.0995` maxDD `-24.5974`
- `market_context_high->commodity_4h` score `-3.7423` n `283` status `ready` deltaP `-2.4902` edge `-0.0277` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.1975` n `218` status `ready` deltaP `7.8905` edge `0.0433` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6723` n `218` status `ready` deltaP `-7.7758` edge `-0.2433` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.5873` n `218` status `ready` deltaP `-11.2688` edge `-0.0765` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
