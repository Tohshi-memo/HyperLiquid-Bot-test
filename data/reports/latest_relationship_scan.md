# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T14:37:31.751576+00:00`
- Price records: `672`
- Market context records: `4836`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7610`

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

- `market_context_high->unknown_1h` score `13.7907` n `109` status `ready` deltaP `11.038` edge `1.1174` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.6801` n `101` status `ready` deltaP `22.5051` edge `0.7695` maxDD `-4.0284`
- `market_context_high->unknown_24h` score `3.9821` n `95` status `ready` deltaP `20.8206` edge `0.2537` maxDD `-2.1866`
- `market_context_high->index_4h` score `0.5151` n `101` status `ready` deltaP `8.1894` edge `0.035` maxDD `-0.7334`
- `market_context_high->equity_1h` score `0.3626` n `109` status `ready` deltaP `4.5775` edge `0.0613` maxDD `-2.928`
- `market_context_high->crypto_alt_4h` score `0.1859` n `101` status `ready` deltaP `13.1384` edge `0.1799` maxDD `-16.4929`
- `market_context_high->equity_4h` score `0.1508` n `101` status `ready` deltaP `10.0926` edge `0.0902` maxDD `-6.3852`
- `market_context_high->commodity_1h` score `0.0775` n `109` status `ready` deltaP `4.5006` edge `0.0281` maxDD `-1.1869`
- `market_context_high->commodity_4h` score `0.0521` n `101` status `ready` deltaP `12.8395` edge `0.0383` maxDD `-4.377`
- `market_context_high->fx_4h` score `-0.175` n `101` status `ready` deltaP `5.9028` edge `0.0064` maxDD `-0.788`
- `market_context_high->index_1h` score `-0.8065` n `109` status `ready` deltaP `-0.5892` edge `0.0122` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-0.8503` n `109` status `ready` deltaP `-5.8905` edge `-0.0048` maxDD `-0.8626`
- `market_context_high->crypto_major_4h` score `-1.0495` n `101` status `ready` deltaP `9.5598` edge `0.1333` maxDD `-23.8601`
- `market_context_high->crypto_alt_1h` score `-1.3002` n `109` status `ready` deltaP `4.09` edge `-0.0016` maxDD `-12.7225`
- `market_context_high->crypto_major_1h` score `-1.9528` n `109` status `ready` deltaP `2.8155` edge `-0.0116` maxDD `-17.9354`
- `market_context_high->fx_24h` score `-2.0547` n `95` status `ready` deltaP `-8.3388` edge `-0.0146` maxDD `-2.749`
- `market_context_high->metal_1h` score `-2.0839` n `109` status `ready` deltaP `0.8309` edge `-0.0624` maxDD `-13.4916`
- `market_context_high->metal_4h` score `-2.589` n `101` status `ready` deltaP `8.7252` edge `-0.0742` maxDD `-21.9379`
- `market_context_high->commodity_24h` score `-2.992` n `95` status `ready` deltaP `14.2635` edge `0.0322` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.3558` n `95` status `ready` deltaP `-5.8753` edge `-0.126` maxDD `-23.4611`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
