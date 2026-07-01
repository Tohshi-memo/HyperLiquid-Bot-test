# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T19:22:26.089892+00:00`
- Price records: `672`
- Market context records: `5380`
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

- `market_context_high->unknown_24h` score `7.5617` n `183` status `ready` deltaP `16.809` edge `0.5311` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.5019` n `183` status `ready` deltaP `22.9679` edge `0.7594` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.2648` n `205` status `ready` deltaP `14.1768` edge `0.4068` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.7459` n `205` status `ready` deltaP `11.311` edge `0.3175` maxDD `-9.46`
- `market_context_high->equity_24h` score `2.4254` n `183` status `ready` deltaP `12.5997` edge `0.681` maxDD `-40.0306`
- `market_context_high->equity_4h` score `1.9635` n `205` status `ready` deltaP `10.2135` edge `0.2594` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.1862` n `205` status `ready` deltaP `6.562` edge `0.0683` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0618` n `205` status `ready` deltaP `4.678` edge `0.013` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.0647` n `205` status `ready` deltaP `1.9293` edge `0.0779` maxDD `-5.0257`
- `market_context_high->fx_24h` score `-0.0932` n `183` status `ready` deltaP `7.5848` edge `0.0312` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.0974` n `205` status `ready` deltaP `3.8754` edge `0.0906` maxDD `-6.9639`
- `market_context_high->index_24h` score `-0.1029` n `183` status `ready` deltaP `16.254` edge `0.0926` maxDD `-9.0959`
- `market_context_high->unknown_4h` score `-0.4227` n `205` status `ready` deltaP `8.5975` edge `0.0259` maxDD `-6.1421`
- `market_context_high->fx_1h` score `-0.4399` n `205` status `ready` deltaP `-0.9537` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.549` n `205` status `ready` deltaP `1.4802` edge `0.0119` maxDD `-2.0682`
- `market_context_high->index_4h` score `-1.1459` n `205` status `ready` deltaP `5.0305` edge `0.0319` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1815` n `205` status `ready` deltaP `0.5488` edge `0.0008` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.5346` n `205` status `ready` deltaP `-3.9192` edge `-0.0073` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.5116` n `205` status `ready` deltaP `-6.0671` edge `-0.0291` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.1932` n `183` status `ready` deltaP `13.5502` edge `0.37` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
