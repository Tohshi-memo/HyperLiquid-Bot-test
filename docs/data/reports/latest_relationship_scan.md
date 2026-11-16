# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T20:52:26.482177+00:00`
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

- `market_context_high->unknown_24h` score `321.7528` n `35` status `ready` deltaP `3.9655` edge `26.7863` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.7274` n `50` status `ready` deltaP `59.2069` edge `4.1532` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.4305` n `50` status `ready` deltaP `39.0345` edge `2.4734` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.1885` n `35` status `ready` deltaP `13.596` edge `1.5795` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.5138` n `50` status `ready` deltaP `44.535` edge `1.0256` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.4072` n `35` status `ready` deltaP `43.8916` edge `1.6251` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.723` n `50` status `ready` deltaP `23.3103` edge `1.5417` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0495` n `50` status `ready` deltaP `50.2414` edge `0.3662` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.3943` n `50` status `ready` deltaP `41.3793` edge `0.257` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3937` n `50` status `ready` deltaP `47.5502` edge `0.1701` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7107` n `50` status `ready` deltaP `27.4225` edge `0.3533` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5058` n `50` status `ready` deltaP `22.2455` edge `0.2902` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.4593` n `50` status `ready` deltaP `22.1824` edge `0.3613` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0621` n `50` status `ready` deltaP `36.8632` edge `0.1181` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1742` n `50` status `ready` deltaP `29.6717` edge `0.1017` maxDD `-0.7999`
- `market_context_high->metal_24h` score `2.9629` n `35` status `ready` deltaP `37.4877` edge `0.2191` maxDD `-3.7989`
- `news_risk_high->metal_1h` score `2.3276` n `50` status `ready` deltaP `26.0419` edge `0.0458` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5479` n `50` status `ready` deltaP `19.7425` edge `0.0275` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8995` n `50` status `ready` deltaP `18.3448` edge `0.2103` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8926` n `50` status `ready` deltaP `18.1916` edge `0.0911` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
