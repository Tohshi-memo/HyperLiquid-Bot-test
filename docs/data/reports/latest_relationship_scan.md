# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T22:52:35.334110+00:00`
- Price records: `672`
- Market context records: `4768`
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

- `market_context_high->unknown_1h` score `7.95` n `126` status `ready` deltaP `13.1784` edge `0.6164` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.1582` n `126` status `ready` deltaP `16.8239` edge `0.6054` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.2545` n `111` status `ready` deltaP `12.6314` edge `0.196` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `-0.0033` n `126` status `ready` deltaP `10.5812` edge `0.0472` maxDD `-4.4534`
- `market_context_high->commodity_1h` score `-0.0159` n `126` status `ready` deltaP `4.3413` edge `0.0285` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.4834` n `126` status `ready` deltaP `6.1654` edge `0.0038` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4891` n `126` status `ready` deltaP `2.0446` edge `0.0013` maxDD `-1.5439`
- `market_context_high->equity_4h` score `-0.5241` n `126` status `ready` deltaP `6.8694` edge `0.0556` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.9724` n `126` status `ready` deltaP `-1.9176` edge `-0.0033` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-1.0086` n `126` status `ready` deltaP `0.1949` edge `-0.0086` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.4435` n `126` status `ready` deltaP `-1.9009` edge `-0.0072` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1437` n `111` status `ready` deltaP `20.092` edge `0.1021` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2079` n `126` status `ready` deltaP `-0.2258` edge `-0.064` maxDD `-14.0715`
- `market_context_high->crypto_major_1h` score `-3.4222` n `126` status `ready` deltaP `-1.7228` edge `-0.0926` maxDD `-24.1056`
- `market_context_high->fx_24h` score `-3.485` n `111` status `ready` deltaP `-14.4098` edge `-0.0206` maxDD `-3.5669`
- `market_context_high->crypto_alt_1h` score `-4.0736` n `126` status `ready` deltaP `-1.2879` edge `-0.0715` maxDD `-18.0839`
- `market_context_high->crypto_alt_4h` score `-4.9781` n `126` status `ready` deltaP `4.5781` edge `-0.0263` maxDD `-46.0617`
- `market_context_high->index_24h` score `-6.0076` n `111` status `ready` deltaP `-7.0899` edge `-0.1072` maxDD `-19.6931`
- `market_context_high->crypto_major_4h` score `-8.2065` n `126` status `ready` deltaP `3.4166` edge `-0.1518` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.4816` n `126` status `ready` deltaP `4.6941` edge `-0.2946` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
