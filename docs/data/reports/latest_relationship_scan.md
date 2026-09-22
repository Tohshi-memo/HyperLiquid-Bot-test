# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T14:37:36.192425+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9930`

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

- `market_context_high->unknown_4h` score `46.6952` n `46` status `ready` deltaP `7.1646` edge `3.8435` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.7921` n `46` status `ready` deltaP `15.6175` edge `2.4775` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.1948` n `46` status `ready` deltaP `12.3189` edge `1.2775` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `16.012` n `46` status `ready` deltaP `14.9306` edge `1.2348` maxDD `0.0`
- `market_context_high->index_24h` score `5.5344` n `46` status `ready` deltaP `20.1314` edge `0.3357` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.2458` n `101` status `ready` deltaP `38.8218` edge `0.2879` maxDD `-3.4467`
- `news_risk_high->crypto_major_24h` score `3.075` n `101` status `ready` deltaP `-9.7377` edge `1.007` maxDD `-46.1999`
- `news_risk_high->crypto_alt_4h` score `2.2093` n `101` status `ready` deltaP `11.6019` edge `0.2277` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.0531` n `101` status `ready` deltaP `12.938` edge `0.1314` maxDD `-2.058`
- `market_context_high->index_4h` score `1.9056` n `46` status `ready` deltaP `22.5543` edge `0.0218` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.5305` n `101` status `ready` deltaP `14.1934` edge `0.1587` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.3278` n `101` status `ready` deltaP `14.2853` edge `0.0677` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `1.0794` n `101` status `ready` deltaP `17.4822` edge `0.037` maxDD `-0.421`
- `market_context_high->metal_24h` score `0.9937` n `46` status `ready` deltaP `22.0939` edge `-0.0411` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.9192` n `46` status `ready` deltaP `7.2243` edge `0.0591` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.7885` n `46` status `ready` deltaP `7.062` edge `0.0429` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.6538` n `46` status `ready` deltaP `7.2971` edge `0.0653` maxDD `-2.7574`
- `market_context_high->index_1h` score `0.6303` n `46` status `ready` deltaP `10.2057` edge `0.0098` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5693` n `101` status `ready` deltaP `14.2986` edge `0.0123` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.4467` n `101` status `ready` deltaP `18.2841` edge `0.0198` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
