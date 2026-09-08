# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-08T05:52:27.789965+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10297`

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

- `market_context_high->unknown_24h` score `86.6796` n `241` status `ready` deltaP `16.184` edge `7.1206` maxDD `-0.0819`
- `risk_on_high->unknown_24h` score `57.3711` n `117` status `ready` deltaP `17.0139` edge `4.6675` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `57.3711` n `117` status `ready` deltaP `17.0139` edge `4.6675` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `8.5536` n `117` status `ready` deltaP `21.9418` edge `0.5895` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `8.5536` n `117` status `ready` deltaP `21.9418` edge `0.5895` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.852` n `117` status `ready` deltaP `31.5497` edge `0.3145` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.852` n `117` status `ready` deltaP `31.5497` edge `0.3145` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `5.066` n `117` status `ready` deltaP `21.1005` edge `0.9156` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.066` n `117` status `ready` deltaP `21.1005` edge `0.9156` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.8787` n `117` status `ready` deltaP `26.1335` edge `0.3182` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.8787` n `117` status `ready` deltaP `26.1335` edge `0.3182` maxDD `-3.8693`
- `market_context_high->crypto_alt_24h` score `3.5061` n `241` status `ready` deltaP `14.597` edge `0.2776` maxDD `-3.9523`
- `risk_on_high->crypto_alt_1h` score `1.0053` n `117` status `ready` deltaP `4.097` edge `0.0917` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0053` n `117` status `ready` deltaP `4.097` edge `0.0917` maxDD `-1.1521`
- `risk_on_high->index_24h` score `0.8562` n `117` status `ready` deltaP `9.7623` edge `0.0105` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `0.8562` n `117` status `ready` deltaP `9.7623` edge `0.0105` maxDD `-0.0051`
- `risk_on_high->equity_1h` score `0.5971` n `117` status `ready` deltaP `15.1211` edge `0.0021` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.5971` n `117` status `ready` deltaP `15.1211` edge `0.0021` maxDD `-2.2516`
- `market_context_high->equity_24h` score `0.5038` n `241` status `ready` deltaP `7.8125` edge `-0.0101` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `0.3656` n `117` status `ready` deltaP `4.6331` edge `0.0723` maxDD `-3.1509`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
