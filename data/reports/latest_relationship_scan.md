# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T17:33:39.336454+00:00`
- Price records: `672`
- Market context records: `3503`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13142`

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

- `risk_on_high->crypto_major_24h` score `54.1596` n `32` status `ready` deltaP `57.8802` edge `4.1317` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `54.1596` n `32` status `ready` deltaP `57.8802` edge `4.1317` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `50.7914` n `32` status `ready` deltaP `57.5336` edge `3.8642` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `50.7914` n `32` status `ready` deltaP `57.5336` edge `3.8642` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.3203` n `32` status `ready` deltaP `54.9393` edge `3.3271` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.3203` n `32` status `ready` deltaP `54.9393` edge `3.3271` maxDD `0.0`
- `risk_on_high->index_24h` score `24.3183` n `32` status `ready` deltaP `50.4333` edge `1.6903` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.3183` n `32` status `ready` deltaP `50.4333` edge `1.6903` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `18.964` n `155` status `ready` deltaP `23.5858` edge `2.1962` maxDD `-54.8486`
- `market_context_high->equity_24h` score `18.7329` n `155` status `ready` deltaP `31.7135` edge `1.9909` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `16.8845` n `155` status `ready` deltaP `18.078` edge `2.0866` maxDD `-56.6728`
- `risk_on_high->metal_24h` score `16.335` n `32` status `ready` deltaP `32.0082` edge `1.174` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.335` n `32` status `ready` deltaP `32.0082` edge `1.174` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `14.7724` n `32` status `ready` deltaP `27.6541` edge `1.1589` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.7724` n `32` status `ready` deltaP `27.6541` edge `1.1589` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.9448` n `155` status `ready` deltaP `34.9494` edge `1.0674` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.1108` n `32` status `ready` deltaP `8.8328` edge `0.7181` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.1108` n `32` status `ready` deltaP `8.8328` edge `0.7181` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.1912` n `155` status `ready` deltaP `26.484` edge `1.0712` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.8687` n `32` status `ready` deltaP `16.3099` edge `0.5007` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
