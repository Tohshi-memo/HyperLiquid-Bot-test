# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T14:07:30.160950+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4296`

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

- `market_context_high->unknown_1h` score `32301.6507` n `45` status `ready` deltaP `1.5668` edge `2691.8032` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22117.3266` n `45` status `ready` deltaP `2.5678` edge `1843.1073` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1092.1213` n `31` status `ready` deltaP `1.7819` edge `91.0158` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `881.9735` n `31` status `ready` deltaP `3.7864` edge `73.4782` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `36.3216` n `31` status `ready` deltaP `49.3056` edge `2.6981` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.445` n `31` status `ready` deltaP `40.2778` edge `2.6019` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.5084` n `31` status `ready` deltaP `46.875` edge `2.3132` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.1122` n `31` status `ready` deltaP `41.2355` edge `0.6786` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.98` n `31` status `ready` deltaP `24.1689` edge `0.8409` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.2285` n `31` status `ready` deltaP `32.499` edge `0.6006` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.7756` n `31` status `ready` deltaP `15.2537` edge `0.9087` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.5962` n `31` status `ready` deltaP `55.4268` edge `0.193` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.057` n `31` status `ready` deltaP `37.8472` edge `0.1691` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4903` n `31` status `ready` deltaP `18.7898` edge `0.1843` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9461` n `45` status `ready` deltaP `35.5759` edge `0.0368` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.8964` n `31` status `ready` deltaP `31.7369` edge `0.0558` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.6433` n `31` status `ready` deltaP `11.9567` edge `0.3053` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5692` n `31` status `ready` deltaP `30.4955` edge `0.0193` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3096` n `31` status `ready` deltaP `11.6573` edge `0.2541` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6217` n `31` status `ready` deltaP `30.7803` edge `0.0306` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
