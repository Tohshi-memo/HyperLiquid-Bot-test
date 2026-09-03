# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T16:07:29.807581+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11625`

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

- `risk_on_high->unknown_4h` score `32.877` n `133` status `ready` deltaP `12.657` edge `2.7172` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `32.877` n `133` status `ready` deltaP `12.657` edge `2.7172` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `26.112` n `167` status `ready` deltaP `14.2553` edge `2.1505` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.1565` n `133` status `ready` deltaP `1.0422` edge `1.5638` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.1565` n `133` status `ready` deltaP `1.0422` edge `1.5638` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.6767` n `167` status `ready` deltaP `1.497` edge `1.1928` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.0463` n `127` status `ready` deltaP `20.6433` edge `0.5508` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `2.9222` n `67` status `ready` deltaP `20.2192` edge `0.5333` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `2.5634` n `107` status `ready` deltaP `15.8895` edge `0.5222` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `2.5634` n `107` status `ready` deltaP `15.8895` edge `0.5222` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `2.4056` n `67` status `ready` deltaP `16.7159` edge `0.6353` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.4648` n `67` status `ready` deltaP `8.3152` edge `0.3791` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `0.6694` n `107` status `ready` deltaP `16.0485` edge `0.6692` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.6694` n `107` status `ready` deltaP `16.0485` edge `0.6692` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `0.3904` n `127` status `ready` deltaP `17.7042` edge `0.6819` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.3355` n `67` status `ready` deltaP `6.7096` edge `0.0342` maxDD `-0.8733`
- `news_risk_high->fx_4h` score `0.0933` n `67` status `ready` deltaP `10.2612` edge `0.005` maxDD `-1.2507`
- `risk_on_high->metal_1h` score `0.033` n `133` status `ready` deltaP `11.2152` edge `0.0007` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.033` n `133` status `ready` deltaP `11.2152` edge `0.0007` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.057` n `67` status `ready` deltaP `4.6251` edge `-0.0028` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
