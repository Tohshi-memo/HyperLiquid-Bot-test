# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T15:07:25.103465+00:00`
- Price records: `672`
- Market context records: `5674`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8758`

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

- `market_context_high->equity_24h` score `2.0748` n `198` status `ready` deltaP `16.3194` edge `0.572` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9638` n `248` status `ready` deltaP `11.728` edge `0.2249` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4905` n `248` status `ready` deltaP `8.7873` edge `0.1633` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.2568` n `248` status `ready` deltaP `5.9647` edge `0.1455` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2577` n `260` status `ready` deltaP `2.0083` edge `0.0012` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4723` n `260` status `ready` deltaP `4.6108` edge `0.0306` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.4918` n `260` status `ready` deltaP `2.4551` edge `0.0388` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.5624` n `260` status `ready` deltaP `1.4302` edge `0.0052` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6509` n `260` status `ready` deltaP `4.2308` edge `0.0421` maxDD `-6.9639`
- `market_context_high->fx_24h` score `-0.6531` n `198` status `ready` deltaP `15.5777` edge `0.0494` maxDD `-2.9474`
- `market_context_high->metal_1h` score `-0.7655` n `260` status `ready` deltaP `0.6195` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.9051` n `260` status `ready` deltaP `0.6633` edge `-0.0033` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2021` n `248` status `ready` deltaP `3.3782` edge `0.0068` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2637` n `248` status `ready` deltaP `-0.4869` edge `0.0084` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.5008` n `198` status `ready` deltaP `6.3763` edge `0.0361` maxDD `-16.9377`
- `market_context_high->metal_4h` score `-2.9086` n `248` status `ready` deltaP `-12.2591` edge `-0.0536` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.7244` n `248` status `ready` deltaP `-1.6522` edge `-0.0318` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.6332` n `198` status `ready` deltaP `4.214` edge `0.0315` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3388` n `198` status `ready` deltaP `-12.721` edge `-0.2497` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.3085` n `198` status `ready` deltaP `-11.8372` edge `-0.0859` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
