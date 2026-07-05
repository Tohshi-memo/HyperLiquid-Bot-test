# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T03:37:27.957959+00:00`
- Price records: `672`
- Market context records: `5732`
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

- `market_context_high->equity_24h` score `0.8902` n `218` status `ready` deltaP `15.5294` edge `0.5185` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1215` n `282` status `ready` deltaP `7.3182` edge `0.1252` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2217` n `285` status `ready` deltaP `2.786` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4136` n `285` status `ready` deltaP `2.234` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6094` n `285` status `ready` deltaP `0.737` edge `0.0038` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.625` n `285` status `ready` deltaP `3.212` edge `0.0272` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.7985` n `285` status `ready` deltaP `3.2304` edge `0.0354` maxDD `-5.5448`
- `market_context_high->commodity_1h` score `-0.8096` n `285` status `ready` deltaP `-2.4866` edge `-0.0065` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.9024` n `285` status `ready` deltaP `1.7849` edge `0.0333` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1098` n `218` status `ready` deltaP `11.0347` edge `0.0425` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1664` n `282` status `ready` deltaP `1.3028` edge `0.0105` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2405` n `282` status `ready` deltaP `2.9828` edge `0.0056` maxDD `-1.4288`
- `market_context_high->crypto_major_4h` score `-2.2581` n `282` status `ready` deltaP `7.1819` edge `0.1479` maxDD `-22.383`
- `market_context_high->metal_4h` score `-2.628` n `282` status `ready` deltaP `-7.5095` edge `-0.0493` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.977` n `218` status `ready` deltaP `0.7056` edge `0.0281` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-3.4385` n `282` status `ready` deltaP `5.3559` edge `0.1022` maxDD `-23.6223`
- `market_context_high->commodity_4h` score `-3.7645` n `282` status `ready` deltaP `-2.7082` edge `-0.0281` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.2366` n `218` status `ready` deltaP `7.7169` edge `0.0412` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6609` n `218` status `ready` deltaP `-7.6022` edge `-0.243` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.5674` n `218` status `ready` deltaP `-11.0952` edge `-0.076` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
