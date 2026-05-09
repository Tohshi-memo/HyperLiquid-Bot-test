# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T12:52:12.342551+00:00`
- Price records: `672`
- Market context records: `867`
- Flow alert records: `2434`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `22.3715` n `31` status `ready` deltaP `32.6389` edge `1.6467` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.3715` n `31` status `ready` deltaP `32.6389` edge `1.6467` maxDD `0.0`
- `risk_on_high->equity_24h` score `13.8802` n `31` status `ready` deltaP `25.3472` edge `0.9877` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.8802` n `31` status `ready` deltaP `25.3472` edge `0.9877` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `13.7638` n `31` status `ready` deltaP `7.8125` edge `1.0949` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.7638` n `31` status `ready` deltaP `7.8125` edge `1.0949` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `12.8834` n `165` status `ready` deltaP `28.3965` edge `0.9177` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3305` n `165` status `ready` deltaP `7.2064` edge `0.4843` maxDD `-0.0508`
- `risk_on_high->index_24h` score `4.5521` n `31` status `ready` deltaP `27.9514` edge `0.193` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.5521` n `31` status `ready` deltaP `27.9514` edge `0.193` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4468` n `32` status `ready` deltaP `8.003` edge `0.2704` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4468` n `32` status `ready` deltaP `8.003` edge `0.2704` maxDD `-0.9217`
- `risk_on_high->crypto_alt_4h` score `2.8519` n `32` status `ready` deltaP `21.875` edge `0.1123` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.8519` n `32` status `ready` deltaP `21.875` edge `0.1123` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.7496` n `32` status `ready` deltaP `19.9695` edge `0.1332` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7496` n `32` status `ready` deltaP `19.9695` edge `0.1332` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.5631` n `32` status `ready` deltaP `14.1006` edge `0.1284` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5631` n `32` status `ready` deltaP `14.1006` edge `0.1284` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.7434` n `31` status `ready` deltaP `-7.1236` edge `0.3387` maxDD `-1.7492`
- `risk_on_and_context->commodity_24h` score `1.7434` n `31` status `ready` deltaP `-7.1236` edge `0.3387` maxDD `-1.7492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
