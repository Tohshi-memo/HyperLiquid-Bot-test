# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T20:37:37.144953+00:00`
- Price records: `672`
- Market context records: `5385`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `6.1502` n `188` status `ready` deltaP `16.9253` edge `0.4127` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.4111` n `188` status `ready` deltaP `22.9573` edge `0.7519` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.5153` n `205` status `ready` deltaP `14.939` edge `0.4226` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0109` n `205` status `ready` deltaP `12.0732` edge `0.3345` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.2765` n `205` status `ready` deltaP `10.9757` edge `0.2804` maxDD `-7.4425`
- `market_context_high->equity_24h` score `1.5798` n `188` status `ready` deltaP `10.5497` edge `0.6242` maxDD `-40.0306`
- `market_context_high->equity_1h` score `0.3949` n `205` status `ready` deltaP `7.3105` edge `0.0807` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.0861` n `205` status `ready` deltaP `4.6239` edge `0.1009` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.0708` n `205` status `ready` deltaP `2.5281` edge `0.0852` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0304` n `205` status `ready` deltaP `5.4265` edge `0.0157` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.2151` n `188` status `ready` deltaP `6.3165` edge `0.0295` maxDD `-0.8294`
- `market_context_high->unknown_4h` score `-0.3919` n `205` status `ready` deltaP `8.2927` edge `0.0305` maxDD `-6.1421`
- `market_context_high->fx_1h` score `-0.4563` n `205` status `ready` deltaP `-1.2531` edge `-0.0012` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.4711` n `205` status `ready` deltaP `2.079` edge `0.0144` maxDD `-2.0682`
- `market_context_high->index_24h` score `-0.6309` n `188` status `ready` deltaP `15.0155` edge `0.0831` maxDD `-9.5288`
- `market_context_high->index_4h` score `-1.0393` n `205` status `ready` deltaP `5.7926` edge `0.0357` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2047` n `205` status `ready` deltaP `0.2439` edge `0.0009` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4927` n `205` status `ready` deltaP `-3.4701` edge `-0.0068` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.4472` n `205` status `ready` deltaP `-5.4573` edge `-0.0249` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.1357` n `188` status `ready` deltaP `13.8593` edge `0.3753` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
