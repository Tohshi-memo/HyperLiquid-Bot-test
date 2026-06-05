# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T14:07:23.836538+00:00`
- Price records: `672`
- Market context records: `2976`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.0343` n `107` status `ready` deltaP `8.0949` edge `1.6739` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `10.4845` n `107` status `ready` deltaP `38.0095` edge `0.6384` maxDD `-0.7805`
- `market_context_high->unknown_24h` score `9.7646` n `107` status `ready` deltaP `15.8829` edge `0.7543` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.0194` n `107` status `ready` deltaP `16.2334` edge `0.6771` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.0161` n `107` status `ready` deltaP `16.1929` edge `0.3248` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.9518` n `108` status `ready` deltaP `15.6786` edge `0.1804` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.0767` n `108` status `ready` deltaP `20.5341` edge `0.115` maxDD `-1.9733`
- `market_context_high->equity_1h` score `1.3178` n `108` status `ready` deltaP `8.9488` edge `0.0835` maxDD `-1.0004`
- `market_context_high->commodity_4h` score `0.91` n `108` status `ready` deltaP `12.4322` edge `0.0985` maxDD `-2.8438`
- `market_context_high->index_1h` score `0.7386` n `108` status `ready` deltaP `9.6141` edge `0.0366` maxDD `-0.7983`
- `market_context_high->crypto_alt_4h` score `0.7345` n `108` status `ready` deltaP `22.1093` edge `0.4029` maxDD `-30.8239`
- `market_context_high->crypto_alt_1h` score `0.2418` n `108` status `ready` deltaP `9.7361` edge `0.1296` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `0.0495` n `108` status `ready` deltaP `9.9523` edge `0.0936` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.3785` n `108` status `ready` deltaP `-0.693` edge `0.0038` maxDD `-0.1244`
- `market_context_high->commodity_1h` score `-0.4242` n `108` status `ready` deltaP `-1.0202` edge `0.003` maxDD `-2.3805`
- `market_context_high->unknown_4h` score `-0.7072` n `108` status `ready` deltaP `0.4799` edge `0.0432` maxDD `-3.7602`
- `market_context_high->metal_1h` score `-0.7778` n `108` status `ready` deltaP `-2.4119` edge `0.0051` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-0.8798` n `108` status `ready` deltaP `3.0107` edge `-0.0203` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.4657` n `108` status `ready` deltaP `-6.7751` edge `0.0009` maxDD `-0.5631`
- `market_context_high->crypto_major_4h` score `-1.9022` n `108` status `ready` deltaP `8.6664` edge `0.2109` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
