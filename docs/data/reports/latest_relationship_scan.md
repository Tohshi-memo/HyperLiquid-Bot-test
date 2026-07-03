# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T15:37:30.728168+00:00`
- Price records: `672`
- Market context records: `5571`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11396`

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

- `market_context_high->equity_24h` score `4.3961` n `176` status `ready` deltaP `15.2304` edge `0.7727` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2347` n `190` status `ready` deltaP `11.1361` edge `0.2579` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `0.9917` n `176` status `ready` deltaP `14.1256` edge `0.4425` maxDD `-29.6555`
- `market_context_high->fx_24h` score `0.7782` n `176` status `ready` deltaP `16.7298` edge `0.0507` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.7356` n `190` status `ready` deltaP `6.5196` edge `0.1817` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.656` n `190` status `ready` deltaP `6.5774` edge `0.1749` maxDD `-9.46`
- `market_context_high->index_1h` score `-0.1552` n `201` status `ready` deltaP `4.1715` edge `0.0086` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.2205` n `201` status `ready` deltaP `6.0029` edge `0.0423` maxDD `-5.0555`
- `market_context_high->fx_4h` score `-0.2604` n `190` status `ready` deltaP `6.2981` edge `0.0097` maxDD `-0.8712`
- `market_context_high->fx_1h` score `-0.3833` n `201` status `ready` deltaP `2.0362` edge `0.0013` maxDD `-0.4122`
- `market_context_high->metal_1h` score `-0.5076` n `201` status `ready` deltaP `0.0506` edge `0.0021` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5438` n `201` status `ready` deltaP `1.0852` edge `0.0436` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.652` n `201` status `ready` deltaP `2.9873` edge `0.0503` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-1.3526` n `201` status `ready` deltaP `-4.0307` edge `-0.0093` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5358` n `190` status `ready` deltaP `2.4358` edge `0.0167` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.9827` n `176` status `ready` deltaP `13.2576` edge `0.0561` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.1104` n `190` status `ready` deltaP `-13.9746` edge `-0.0623` maxDD `-12.1312`
- `market_context_high->commodity_4h` score `-4.5572` n `190` status `ready` deltaP `-8.4323` edge `-0.056` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.8348` n `176` status `ready` deltaP `-7.5758` edge `-0.217` maxDD `-32.9569`
- `market_context_high->crypto_alt_24h` score `-8.8982` n `176` status `ready` deltaP `4.2298` edge `0.1` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
