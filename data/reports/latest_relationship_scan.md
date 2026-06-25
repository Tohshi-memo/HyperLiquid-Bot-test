# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T23:07:27.011385+00:00`
- Price records: `672`
- Market context records: `4769`
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

- `market_context_high->unknown_1h` score `8.0049` n `125` status `ready` deltaP `12.9054` edge `0.6228` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.286` n `125` status `ready` deltaP `17.2366` edge `0.6133` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.1681` n `110` status `ready` deltaP `12.3611` edge `0.1906` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.0474` n `125` status `ready` deltaP `10.9939` edge `0.05` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0269` n `125` status `ready` deltaP `4.7413` edge `0.0294` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.4668` n `125` status `ready` deltaP `2.4573` edge `0.0014` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.4956` n `125` status `ready` deltaP `5.9622` edge `0.0036` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.5619` n `125` status `ready` deltaP `6.5329` edge `0.053` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.9422` n `125` status `ready` deltaP `-1.5557` edge `-0.0032` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-1.0449` n `125` status `ready` deltaP `-0.1988` edge `-0.009` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.4798` n `125` status `ready` deltaP `-2.2946` edge `-0.0076` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1029` n `110` status `ready` deltaP `20.4261` edge `0.1051` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2374` n `125` status `ready` deltaP `-0.6575` edge `-0.0649` maxDD `-14.0715`
- `market_context_high->crypto_major_1h` score `-3.2967` n `125` status `ready` deltaP `-1.3545` edge `-0.0887` maxDD `-23.3274`
- `market_context_high->fx_24h` score `-3.4212` n `110` status `ready` deltaP `-14.2803` edge `-0.0208` maxDD `-3.5277`
- `market_context_high->crypto_alt_1h` score `-3.8405` n `125` status `ready` deltaP `-0.9006` edge `-0.0661` maxDD `-17.1685`
- `market_context_high->crypto_alt_4h` score `-5.0238` n `125` status `ready` deltaP `4.2098` edge `-0.0297` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.922` n `110` status `ready` deltaP `-6.6067` edge `-0.1065` maxDD `-19.4367`
- `market_context_high->crypto_major_4h` score `-8.2774` n `125` status `ready` deltaP `3.0293` edge `-0.1583` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.5213` n `125` status `ready` deltaP `4.4402` edge `-0.298` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
