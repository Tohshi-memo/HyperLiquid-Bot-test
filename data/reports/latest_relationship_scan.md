# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T03:07:27.285951+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10938`

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

- `market_context_high->commodity_4h` score `1.3799` n `162` status `ready` deltaP `15.5224` edge `0.0788` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7443` n `174` status `ready` deltaP `10.0988` edge `0.029` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.4896` n `139` status `ready` deltaP `18.7425` edge `0.0213` maxDD `-1.678`
- `market_context_high->fx_1h` score `-0.1941` n `174` status `ready` deltaP `3.8492` edge `-0.001` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.2583` n `162` status `ready` deltaP `5.8755` edge `0.003` maxDD `-1.6892`
- `market_context_high->index_1h` score `-0.6086` n `174` status `ready` deltaP `-3.7666` edge `-0.0052` maxDD `-0.8168`
- `market_context_high->index_24h` score `-0.6181` n `139` status `ready` deltaP `2.1507` edge `0.0873` maxDD `-5.9181`
- `market_context_high->metal_1h` score `-0.8245` n `174` status `ready` deltaP `-4.6648` edge `-0.011` maxDD `-2.0884`
- `market_context_high->index_4h` score `-0.852` n `162` status `ready` deltaP `-3.0112` edge `-0.0109` maxDD `-1.26`
- `market_context_high->equity_1h` score `-0.8848` n `174` status `ready` deltaP `-2.8821` edge `-0.0072` maxDD `-4.6286`
- `market_context_high->metal_24h` score `-1.2879` n `139` status `ready` deltaP `-3.8507` edge `0.0288` maxDD `-2.503`
- `market_context_high->equity_24h` score `-1.3239` n `139` status `ready` deltaP `-1.2953` edge `0.2043` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5721` n `174` status `ready` deltaP `-9.1851` edge `-0.0382` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.8821` n `162` status `ready` deltaP `-7.4243` edge `-0.0363` maxDD `-5.7738`
- `market_context_high->equity_4h` score `-2.5045` n `162` status `ready` deltaP `-6.8146` edge `-0.0961` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.608` n `174` status `ready` deltaP `-10.393` edge `-0.058` maxDD `-10.5372`
- `market_context_high->crypto_alt_24h` score `-4.3445` n `139` status `ready` deltaP `-10.8951` edge `-0.1451` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7674` n `139` status `ready` deltaP `-1.7936` edge `-0.1359` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-6.3865` n `162` status `ready` deltaP `-13.1776` edge `-0.1686` maxDD `-15.3937`
- `market_context_high->unknown_1h` score `-7.4079` n `174` status `ready` deltaP `-4.1727` edge `-0.5438` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
