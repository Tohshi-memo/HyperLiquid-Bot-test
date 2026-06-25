# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T23:52:27.821781+00:00`
- Price records: `672`
- Market context records: `4773`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `8.2105` n `122` status `ready` deltaP `12.7295` edge `0.6411` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.3787` n `122` status `ready` deltaP `17.1956` edge `0.6213` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.8572` n `107` status `ready` deltaP `11.52` edge `0.1703` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.1545` n `122` status `ready` deltaP `12.2726` edge `0.0552` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.1297` n `122` status `ready` deltaP `5.5315` edge `0.0327` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.3941` n `122` status `ready` deltaP `3.736` edge `0.0022` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.5653` n `122` status `ready` deltaP `4.8606` edge `0.002` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.6816` n `122` status `ready` deltaP `5.4903` edge `0.0446` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.8597` n `122` status `ready` deltaP `-0.5841` edge `-0.0028` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-1.0568` n `122` status `ready` deltaP `-0.0785` edge `-0.0108` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.5393` n `122` status `ready` deltaP `-2.8443` edge `-0.0089` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-1.9917` n `107` status `ready` deltaP `21.4856` edge `0.1123` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3421` n `122` status `ready` deltaP `-1.6958` edge `-0.0714` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-3.2214` n `107` status `ready` deltaP `-13.8581` edge `-0.0211` maxDD `-3.3968`
- `market_context_high->crypto_alt_1h` score `-3.3822` n `122` status `ready` deltaP `-0.1497` edge `-0.0569` maxDD `-15.2495`
- `market_context_high->crypto_major_1h` score `-4.7609` n `122` status `ready` deltaP `-0.6626` edge `-0.0833` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.2243` n `122` status `ready` deltaP `3.0688` edge `-0.0478` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6642` n `107` status `ready` deltaP `-5.1029` edge `-0.1046` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.5582` n `122` status `ready` deltaP `1.8293` edge `-0.1863` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.6831` n `122` status `ready` deltaP `3.6386` edge `-0.3134` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
