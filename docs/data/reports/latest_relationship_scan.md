# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T18:22:25.607630+00:00`
- Price records: `672`
- Market context records: `5583`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11423`

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

- `market_context_high->equity_24h` score `4.0195` n `174` status `ready` deltaP `15.0084` edge `0.7428` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.1747` n `198` status `ready` deltaP `11.5114` edge `0.2504` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.9325` n `174` status `ready` deltaP `18.313` edge `0.053` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.5874` n `198` status `ready` deltaP `6.9952` edge `0.1664` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.563` n `198` status `ready` deltaP `5.862` edge `0.1717` maxDD `-7.4425`
- `market_context_high->crypto_major_24h` score `0.5093` n `174` status `ready` deltaP `13.1047` edge `0.4091` maxDD `-29.6555`
- `market_context_high->index_1h` score `-0.1905` n `210` status `ready` deltaP `3.8495` edge `0.0078` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.1932` n `210` status `ready` deltaP `5.9439` edge `0.0363` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.3144` n `210` status `ready` deltaP `0.8569` edge `0.0008` maxDD `-0.4122`
- `market_context_high->fx_4h` score `-0.4388` n `198` status `ready` deltaP `4.8134` edge `0.0089` maxDD `-0.8712`
- `market_context_high->crypto_major_1h` score `-0.4757` n `210` status `ready` deltaP `2.8301` edge `0.0447` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5375` n `210` status `ready` deltaP `-0.2994` edge `0.0006` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6374` n `210` status `ready` deltaP `0.6658` edge `0.0386` maxDD `-5.0257`
- `market_context_high->commodity_1h` score `-1.2211` n `210` status `ready` deltaP `-2.4765` edge `-0.0087` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5391` n `198` status `ready` deltaP `2.65` edge `0.015` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.1336` n `174` status `ready` deltaP `12.1707` edge `0.044` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0251` n `198` status `ready` deltaP `-13.3315` edge `-0.0606` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2921` n `198` status `ready` deltaP `-6.0329` edge `-0.0499` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.9623` n `174` status `ready` deltaP `-8.3273` edge `-0.2292` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.574` n `174` status `ready` deltaP `2.8915` edge `0.0526` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
