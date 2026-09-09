# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T16:37:31.737379+00:00`
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

- `risk_on_high->crypto_alt_24h` score `9.6337` n `117` status `ready` deltaP `22.289` edge `0.6772` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `9.6337` n `117` status `ready` deltaP `22.289` edge `0.6772` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.6922` n `117` status `ready` deltaP `32.3119` edge `0.2961` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.6922` n `117` status `ready` deltaP `32.3119` edge `0.2961` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `4.7471` n `117` status `ready` deltaP `18.1491` edge `0.8944` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.7471` n `117` status `ready` deltaP `18.1491` edge `0.8944` maxDD `-24.5429`
- `market_context_high->crypto_alt_24h` score `4.5863` n `241` status `ready` deltaP `14.9442` edge `0.3653` maxDD `-3.9523`
- `risk_on_high->crypto_major_4h` score `3.8968` n `117` status `ready` deltaP `23.0848` edge `0.2567` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.8968` n `117` status `ready` deltaP `23.0848` edge `0.2567` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.1648` n `117` status `ready` deltaP `22.6095` edge `0.0339` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.1648` n `117` status `ready` deltaP `22.6095` edge `0.0339` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.4433` n `241` status `ready` deltaP `17.7047` edge `0.0416` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9022` n `117` status `ready` deltaP `3.4982` edge `0.0871` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9022` n `117` status `ready` deltaP `3.4982` edge `0.0871` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.681` n `117` status `ready` deltaP `19.7383` edge `0.0713` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.681` n `117` status `ready` deltaP `19.7383` edge `0.0713` maxDD `-0.9131`
- `market_context_high->equity_24h` score `0.4573` n `241` status `ready` deltaP `6.0764` edge `-0.0024` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.2567` n `117` status `ready` deltaP `13.0253` edge `-0.0123` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.2567` n `117` status `ready` deltaP `13.0253` edge `-0.0123` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.2146` n `117` status `ready` deltaP `10.0172` edge `-0.0029` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
