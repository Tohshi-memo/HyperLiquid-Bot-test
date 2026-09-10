# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T14:37:29.452842+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11958`

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

- `risk_on_high->crypto_alt_24h` score `18.6824` n `91` status `ready` deltaP `36.1722` edge `1.3387` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.6824` n `91` status `ready` deltaP `36.1722` edge `1.3387` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.0937` n `201` status `ready` deltaP `27.7364` edge `1.0723` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.8463` n `91` status `ready` deltaP `42.0983` edge `0.4937` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8463` n `91` status `ready` deltaP `42.0983` edge `0.4937` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.4097` n `91` status `ready` deltaP `31.8966` edge `0.4907` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.4097` n `91` status `ready` deltaP `31.8966` edge `0.4907` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.847` n `91` status `ready` deltaP `25.021` edge `1.1178` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.847` n `91` status `ready` deltaP `25.021` edge `1.1178` maxDD `-24.5429`
- `market_context_high->equity_24h` score `4.4383` n `201` status `ready` deltaP `21.3542` edge `0.2275` maxDD `0.0`
- `risk_on_high->index_24h` score `3.692` n `91` status `ready` deltaP `37.1547` edge `0.0642` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.692` n `91` status `ready` deltaP `37.1547` edge `0.0642` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `2.8447` n `91` status `ready` deltaP `21.3542` edge `0.0947` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.8447` n `91` status `ready` deltaP `21.3542` edge `0.0947` maxDD `0.0`
- `market_context_high->index_24h` score `2.8203` n `201` status `ready` deltaP `31.4962` edge `0.0644` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.7925` n `91` status `ready` deltaP `28.9249` edge `0.0492` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.7925` n `91` status `ready` deltaP `28.9249` edge `0.0492` maxDD `-0.0796`
- `market_context_high->equity_4h` score `1.6668` n `201` status `ready` deltaP `22.0855` edge `0.0772` maxDD `-2.843`
- `market_context_high->commodity_24h` score `1.4405` n `201` status `ready` deltaP `16.1951` edge `0.026` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.4244` n `91` status `ready` deltaP `15.8616` edge `0.0223` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
