# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T06:37:28.409672+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8952`

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

- `news_risk_high->equity_24h` score `48.9349` n `50` status `ready` deltaP `52.2361` edge `3.8003` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1441` n `50` status `ready` deltaP `40.6389` edge `2.5542` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.8962` n `50` status `ready` deltaP `37.3902` edge `0.8551` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.3272` n `50` status `ready` deltaP `22.2986` edge `1.4977` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.0984` n `50` status `ready` deltaP `43.9028` edge `0.3292` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.135` n `50` status `ready` deltaP `40.9722` edge `0.2381` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.977` n `50` status `ready` deltaP `44.2317` edge `0.1575` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1764` n `50` status `ready` deltaP `20.5366` edge `0.3487` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `3.9556` n `50` status `ready` deltaP `25.4695` edge `0.3034` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9301` n `50` status `ready` deltaP `20.2994` edge `0.2552` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7412` n `50` status `ready` deltaP `34.5915` edge `0.1065` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4624` n `50` status `ready` deltaP `23.5793` edge `0.083` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2688` n `50` status `ready` deltaP `25.5928` edge `0.0439` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2735` n `50` status `ready` deltaP `16.8982` edge `0.0236` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9823` n `50` status `ready` deltaP `18.9028` edge `0.2172` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8583` n `50` status `ready` deltaP `20.0419` edge `0.0816` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.82` n `50` status `ready` deltaP `18.1916` edge `0.0818` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.2886` n `50` status `ready` deltaP `3.497` edge `0.0342` maxDD `-0.3438`
- `market_context_high->crypto_alt_4h` score `-0.9661` n `64` status `ready` deltaP `2.782` edge `0.1386` maxDD `-17.1476`
- `market_context_high->index_4h` score `-1.2639` n `64` status `ready` deltaP `-4.4207` edge `-0.0313` maxDD `-2.7678`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
