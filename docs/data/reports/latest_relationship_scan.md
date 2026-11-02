# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T08:07:28.817545+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4843`

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

- `market_context_high->unknown_24h` score `5497.7551` n `30` status `ready` deltaP `1.3889` edge `458.137` maxDD `0.0`
- `market_context_high->unknown_4h` score `703.2209` n `35` status `ready` deltaP `8.8415` edge `58.5428` maxDD `0.0`
- `market_context_high->unknown_1h` score `189.1991` n `35` status `ready` deltaP `7.2969` edge `15.729` maxDD `-0.2178`
- `market_context_high->equity_24h` score `20.1148` n `30` status `ready` deltaP `41.2848` edge `1.4246` maxDD `-1.5546`
- `market_context_high->commodity_24h` score `7.3097` n `30` status `ready` deltaP `41.2847` edge `0.365` maxDD `-0.8203`
- `market_context_high->index_24h` score `7.0422` n `30` status `ready` deltaP `49.1319` edge `0.2593` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.6589` n `102` status `ready` deltaP `28.3701` edge `0.9092` maxDD `-15.5698`
- `market_context_high->crypto_alt_4h` score `5.825` n `35` status `ready` deltaP `24.8171` edge `0.3494` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.8246` n `35` status `ready` deltaP `8.8937` edge `0.4963` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `4.5728` n `35` status `ready` deltaP `22.304` edge `0.266` maxDD `-1.6901`
- `market_context_high->equity_1h` score `3.6548` n `35` status `ready` deltaP `12.5577` edge `0.2609` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `2.6715` n `126` status `ready` deltaP `10.6901` edge `0.29` maxDD `-7.4246`
- `market_context_high->index_4h` score `2.6436` n `35` status `ready` deltaP `25.122` edge `0.0755` maxDD `-0.1474`
- `market_context_high->crypto_major_1h` score `2.3855` n `35` status `ready` deltaP `12.7074` edge `0.1531` maxDD `-1.1219`
- `market_context_high->crypto_alt_1h` score `1.592` n `35` status `ready` deltaP `10.5988` edge `0.1776` maxDD `-1.5324`
- `market_context_high->metal_4h` score `1.2908` n `35` status `ready` deltaP `15.4878` edge `0.0468` maxDD `-0.7323`
- `market_context_high->fx_1h` score `1.157` n `35` status `ready` deltaP `15.2652` edge `0.0118` maxDD `-0.0388`
- `market_context_high->commodity_4h` score `1.0225` n `35` status `ready` deltaP `20.7055` edge `0.0343` maxDD `-1.633`
- `market_context_high->crypto_alt_24h` score `0.6564` n `30` status `ready` deltaP `-11.0417` edge `0.2801` maxDD `-8.8096`
- `market_context_high->index_1h` score `0.6266` n `35` status `ready` deltaP `5.9453` edge `0.0367` maxDD `-0.2628`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
