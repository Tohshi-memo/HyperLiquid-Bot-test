# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T09:22:31.196579+00:00`
- Price records: `672`
- Market context records: `7655`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14697`

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

- `market_context_high->index_1h` score `0.0508` n `146` status `ready` deltaP `6.512` edge `0.011` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.19` n `146` status `ready` deltaP `7.8562` edge `0.0193` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2895` n `146` status `ready` deltaP `1.456` edge `0.0164` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3563` n `145` status `ready` deltaP `9.2803` edge `0.0172` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4069` n `146` status `ready` deltaP `1.378` edge `-0.0043` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5423` n `146` status `ready` deltaP `5.0764` edge `0.048` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6481` n `146` status `ready` deltaP `0.9392` edge `0.0152` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7104` n `146` status `ready` deltaP `1.6066` edge `0.0046` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.723` n `146` status `ready` deltaP `7.6871` edge `0.0262` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7422` n `146` status `ready` deltaP `-1.4727` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-0.9217` n `145` status `ready` deltaP `8.3612` edge `0.0258` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.115` n `146` status `ready` deltaP `1.9775` edge `0.0428` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1869` n `146` status `ready` deltaP `9.2841` edge `0.0537` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.5014` n `146` status `ready` deltaP `-0.9843` edge `-0.0562` maxDD `-1.3217`
- `market_context_high->equity_24h` score `-1.653` n `145` status `ready` deltaP `14.0154` edge `0.1852` maxDD `-34.5784`
- `market_context_high->metal_4h` score `-1.7068` n `146` status `ready` deltaP `-2.7376` edge `0.0451` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.723` n `146` status `ready` deltaP `0.6849` edge `0.1889` maxDD `-20.4824`
- `market_context_high->metal_24h` score `-2.245` n `146` status `ready` deltaP `-3.2772` edge `0.0597` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.7546` n `146` status `ready` deltaP `-8.3407` edge `-0.0055` maxDD `-2.1425`
- `market_context_high->unknown_24h` score `-3.0157` n `146` status `ready` deltaP `5.2821` edge `-0.1685` maxDD `-4.775`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
