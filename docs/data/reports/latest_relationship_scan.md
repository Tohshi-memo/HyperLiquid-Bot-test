# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T03:52:29.485491+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4560`

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

- `market_context_high->unknown_1h` score `32366.6054` n `45` status `ready` deltaP `2.1656` edge `2697.2121` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22214.0288` n `45` status `ready` deltaP `2.7202` edge `1851.1648` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1157.076` n `31` status `ready` deltaP `2.3807` edge `96.4247` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `978.6757` n `31` status `ready` deltaP `3.9388` edge `81.5357` maxDD `-0.119`
- `news_risk_high->equity_24h` score `36.3402` n `31` status `ready` deltaP `42.1875` edge `2.7471` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `34.994` n `31` status `ready` deltaP `46.1806` edge `2.6083` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.7661` n `31` status `ready` deltaP `45.4861` edge `2.2606` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.7822` n `31` status `ready` deltaP `41.9299` edge `0.7298` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.734` n `31` status `ready` deltaP `24.1689` edge `0.8204` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6359` n `31` status `ready` deltaP `30.8222` edge `0.5624` maxDD `-2.1911`
- `news_risk_high->crypto_major_4h` score `6.6485` n `31` status `ready` deltaP `14.3391` edge `0.8985` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.6411` n `31` status `ready` deltaP `56.4684` edge `0.1898` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.553` n `31` status `ready` deltaP `39.7569` edge `0.1977` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.314` n `31` status `ready` deltaP `18.3407` edge `0.1726` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1698` n `45` status `ready` deltaP `37.8624` edge `0.0402` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.7412` n `31` status `ready` deltaP `30.5173` edge `0.051` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5872` n `31` status `ready` deltaP `11.3579` edge `0.3021` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4877` n `31` status `ready` deltaP `29.747` edge `0.0175` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2037` n `31` status `ready` deltaP `10.7591` edge `0.2465` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6139` n `31` status `ready` deltaP `30.7803` edge `0.0296` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
