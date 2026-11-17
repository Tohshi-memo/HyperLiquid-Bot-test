# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T06:52:24.291721+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4356`

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

- `market_context_high->unknown_24h` score `2407.5143` n `66` status `ready` deltaP `3.4483` edge `200.6032` maxDD `0.0`
- `news_risk_high->equity_24h` score `56.2641` n `50` status `ready` deltaP `61.9655` edge `4.3462` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.5746` n `50` status `ready` deltaP `34.0345` edge `2.2688` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.1212` n `66` status `ready` deltaP `18.8035` edge `1.5971` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.5042` n `50` status `ready` deltaP `44.25` edge `1.0267` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.2173` n `66` status `ready` deltaP `39.6709` edge `1.7571` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.1011` n `50` status `ready` deltaP `20.3793` edge `1.4815` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.545` n `50` status `ready` deltaP `53.3448` edge `0.3868` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.9271` n `50` status `ready` deltaP `47.7586` edge `0.3422` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0724` n `50` status `ready` deltaP `44.689` edge `0.1624` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6676` n `50` status `ready` deltaP `23.5928` edge `0.2947` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4818` n `50` status `ready` deltaP `26.8415` edge `0.3381` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.1378` n `50` status `ready` deltaP `21.2988` edge `0.3404` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1021` n `50` status `ready` deltaP `37.1829` edge `0.1193` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2367` n `50` status `ready` deltaP `30.439` edge `0.1018` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2353` n `50` status `ready` deltaP `24.994` edge `0.0451` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5886` n `50` status `ready` deltaP `20.1916` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8085` n `50` status `ready` deltaP `16.994` edge `0.0883` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7781` n `50` status `ready` deltaP `18.8443` edge `0.0793` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7283` n `50` status `ready` deltaP `17.4828` edge `0.1941` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
