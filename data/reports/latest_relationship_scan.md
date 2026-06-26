# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T03:52:29.658065+00:00`
- Price records: `672`
- Market context records: `4790`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7530`

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

- `market_context_high->unknown_4h` score `7.6479` n `122` status `ready` deltaP `18.4152` edge `0.6356` maxDD `-4.6834`
- `market_context_high->unknown_1h` score `7.5901` n `122` status `ready` deltaP `12.7295` edge `0.5894` maxDD `-1.674`
- `market_context_high->unknown_24h` score `1.9892` n `107` status `ready` deltaP `11.52` edge `0.1813` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.1657` n `122` status `ready` deltaP `5.8309` edge `0.0337` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.073` n `122` status `ready` deltaP `11.8153` edge `0.0478` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.1968` n `122` status `ready` deltaP `7.9294` edge `0.0905` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.3961` n `122` status `ready` deltaP `6.6899` edge `0.0115` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4614` n `122` status `ready` deltaP `2.5165` edge `0.0017` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.7175` n `122` status `ready` deltaP `1.4185` edge `0.0075` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.9364` n `122` status `ready` deltaP `-1.4823` edge `-0.0032` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3776` n `122` status `ready` deltaP `-1.3473` edge `-0.0054` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.2564` n `122` status `ready` deltaP `-0.7976` edge `-0.0664` maxDD `-14.0715`
- `market_context_high->commodity_24h` score `-2.296` n `107` status `ready` deltaP `18.7078` edge `0.0918` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-3.1076` n `122` status `ready` deltaP `0.8982` edge `-0.041` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.4549` n `107` status `ready` deltaP `-16.4623` edge `-0.0232` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4335` n `122` status `ready` deltaP `0.6847` edge `-0.065` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.8174` n `122` status `ready` deltaP `4.5931` edge `-0.0058` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6354` n `107` status `ready` deltaP `-5.1029` edge `-0.1022` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.11` n `122` status `ready` deltaP `3.3537` edge `-0.139` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.3769` n `122` status `ready` deltaP `6.0776` edge `-0.2904` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
