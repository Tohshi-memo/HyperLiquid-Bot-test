# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T10:07:18.324121+00:00`
- Price records: `672`
- Market context records: `1935`
- Flow alert records: `7470`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7540`

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

- `market_context_high->crypto_alt_4h` score `6.9994` n `214` status `ready` deltaP `22.0723` edge `0.5506` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4018` n `214` status `ready` deltaP `25.993` edge `0.4848` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.0865` n `214` status `ready` deltaP `15.5103` edge `0.3562` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0299` n `214` status `ready` deltaP `13.5158` edge `0.1885` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.7923` n `196` status `ready` deltaP `14.8597` edge `0.499` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5394` n `226` status `ready` deltaP `7.3592` edge `0.0945` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4413` n `226` status `ready` deltaP `7.1764` edge `0.1003` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.321` n `196` status `ready` deltaP `12.2626` edge `0.1876` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1718` n `196` status `ready` deltaP `4.2233` edge `0.109` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.0935` n `214` status `ready` deltaP `7.8584` edge `0.0643` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1975` n `226` status `ready` deltaP `4.7282` edge `0.0314` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2525` n `196` status `ready` deltaP `10.1793` edge `0.016` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6031` n `226` status `ready` deltaP `-2.219` edge `0.0007` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6802` n `226` status `ready` deltaP `0.0437` edge `0.0062` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7697` n `226` status `ready` deltaP `3.3901` edge `0.0123` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.9236` n `214` status `ready` deltaP `-4.2883` edge `-0.001` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-0.9983` n `196` status `ready` deltaP `8.1527` edge `0.3523` maxDD `-33.1875`
- `market_context_high->metal_4h` score `-1.3701` n `214` status `ready` deltaP `7.7416` edge `0.1034` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-1.4544` n `226` status `ready` deltaP `0.6889` edge `-0.0306` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.9706` n `226` status `ready` deltaP `1.3142` edge `-0.0056` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
