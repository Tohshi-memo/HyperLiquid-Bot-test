# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T12:52:26.866905+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4108`

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

- `market_context_high->unknown_24h` score `1786.7823` n `87` status `ready` deltaP `3.4542` edge `148.8755` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.6381` n `50` status `ready` deltaP `66.0656` edge `4.5167` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.3792` n `50` status `ready` deltaP `30.0207` edge `2.1423` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.3753` n `87` status `ready` deltaP `44.4345` edge `1.8738` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `14.3634` n `50` status `ready` deltaP `43.9451` edge `1.017` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `13.4503` n `87` status `ready` deltaP `28.6879` edge `1.7455` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.095` n `50` status `ready` deltaP `57.4301` edge `0.4054` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.9175` n `50` status `ready` deltaP `51.8135` edge `0.3977` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.2879` n `50` status `ready` deltaP `16.3661` edge `1.404` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.9624` n `50` status `ready` deltaP `44.0793` edge `0.1573` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.4709` n `50` status `ready` deltaP `22.6946` edge `0.2843` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.45` n `50` status `ready` deltaP `26.3841` edge `0.3385` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `3.8532` n `50` status `ready` deltaP `20.2317` edge `0.3238` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.7106` n `50` status `ready` deltaP `34.1341` edge `0.107` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1248` n `50` status `ready` deltaP `29.2195` edge `0.1006` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1383` n `50` status `ready` deltaP `24.0958` edge `0.043` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4808` n `50` status `ready` deltaP `18.994` edge `0.0269` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.888` n `50` status `ready` deltaP `19.5199` edge `0.201` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7157` n `50` status `ready` deltaP `16.2455` edge `0.0814` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6736` n `50` status `ready` deltaP `18.2455` edge `0.0699` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
