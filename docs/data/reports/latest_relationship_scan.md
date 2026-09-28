# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T02:52:35.561059+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7628`

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

- `news_risk_high->unknown_24h` score `591.2244` n `139` status `ready` deltaP `1.2153` edge `49.2606` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `2.0494` n `139` status `ready` deltaP `14.1849` edge `0.4714` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.6245` n `139` status `ready` deltaP `18.72` edge `0.0801` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.8994` n `139` status `ready` deltaP `20.3013` edge `0.1251` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.3936` n `139` status `ready` deltaP `17.57` edge `0.0766` maxDD `-9.2079`
- `news_risk_high->crypto_alt_1h` score `0.0714` n `139` status `ready` deltaP `4.7721` edge `0.0652` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.0443` n `139` status `ready` deltaP `4.1109` edge `0.0053` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.0075` n `139` status `ready` deltaP `4.2606` edge `0.0371` maxDD `-1.957`
- `news_risk_high->equity_24h` score `-0.0934` n `139` status `ready` deltaP `13.0882` edge `0.1606` maxDD `-11.1179`
- `news_risk_high->metal_1h` score `-0.631` n `139` status `ready` deltaP `0.4426` edge `0.0074` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.9459` n `139` status `ready` deltaP `-0.6591` edge `0.0109` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.9995` n `139` status `ready` deltaP `-2.6968` edge `0.0181` maxDD `-7.2607`
- `news_risk_high->crypto_major_24h` score `-1.1033` n `139` status `ready` deltaP `9.616` edge `0.2874` maxDD `-26.1424`
- `news_risk_high->fx_4h` score `-1.1424` n `139` status `ready` deltaP `11.354` edge `-0.0008` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.1492` n `139` status `ready` deltaP `-8.519` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->crypto_alt_4h` score `-1.3499` n `139` status `ready` deltaP `3.0104` edge `0.1334` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.7816` n `139` status `ready` deltaP `-13.272` edge `0.0095` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9695` n `139` status `ready` deltaP `-10.968` edge `-0.0119` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.3101` n `139` status `ready` deltaP `-11.1884` edge `-0.0783` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5362` n `139` status `ready` deltaP `-8.8832` edge `0.0064` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
