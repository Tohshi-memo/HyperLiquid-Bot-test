# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T17:52:22.161537+00:00`
- Price records: `672`
- Market context records: `2164`
- Flow alert records: `8125`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `13.1517` n `138` status `ready` deltaP `36.9918` edge `0.943` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7288` n `138` status `ready` deltaP `41.2645` edge `0.7553` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5881` n `138` status `ready` deltaP `23.3387` edge `0.385` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `3.9779` n `43` status `ready` deltaP `32.4624` edge `0.3607` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.8765` n `138` status `ready` deltaP `24.5692` edge `0.2687` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.219` n `138` status `ready` deltaP `17.439` edge `0.1997` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.1225` n `138` status `ready` deltaP `16.0917` edge `0.2393` maxDD `-4.9097`
- `market_context_high->index_24h` score `3.0376` n `138` status `ready` deltaP `12.1905` edge `0.2947` maxDD `-4.1604`
- `market_context_high->index_4h` score `2.935` n `138` status `ready` deltaP `23.1972` edge `0.1583` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.6716` n `138` status `ready` deltaP `27.5665` edge `0.5709` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `2.2499` n `138` status `ready` deltaP `19.9728` edge `1.013` maxDD `-62.2831`
- `market_context_high->equity_24h` score `2.1069` n `138` status `ready` deltaP `23.913` edge `0.506` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `2.0491` n `43` status `ready` deltaP `26.2124` edge `0.0144` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.8641` n `138` status `ready` deltaP `18.8383` edge `0.1685` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.5273` n `43` status `ready` deltaP `15.8395` edge `0.094` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.4315` n `43` status `ready` deltaP `-2.0739` edge `0.3181` maxDD `-4.6598`
- `news_risk_high->unknown_1h` score `1.3207` n `43` status `ready` deltaP `21.3445` edge `0.0147` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.8329` n `43` status `ready` deltaP `10.9142` edge `0.102` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.5225` n `138` status `ready` deltaP `10.1818` edge `0.0545` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.5001` n `138` status `ready` deltaP `8.9951` edge `0.0487` maxDD `-2.3594`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
