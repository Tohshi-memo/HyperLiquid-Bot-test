# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T09:07:31.285053+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14747`

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

- `news_risk_high->unknown_24h` score `50.7137` n `50` status `ready` deltaP `11.5717` edge `4.149` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.5164` n `50` status `ready` deltaP `37.6235` edge `1.253` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.604` n `50` status `ready` deltaP `26.4695` edge `0.8838` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.9981` n `50` status `ready` deltaP `25.6235` edge `0.3385` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0101` n `50` status `ready` deltaP `46.7256` edge `0.0317` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.7055` n `50` status `ready` deltaP `41.8687` edge `0.0339` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.5734` n `130` status `ready` deltaP `24.7772` edge `0.1733` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.8748` n `50` status `ready` deltaP `16.2275` edge `0.167` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.8046` n `50` status `ready` deltaP `30.6598` edge `0.0444` maxDD `-0.2064`
- `news_risk_high->fx_1h` score `1.5204` n `50` status `ready` deltaP `20.3533` edge `0.008` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.4856` n `133` status `ready` deltaP `12.1673` edge `0.0877` maxDD `-1.6015`
- `market_context_high->unknown_24h` score `1.4853` n `129` status `ready` deltaP `5.3701` edge `0.1612` maxDD `-3.1917`
- `news_risk_high->equity_1h` score `1.1547` n `50` status `ready` deltaP `16.3653` edge `0.015` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.0091` n `50` status `ready` deltaP `19.1402` edge `0.0328` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.6047` n `50` status `ready` deltaP `15.6467` edge `0.0045` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1172` n `50` status `ready` deltaP `7.2096` edge `0.0009` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0835` n `50` status `ready` deltaP `5.2515` edge `-0.0017` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.0139` n `50` status `ready` deltaP `5.7134` edge `0.0004` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2688` n `50` status `ready` deltaP `6.0915` edge `-0.0099` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4903` n `133` status `ready` deltaP `1.7368` edge `-0.0012` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
