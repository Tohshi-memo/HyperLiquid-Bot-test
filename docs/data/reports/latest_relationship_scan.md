# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T18:37:29.910265+00:00`
- Price records: `672`
- Market context records: `5584`
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

- `market_context_high->equity_24h` score `3.9895` n `174` status `ready` deltaP `15.0084` edge `0.7403` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.1814` n `199` status `ready` deltaP `11.5494` edge `0.2507` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.95` n `174` status `ready` deltaP `18.4866` edge `0.0533` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.5873` n `199` status `ready` deltaP `7.0382` edge `0.1661` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.5776` n `199` status `ready` deltaP `6.0447` edge `0.1717` maxDD `-7.4425`
- `market_context_high->crypto_major_24h` score `0.4661` n `174` status `ready` deltaP `13.1047` edge `0.4055` maxDD `-29.6555`
- `market_context_high->equity_1h` score `-0.1831` n `211` status `ready` deltaP `6.1221` edge `0.0364` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2146` n `211` status `ready` deltaP `3.5786` edge `0.0076` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3103` n `211` status `ready` deltaP `0.9351` edge `0.0008` maxDD `-0.4122`
- `market_context_high->crypto_major_1h` score `-0.4592` n `211` status `ready` deltaP `3.0557` edge `0.0453` maxDD `-6.9639`
- `market_context_high->fx_4h` score `-0.5022` n `199` status `ready` deltaP `4.6613` edge `0.0088` maxDD `-0.8712`
- `market_context_high->metal_1h` score `-0.5506` n `211` status `ready` deltaP `-0.5364` edge `0.0005` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6434` n `211` status `ready` deltaP `0.5605` edge `0.0388` maxDD `-5.0257`
- `market_context_high->commodity_1h` score `-1.2275` n `211` status `ready` deltaP `-2.557` edge `-0.0087` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.534` n `199` status `ready` deltaP `2.7132` edge `0.015` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.152` n `174` status `ready` deltaP `11.9971` edge `0.0428` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0069` n `199` status `ready` deltaP `-13.0117` edge `-0.0604` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2897` n `199` status `ready` deltaP `-6.0784` edge `-0.0494` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.9685` n `174` status `ready` deltaP `-8.3273` edge `-0.23` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.6244` n `174` status `ready` deltaP `2.8915` edge `0.0484` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
