# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T07:52:31.094340+00:00`
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

- `risk_on_high->crypto_alt_24h` score `14.6565` n `91` status `ready` deltaP `31.6583` edge `1.0333` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `14.6565` n `91` status `ready` deltaP `31.6583` edge `1.0333` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `10.6768` n `209` status `ready` deltaP `23.7557` edge `0.8141` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.5334` n `91` status `ready` deltaP `38.2873` edge `0.4097` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.5334` n `91` status `ready` deltaP `38.2873` edge `0.4097` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.6313` n `91` status `ready` deltaP `28.0857` edge `0.3679` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.6313` n `91` status `ready` deltaP `28.0857` edge `0.3679` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.2692` n `91` status `ready` deltaP `20.5071` edge `0.8174` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.2692` n `91` status `ready` deltaP `20.5071` edge `0.8174` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.9486` n `91` status `ready` deltaP `32.4672` edge `0.0335` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9486` n `91` status `ready` deltaP `32.4672` edge `0.0335` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.7457` n `209` status `ready` deltaP `16.6667` edge `0.1177` maxDD `0.0`
- `market_context_high->index_24h` score `2.4259` n `209` status `ready` deltaP `27.1515` edge `0.0605` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.9519` n `91` status `ready` deltaP `18.4657` edge `0.0489` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.9519` n `91` status `ready` deltaP `18.4657` edge `0.0489` maxDD `-0.0811`
- `risk_on_high->equity_4h` score `1.8459` n `91` status `ready` deltaP `25.4188` edge `-0.0063` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `1.8459` n `91` status `ready` deltaP `25.4188` edge `-0.0063` maxDD `-0.0802`
- `risk_on_high->equity_1h` score `1.1318` n `91` status `ready` deltaP `17.8901` edge `0.0029` maxDD `-0.228`
- `risk_on_and_context->equity_1h` score `1.1318` n `91` status `ready` deltaP `17.8901` edge `0.0029` maxDD `-0.228`
- `risk_on_high->crypto_alt_1h` score `1.1316` n `91` status `ready` deltaP `4.7` edge `0.0982` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
