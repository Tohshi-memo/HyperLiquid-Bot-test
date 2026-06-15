# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T16:31:48.197982+00:00`
- Price records: `672`
- Market context records: `4007`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10412`

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

- `risk_on_high->unknown_4h` score `147.1796` n `40` status `ready` deltaP `-3.8394` edge `12.4722` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `147.1796` n `40` status `ready` deltaP `-3.8394` edge `12.4722` maxDD `-10.864`
- `market_context_high->unknown_24h` score `49.0062` n `135` status `ready` deltaP `-2.8783` edge `4.5059` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.7385` n `146` status `ready` deltaP `3.0442` edge `2.7502` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `8.2178` n `40` status `ready` deltaP `40.7279` edge `0.4133` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.2178` n `40` status `ready` deltaP `40.7279` edge `0.4133` maxDD `0.0`
- `market_context_high->index_24h` score `4.0034` n `135` status `ready` deltaP `26.9414` edge `0.2025` maxDD `-3.2125`
- `risk_on_high->equity_4h` score `3.782` n `40` status `ready` deltaP `37.3782` edge `0.0707` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.782` n `40` status `ready` deltaP `37.3782` edge `0.0707` maxDD `-0.0446`
- `market_context_high->metal_24h` score `3.2049` n `135` status `ready` deltaP `15.1178` edge `0.2852` maxDD `-6.5125`
- `risk_on_high->index_24h` score `2.1538` n `40` status `ready` deltaP `28.4229` edge `-0.01` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.1538` n `40` status `ready` deltaP `28.4229` edge `-0.01` maxDD `0.0`
- `market_context_high->equity_4h` score `1.9698` n `146` status `ready` deltaP `20.0152` edge `0.1588` maxDD `-6.9137`
- `market_context_high->equity_24h` score `1.9246` n `135` status `ready` deltaP `17.0242` edge `0.3467` maxDD `-14.318`
- `risk_on_high->crypto_major_4h` score `1.2491` n `40` status `ready` deltaP `19.8364` edge `0.0384` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.2491` n `40` status `ready` deltaP `19.8364` edge `0.0384` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.175` n `147` status `ready` deltaP `12.794` edge `0.0601` maxDD `-1.7983`
- `market_context_high->equity_1h` score `1.1253` n `147` status `ready` deltaP `9.0357` edge `0.0895` maxDD `-2.144`
- `risk_on_high->commodity_24h` score `1.0436` n `40` status `ready` deltaP `4.2028` edge `0.2871` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0436` n `40` status `ready` deltaP `4.2028` edge `0.2871` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
