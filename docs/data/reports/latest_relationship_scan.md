# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T20:37:31.972883+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4400`

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

- `market_context_high->unknown_24h` score `260.7076` n `34` status `ready` deltaP `3.9655` edge `21.6992` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.695` n `50` status `ready` deltaP `59.2069` edge `4.1505` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.4769` n `50` status `ready` deltaP `39.2069` edge `2.4782` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.2848` n `34` status `ready` deltaP `14.6044` edge `1.5808` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.4776` n `50` status `ready` deltaP `44.383` edge `1.0236` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.3126` n `34` status `ready` deltaP `42.9716` edge `1.6191` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.7456` n `50` status `ready` deltaP `23.3103` edge `1.5446` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0459` n `50` status `ready` deltaP `50.2414` edge `0.3659` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.3763` n `50` status `ready` deltaP `41.3793` edge `0.2555` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3755` n `50` status `ready` deltaP `47.3982` edge `0.1696` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7432` n `50` status `ready` deltaP `27.5745` edge `0.355` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.4818` n `50` status `ready` deltaP `22.0958` edge `0.2892` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.4641` n `50` status `ready` deltaP `22.1824` edge `0.3617` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0633` n `50` status `ready` deltaP `36.8632` edge `0.1182` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1572` n `50` status `ready` deltaP `29.5198` edge `0.1013` maxDD `-0.7999`
- `market_context_high->metal_24h` score `3.1221` n `34` status `ready` deltaP `39.1683` edge `0.2283` maxDD `-3.7989`
- `news_risk_high->metal_1h` score `2.3096` n `50` status `ready` deltaP `25.8922` edge `0.0453` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5335` n `50` status `ready` deltaP `19.5928` edge `0.0273` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9035` n `50` status `ready` deltaP `18.3413` edge `0.0915` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.9003` n `50` status `ready` deltaP `18.3448` edge `0.2104` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
