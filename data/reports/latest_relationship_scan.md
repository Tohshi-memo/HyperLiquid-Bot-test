# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T00:22:22.171443+00:00`
- Price records: `672`
- Market context records: `3331`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_24h` score `62.3232` n `31` status `ready` deltaP `66.8403` edge `4.748` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `62.3232` n `31` status `ready` deltaP `66.8403` edge `4.748` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `57.4957` n `31` status `ready` deltaP `61.1111` edge `4.3839` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `57.4957` n `31` status `ready` deltaP `61.1111` edge `4.3839` maxDD `0.0`
- `risk_on_high->equity_24h` score `46.8033` n `31` status `ready` deltaP `56.7708` edge `3.5218` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.8033` n `31` status `ready` deltaP `56.7708` edge `3.5218` maxDD `0.0`
- `risk_on_high->index_24h` score `22.9748` n `31` status `ready` deltaP `50.6944` edge `1.5766` maxDD `0.0`
- `risk_on_and_context->index_24h` score `22.9748` n `31` status `ready` deltaP `50.6944` edge `1.5766` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.0289` n `31` status `ready` deltaP `35.2766` edge `1.1267` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0289` n `31` status `ready` deltaP `35.2766` edge `1.1267` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.8579` n `32` status `ready` deltaP `30.1829` edge `1.2325` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8579` n `32` status `ready` deltaP `30.1829` edge `1.2325` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.8909` n `145` status `ready` deltaP `23.1801` edge `2.7387` maxDD `-70.3986`
- `market_context_high->index_24h` score `11.4692` n `145` status `ready` deltaP `34.8323` edge `0.979` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.1809` n `145` status `ready` deltaP `28.4949` edge `1.9569` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.3667` n `32` status `ready` deltaP `9.5274` edge `0.7348` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3667` n `32` status `ready` deltaP `9.5274` edge `0.7348` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5178` n `32` status `ready` deltaP `13.6433` edge `0.4735` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5178` n `32` status `ready` deltaP `13.6433` edge `0.4735` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `3.1826` n `145` status `ready` deltaP `24.7713` edge `2.3128` maxDD `-152.2601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
