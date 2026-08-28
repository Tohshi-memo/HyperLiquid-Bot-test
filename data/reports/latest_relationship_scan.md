# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T09:22:27.602190+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11608`

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

- `news_risk_high->unknown_24h` score `53.2489` n `50` status `ready` deltaP `11.6118` edge `4.36` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.054` n `50` status `ready` deltaP `38.8076` edge `2.2899` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.8008` n `50` status `ready` deltaP `25.5549` edge `0.9063` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.4271` n `50` status `ready` deltaP `30.1005` edge `0.3444` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.1617` n `50` status `ready` deltaP `48.0867` edge `0.1138` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9467` n `50` status `ready` deltaP `45.9634` edge `0.0315` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `2.857` n `133` status `ready` deltaP `5.5968` edge `0.274` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.7128` n `52` status `ready` deltaP `15.5228` edge `0.1582` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.5715` n `50` status `ready` deltaP `28.9012` edge `0.0367` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3592` n `147` status `ready` deltaP `18.6297` edge `0.1131` maxDD `-0.5894`
- `news_risk_high->crypto_major_24h` score `2.1664` n `50` status `ready` deltaP `18.4887` edge `0.1066` maxDD `-2.6128`
- `news_risk_high->equity_4h` score `1.7999` n `50` status `ready` deltaP `23.8659` edge `0.0672` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.5689` n `52` status `ready` deltaP `21.0041` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2728` n `52` status `ready` deltaP `16.8125` edge `0.0222` maxDD `-0.2574`
- `market_context_high->unknown_1h` score `0.8718` n `147` status `ready` deltaP `8.7854` edge `0.0591` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5178` n `52` status `ready` deltaP `14.3597` edge `0.0024` maxDD `-0.5397`
- `market_context_high->metal_24h` score `0.3187` n `133` status `ready` deltaP `14.7484` edge `0.0865` maxDD `-3.6609`
- `news_risk_high->metal_4h` score `0.292` n `50` status `ready` deltaP `11.122` edge `0.0033` maxDD `-0.249`
- `news_risk_high->index_4h` score `0.1334` n `50` status `ready` deltaP `7.3902` edge `0.0015` maxDD `-0.1719`
- `news_risk_high->metal_1h` score `0.072` n `52` status `ready` deltaP `4.7444` edge `0.0002` maxDD `-0.1413`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
