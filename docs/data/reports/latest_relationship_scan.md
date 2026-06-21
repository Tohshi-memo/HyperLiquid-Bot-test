# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T08:07:29.944144+00:00`
- Price records: `672`
- Market context records: `4293`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10730`

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

- `risk_on_high->unknown_4h` score `130.4204` n `44` status `ready` deltaP `-3.1181` edge `11.071` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.4204` n `44` status `ready` deltaP `-3.1181` edge `11.071` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.748` n `236` status `ready` deltaP `2.0071` edge `2.4569` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.777` n `236` status `ready` deltaP `-0.0749` edge `1.2749` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.1752` n `202` status `ready` deltaP `-7.7249` edge `1.0528` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.9857` n `44` status `ready` deltaP `30.959` edge `-0.0362` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9857` n `44` status `ready` deltaP `30.959` edge `-0.0362` maxDD `-0.044`
- `risk_on_high->metal_24h` score `1.3948` n `40` status `ready` deltaP `-21.9097` edge `0.3863` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `1.3948` n `40` status `ready` deltaP `-21.9097` edge `0.3863` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `1.0653` n `40` status `ready` deltaP `22.9167` edge `-0.064` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.0653` n `40` status `ready` deltaP `22.9167` edge `-0.064` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.0504` n `44` status `ready` deltaP `15.8675` edge `0.0483` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0504` n `44` status `ready` deltaP `15.8675` edge `0.0483` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4207` n `44` status `ready` deltaP `8.1927` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4207` n `44` status `ready` deltaP `8.1927` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1659` n `44` status `ready` deltaP `8.2472` edge `0.0205` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1659` n `44` status `ready` deltaP `8.2472` edge `0.0205` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0107` n `44` status `ready` deltaP `8.4811` edge `0.0039` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0107` n `44` status `ready` deltaP `8.4811` edge `0.0039` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0633` n `44` status `ready` deltaP `6.478` edge `-0.0095` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
