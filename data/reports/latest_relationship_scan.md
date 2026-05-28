# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T18:07:25.277493+00:00`
- Price records: `672`
- Market context records: `2165`
- Flow alert records: `8128`
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

- `market_context_high->crypto_alt_4h` score `13.0556` n `137` status `ready` deltaP `36.8702` edge `0.9358` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7225` n `137` status `ready` deltaP `41.1852` edge `0.7553` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5396` n `137` status `ready` deltaP `23.1218` edge `0.3824` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `3.9615` n `43` status `ready` deltaP `32.4624` edge `0.3586` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.786` n `137` status `ready` deltaP `24.4581` edge `0.2619` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.1931` n `137` status `ready` deltaP `17.1904` edge `0.1992` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.0498` n `137` status `ready` deltaP `15.8431` edge `0.2349` maxDD `-4.9097`
- `market_context_high->index_24h` score `2.9515` n `137` status `ready` deltaP `11.9842` edge `0.2889` maxDD `-4.1604`
- `market_context_high->index_4h` score `2.8842` n `137` status `ready` deltaP `23.0861` edge `0.1548` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.686` n `137` status `ready` deltaP `27.5814` edge `0.572` maxDD `-35.8966`
- `market_context_high->crypto_major_24h` score `2.2689` n `137` status `ready` deltaP `19.8132` edge `1.0165` maxDD `-62.2831`
- `news_risk_high->fx_4h` score `2.0625` n `43` status `ready` deltaP `26.3648` edge `0.0145` maxDD `-0.1382`
- `market_context_high->equity_24h` score `2.0209` n `137` status `ready` deltaP `23.7226` edge `0.5001` maxDD `-33.1875`
- `market_context_high->metal_4h` score `1.7494` n `137` status `ready` deltaP `18.5897` edge `0.1606` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.5321` n `43` status `ready` deltaP `15.8395` edge `0.0944` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.4206` n `43` status `ready` deltaP `-2.0739` edge `0.3167` maxDD `-4.6598`
- `news_risk_high->unknown_1h` score `1.3351` n `43` status `ready` deltaP `21.3445` edge `0.0159` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.8243` n `43` status `ready` deltaP `10.9142` edge `0.1009` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4741` n `43` status `ready` deltaP `8.2892` edge `0.0099` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.4691` n `137` status `ready` deltaP `9.9491` edge `0.0516` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
