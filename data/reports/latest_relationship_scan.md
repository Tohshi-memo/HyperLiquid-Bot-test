# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T16:52:27.658098+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10148`

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

- `risk_on_high->crypto_alt_24h` score `9.7604` n `117` status `ready` deltaP `22.4626` edge `0.6866` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.7604` n `117` status `ready` deltaP `22.4626` edge `0.6866` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.7283` n `117` status `ready` deltaP `32.4643` edge `0.2981` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7283` n `117` status `ready` deltaP `32.4643` edge `0.2981` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.8357` n `117` status `ready` deltaP `18.3227` edge `0.9046` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.8357` n `117` status `ready` deltaP `18.3227` edge `0.9046` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `4.713` n `241` status `ready` deltaP `15.1178` edge `0.3747` maxDD `-3.9523`
- `risk_on_high->crypto_major_4h` score `3.939` n `117` status `ready` deltaP `23.2372` edge `0.2592` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.939` n `117` status `ready` deltaP `23.2372` edge `0.2592` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.1883` n `117` status `ready` deltaP `22.7831` edge `0.0347` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.1883` n `117` status `ready` deltaP `22.7831` edge `0.0347` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.4668` n `241` status `ready` deltaP `17.8783` edge `0.0424` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.8926` n `117` status `ready` deltaP `3.4982` edge `0.0863` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8926` n `117` status `ready` deltaP `3.4982` edge `0.0863` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6888` n `117` status `ready` deltaP `19.7383` edge `0.0723` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.6888` n `117` status `ready` deltaP `19.7383` edge `0.0723` maxDD `-0.9131`
- `market_context_high->equity_24h` score `0.5252` n `241` status `ready` deltaP `6.25` edge `0.0021` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.2615` n `117` status `ready` deltaP `13.0253` edge `-0.0119` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.2615` n `117` status `ready` deltaP `13.0253` edge `-0.0119` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.2231` n `117` status `ready` deltaP `10.1669` edge `-0.0028` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
