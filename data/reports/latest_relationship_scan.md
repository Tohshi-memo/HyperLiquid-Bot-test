# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T05:52:27.734473+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10930`

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

- `risk_on_high->crypto_alt_24h` score `13.7599` n `95` status `ready` deltaP `30.5007` edge `0.9663` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.7599` n `95` status `ready` deltaP `30.5007` edge `0.9663` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.896` n `217` status `ready` deltaP `22.8607` edge `0.755` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2454` n `95` status `ready` deltaP `37.2673` edge `0.3925` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2454` n `95` status `ready` deltaP `37.2673` edge `0.3925` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.1967` n `95` status `ready` deltaP `26.5084` edge `0.3422` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.1967` n `95` status `ready` deltaP `26.5084` edge `0.3422` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `4.5158` n `95` status `ready` deltaP `20.6451` edge `0.8481` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `4.5158` n `95` status `ready` deltaP `20.6451` edge `0.8481` maxDD `-24.5429`
- `risk_on_high->index_24h` score `2.9062` n `95` status `ready` deltaP `31.2171` edge `0.0383` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9062` n `95` status `ready` deltaP `31.2171` edge `0.0383` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.6622` n `217` status `ready` deltaP `15.2778` edge `0.12` maxDD `0.0`
- `market_context_high->index_24h` score `2.3726` n `217` status `ready` deltaP `26.0801` edge `0.0632` maxDD `-0.1483`
- `risk_on_high->commodity_24h` score `1.4186` n `95` status `ready` deltaP `14.2781` edge `0.0417` maxDD `-0.16`
- `risk_on_and_context->commodity_24h` score `1.4186` n `95` status `ready` deltaP `14.2781` edge `0.0417` maxDD `-0.16`
- `risk_on_high->equity_4h` score `1.2913` n `95` status `ready` deltaP `22.7054` edge `-0.0151` maxDD `-0.9594`
- `risk_on_and_context->equity_4h` score `1.2913` n `95` status `ready` deltaP `22.7054` edge `-0.0151` maxDD `-0.9594`
- `risk_on_high->crypto_alt_1h` score `1.1352` n `95` status `ready` deltaP `4.7605` edge `0.0981` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1352` n `95` status `ready` deltaP `4.7605` edge `0.0981` maxDD `-1.1521`
- `risk_on_high->equity_1h` score `1.0692` n `95` status `ready` deltaP `17.1069` edge `0.0029` maxDD `-0.228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
