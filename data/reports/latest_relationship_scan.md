# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T09:37:27.286451+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9733`

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

- `risk_on_high->commodity_24h` score `7.9327` n `54` status `ready` deltaP `41.2892` edge `0.3858` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9327` n `54` status `ready` deltaP `41.2892` edge `0.3858` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.6789` n `121` status `ready` deltaP `18.7235` edge `0.6595` maxDD `-9.2196`
- `risk_on_high->crypto_alt_4h` score `6.7615` n `54` status `ready` deltaP `22.5497` edge `0.4578` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.7615` n `54` status `ready` deltaP `22.5497` edge `0.4578` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.062` n `121` status `ready` deltaP `19.9909` edge `0.5278` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.6826` n `54` status `ready` deltaP `34.5303` edge `0.4554` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6826` n `54` status `ready` deltaP `34.5303` edge `0.4554` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8231` n `123` status `ready` deltaP `13.4791` edge `0.1685` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1148` n `123` status `ready` deltaP `5.3491` edge `0.1378` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0844` n `121` status `ready` deltaP `11.0046` edge `0.0382` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3188` n `54` status `ready` deltaP `1.1034` edge `0.024` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3188` n `54` status `ready` deltaP `1.1034` edge `0.024` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3356` n `54` status `ready` deltaP `4.8071` edge `0.0272` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3356` n `54` status `ready` deltaP `4.8071` edge `0.0272` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3569` n `123` status `ready` deltaP `-0.8204` edge `-0.0019` maxDD `-0.4047`
- `market_context_high->commodity_24h` score `-0.4335` n `116` status `ready` deltaP `12.8409` edge `0.1473` maxDD `-12.0788`
- `market_context_high->metal_1h` score `-0.4736` n `123` status `ready` deltaP `6.3118` edge `0.0054` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4913` n `54` status `ready` deltaP `1.2531` edge `0.0018` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4913` n `54` status `ready` deltaP `1.2531` edge `0.0018` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
