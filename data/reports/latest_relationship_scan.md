# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T10:52:36.672117+00:00`
- Price records: `672`
- Market context records: `3782`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13040`

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

- `risk_on_high->crypto_major_24h` score `30.267` n `32` status `ready` deltaP `32.1181` edge `2.3124` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.267` n `32` status `ready` deltaP `32.1181` edge `2.3124` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.5978` n `32` status `ready` deltaP `39.0625` edge `1.7894` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.5978` n `32` status `ready` deltaP `39.0625` edge `1.7894` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.8591` n `32` status `ready` deltaP `31.9444` edge `1.7071` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.8591` n `32` status `ready` deltaP `31.9444` edge `1.7071` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5456` n `32` status `ready` deltaP `31.25` edge `0.7538` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5456` n `32` status `ready` deltaP `31.25` edge `0.7538` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0577` n `32` status `ready` deltaP `17.5305` edge `0.8335` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0577` n `32` status `ready` deltaP `17.5305` edge `0.8335` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.6482` n `157` status `ready` deltaP `19.3173` edge `0.7` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.3755` n `157` status `ready` deltaP `26.7914` edge `0.3833` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `5.0184` n `157` status `ready` deltaP `7.8546` edge `0.8122` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.5195` n `157` status `ready` deltaP `27.0148` edge `0.3397` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.0104` n `169` status `ready` deltaP `10.319` edge `0.2888` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.468` n `32` status `ready` deltaP `8.003` edge `0.2483` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.468` n `32` status `ready` deltaP `8.003` edge `0.2483` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4241` n `32` status `ready` deltaP `14.2361` edge `0.0499` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4241` n `32` status `ready` deltaP `14.2361` edge `0.0499` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.1948` n `169` status `ready` deltaP `9.8336` edge `0.2044` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
