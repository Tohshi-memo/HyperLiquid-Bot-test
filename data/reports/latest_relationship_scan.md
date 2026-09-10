# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T07:22:27.433974+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10942`

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

- `risk_on_high->crypto_alt_24h` score `14.3599` n `91` status `ready` deltaP `31.3111` edge `1.0109` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `14.3599` n `91` status `ready` deltaP `31.3111` edge `1.0109` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `10.4732` n `211` status `ready` deltaP `23.5355` edge `0.7986` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.4754` n `91` status `ready` deltaP `37.9824` edge `0.4069` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.4754` n `91` status `ready` deltaP `37.9824` edge `0.4069` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.5697` n `91` status `ready` deltaP `27.7808` edge `0.3648` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.5697` n `91` status `ready` deltaP `27.7808` edge `0.3648` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.0631` n `91` status `ready` deltaP `20.1599` edge `0.7933` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.0631` n `91` status `ready` deltaP `20.1599` edge `0.7933` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.9004` n `91` status `ready` deltaP `32.12` edge `0.0318` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9004` n `91` status `ready` deltaP `32.12` edge `0.0318` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.7264` n `211` status `ready` deltaP `16.3194` edge `0.1184` maxDD `0.0`
- `market_context_high->index_24h` score `2.4142` n `211` status `ready` deltaP `26.8859` edge `0.0613` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.9543` n `91` status `ready` deltaP `18.4657` edge `0.0491` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.9543` n `91` status `ready` deltaP `18.4657` edge `0.0491` maxDD `-0.0811`
- `risk_on_high->equity_4h` score `1.8823` n `91` status `ready` deltaP `25.7237` edge `-0.0053` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `1.8823` n `91` status `ready` deltaP `25.7237` edge `-0.0053` maxDD `-0.0802`
- `risk_on_high->equity_1h` score `1.1007` n `91` status `ready` deltaP `17.5907` edge `0.0023` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.1007` n `91` status `ready` deltaP `17.5907` edge `0.0023` maxDD `-0.228`
- `risk_on_high->crypto_alt_1h` score `1.0812` n `91` status `ready` deltaP `4.4006` edge `0.096` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
