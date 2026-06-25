# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T21:22:34.214583+00:00`
- Price records: `672`
- Market context records: `4761`
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

- `market_context_high->unknown_1h` score `7.2238` n `132` status `ready` deltaP `12.6066` edge `0.5597` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.6272` n `129` status `ready` deltaP `15.0159` edge `0.5732` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.7953` n `117` status `ready` deltaP `14.156` edge `0.2309` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3206` n `132` status `ready` deltaP `2.6674` edge `0.0226` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `-0.3948` n `129` status `ready` deltaP `9.3815` edge `0.034` maxDD `-6.7722`
- `market_context_high->equity_4h` score `-0.3991` n `129` status `ready` deltaP `8.0131` edge `0.064` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.4394` n `129` status `ready` deltaP `6.7415` edge `0.0056` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.5955` n `129` status `ready` deltaP `0.2222` edge `-0.0002` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.7709` n `132` status `ready` deltaP `-0.2903` edge `-0.014` maxDD `-4.6318`
- `market_context_high->fx_1h` score `-1.1489` n `132` status `ready` deltaP `-3.9739` edge `-0.0043` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.5796` n `132` status `ready` deltaP `-3.4522` edge `-0.0082` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.3867` n `117` status `ready` deltaP `18.2693` edge `0.0831` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3891` n `132` status `ready` deltaP `-2.0187` edge `-0.0685` maxDD `-14.6135`
- `market_context_high->crypto_major_1h` score `-3.4147` n `132` status `ready` deltaP `-1.3927` edge `-0.0854` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-3.9043` n `117` status `ready` deltaP `-15.0775` edge `-0.0208` maxDD `-3.9898`
- `market_context_high->crypto_alt_1h` score `-4.6305` n `132` status `ready` deltaP `-2.2818` edge `-0.0728` maxDD `-19.8288`
- `market_context_high->crypto_alt_4h` score `-5.4559` n `129` status `ready` deltaP `1.912` edge `-0.0451` maxDD `-48.0361`
- `market_context_high->index_24h` score `-6.5468` n `117` status `ready` deltaP `-9.8157` edge `-0.1122` maxDD `-21.4344`
- `market_context_high->crypto_major_4h` score `-8.2459` n `129` status `ready` deltaP `2.6742` edge `-0.1519` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.2946` n `129` status `ready` deltaP `6.0408` edge `-0.2796` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
