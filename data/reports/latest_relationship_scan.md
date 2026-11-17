# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T04:22:36.001697+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4422`

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

- `market_context_high->unknown_24h` score `2107.3103` n `59` status `ready` deltaP `3.4483` edge `175.5862` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.339` n `50` status `ready` deltaP `60.2414` edge `4.2806` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.1057` n `50` status `ready` deltaP `35.7586` edge `2.3254` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.518` n `59` status `ready` deltaP `12.8346` edge `1.5033` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.4052` n `50` status `ready` deltaP `43.7927` edge `1.0215` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.3206` n `59` status `ready` deltaP `37.0806` edge `1.6594` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.2535` n `50` status `ready` deltaP `21.2414` edge `1.4953` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.3123` n `50` status `ready` deltaP `51.6207` edge `0.3789` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.4808` n `50` status `ready` deltaP `46.0345` edge `0.3165` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2375` n `50` status `ready` deltaP `46.2134` edge `0.166` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5528` n `50` status `ready` deltaP `26.9939` edge `0.343` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.4974` n `50` status `ready` deltaP `22.5449` edge `0.2875` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.2897` n `50` status `ready` deltaP `21.9085` edge `0.349` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1373` n `50` status `ready` deltaP `37.4878` edge `0.1202` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.12` n `50` status `ready` deltaP `29.2195` edge `0.1002` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2066` n `50` status `ready` deltaP `24.6946` edge `0.0447` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5191` n `50` status `ready` deltaP `19.4431` edge `0.0271` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8059` n `50` status `ready` deltaP `18.3448` edge `0.1983` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7313` n `50` status `ready` deltaP `16.3952` edge `0.0824` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7134` n `50` status `ready` deltaP `18.3952` edge `0.074` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
