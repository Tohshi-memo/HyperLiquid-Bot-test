# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T00:37:22.431667+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8592`

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

- `market_context_high->unknown_24h` score `1032.4389` n `40` status `ready` deltaP `3.9861` edge `86.01` maxDD `0.0`
- `news_risk_high->equity_24h` score `47.0241` n `50` status `ready` deltaP `50.565` edge `3.6522` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `44.7259` n `64` status `ready` deltaP `8.9939` edge `3.6672` maxDD `0.0`
- `market_context_high->equity_24h` score `35.4847` n `40` status `ready` deltaP `37.565` edge `2.8608` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `31.3136` n `40` status `ready` deltaP `56.6031` edge `2.3398` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.7668` n `50` status `ready` deltaP `43.2686` edge `2.6165` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `12.7806` n `40` status `ready` deltaP `15.2686` edge `1.3988` maxDD `-30.1765`
- `news_risk_high->equity_4h` score `11.7044` n `50` status `ready` deltaP `36.628` edge `0.8442` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.1439` n `50` status `ready` deltaP `20.6031` edge `1.4855` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.2227` n `40` status `ready` deltaP `46.7461` edge `0.2989` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.7823` n `50` status `ready` deltaP `42.2461` edge `0.3139` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2656` n `50` status `ready` deltaP `41.0745` edge `0.2483` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9154` n `50` status `ready` deltaP `43.9268` edge `0.1544` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.8079` n `40` status `ready` deltaP `55.7626` edge `0.3338` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.2864` n `50` status `ready` deltaP `20.2317` edge `0.3599` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.049` n `50` status `ready` deltaP `25.3171` edge `0.3122` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.6948` n `50` status `ready` deltaP `33.9817` edge `0.1067` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.6543` n `50` status `ready` deltaP `19.4012` edge `0.2382` maxDD `-3.7082`
- `news_risk_high->index_4h` score `2.403` n `50` status `ready` deltaP `23.122` edge `0.0811` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1178` n `50` status `ready` deltaP `24.3952` edge `0.0393` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
