# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T14:07:33.743059+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `6.9993` n `54` status `ready` deltaP `38.5017` edge `0.3266` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9993` n `54` status `ready` deltaP `38.5017` edge `0.3266` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `4.5321` n `156` status `ready` deltaP `18.492` edge `0.4084` maxDD `-6.6539`
- `risk_on_high->crypto_major_4h` score `2.8023` n `82` status `ready` deltaP `20.8842` edge `0.2483` maxDD `-6.6539`
- `risk_on_and_context->crypto_major_4h` score `2.8023` n `82` status `ready` deltaP `20.8842` edge `0.2483` maxDD `-6.6539`
- `market_context_high->crypto_alt_4h` score `2.4683` n `156` status `ready` deltaP `10.8037` edge `0.4656` maxDD `-17.2213`
- `market_context_high->crypto_major_1h` score `0.4607` n `168` status `ready` deltaP `5.2181` edge `0.0925` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.151` n `156` status `ready` deltaP `10.6825` edge `0.0459` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.0351` n `90` status `ready` deltaP `5.4054` edge `0.0053` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0351` n `90` status `ready` deltaP `5.4054` edge `0.0053` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.1001` n `168` status `ready` deltaP `6.2625` edge `0.0999` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.2048` n `168` status `ready` deltaP `6.5959` edge `0.0046` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2339` n `168` status `ready` deltaP `7.3139` edge `0.0082` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.2756` n `90` status `ready` deltaP `0.8708` edge `-0.0031` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2756` n `90` status `ready` deltaP `0.8708` edge `-0.0031` maxDD `-0.376`
- `market_context_high->equity_1h` score `-0.3918` n `168` status `ready` deltaP `9.5989` edge `0.0372` maxDD `-7.1141`
- `market_context_high->equity_4h` score `-0.4377` n `156` status `ready` deltaP `12.8087` edge `0.2011` maxDD `-17.4086`
- `market_context_high->fx_1h` score `-0.4591` n `168` status `ready` deltaP `-0.7562` edge `-0.0017` maxDD `-0.503`
- `risk_on_high->equity_1h` score `-0.4831` n `90` status `ready` deltaP `9.5195` edge `0.0259` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4831` n `90` status `ready` deltaP `9.5195` edge `0.0259` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
