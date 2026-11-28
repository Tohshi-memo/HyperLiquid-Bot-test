# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T11:37:34.166535+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `5558`

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

- `news_risk_high->unknown_1h` score `3387.7212` n `31` status `ready` deltaP `2.0813` edge `282.3138` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3262.429` n `31` status `ready` deltaP `3.7864` edge `271.8495` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.0446` n `31` status `ready` deltaP `34.662` edge `1.6893` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.769` n `31` status `ready` deltaP `32.5823` edge `1.1802` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.6429` n `31` status `ready` deltaP `28.0763` edge `0.8664` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.853` n `31` status `ready` deltaP `22.797` edge `0.6728` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.6266` n `31` status `ready` deltaP `17.083` edge `0.7492` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.5573` n `31` status `ready` deltaP `30.6698` edge `0.3067` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0256` n `31` status `ready` deltaP `41.4491` edge `0.1553` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9066` n `31` status `ready` deltaP `16.5204` edge `0.2429` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.494` n `31` status `ready` deltaP `30.5173` edge `0.0304` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3936` n `31` status `ready` deltaP `26.1698` edge `0.025` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3367` n `31` status `ready` deltaP `28.6991` edge `0.0119` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.152` n `31` status `ready` deltaP `14.2988` edge `0.1027` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.9809` n `31` status `ready` deltaP `7.0166` edge `0.2533` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7686` n `31` status `ready` deltaP `9.4118` edge `0.1997` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1154` n `31` status `ready` deltaP `24.3432` edge `0.0086` maxDD `-0.2315`
- `market_context_high->metal_4h` score `0.8352` n `39` status `ready` deltaP `11.6909` edge `0.0328` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4315` n `31` status `ready` deltaP `10.1986` edge `0.0271` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3467` n `31` status `ready` deltaP `11.4427` edge `0.0239` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
