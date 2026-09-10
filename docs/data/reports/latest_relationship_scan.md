# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T14:52:26.371070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11844`

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

- `risk_on_high->crypto_alt_24h` score `18.7544` n `91` status `ready` deltaP `36.1722` edge `1.3447` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.7544` n `91` status `ready` deltaP `36.1722` edge `1.3447` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.1657` n `201` status `ready` deltaP `27.7364` edge `1.0783` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.8993` n `91` status `ready` deltaP `42.2507` edge `0.4971` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8993` n `91` status `ready` deltaP `42.2507` edge `0.4971` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.4675` n `91` status `ready` deltaP `32.0491` edge `0.4945` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.4675` n `91` status `ready` deltaP `32.0491` edge `0.4945` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.8774` n `91` status `ready` deltaP `25.021` edge `1.1217` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.8774` n `91` status `ready` deltaP `25.021` edge `1.1217` maxDD `-24.5429`
- `market_context_high->equity_24h` score `4.5338` n `201` status `ready` deltaP `21.5278` edge `0.2343` maxDD `0.0`
- `risk_on_high->index_24h` score `3.7191` n `91` status `ready` deltaP `37.3283` edge `0.0653` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.7191` n `91` status `ready` deltaP `37.3283` edge `0.0653` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `2.9402` n `91` status `ready` deltaP `21.5278` edge `0.1015` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.9402` n `91` status `ready` deltaP `21.5278` edge `0.1015` maxDD `0.0`
- `market_context_high->index_24h` score `2.8473` n `201` status `ready` deltaP `31.6698` edge `0.0655` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.8358` n `91` status `ready` deltaP `29.0773` edge `0.0518` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.8358` n `91` status `ready` deltaP `29.0773` edge `0.0518` maxDD `-0.0796`
- `market_context_high->equity_4h` score `1.7102` n `201` status `ready` deltaP `22.2379` edge `0.0798` maxDD `-2.843`
- `market_context_high->commodity_24h` score `1.4158` n `201` status `ready` deltaP `16.0215` edge `0.0251` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.3997` n `91` status `ready` deltaP `15.688` edge `0.0214` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
