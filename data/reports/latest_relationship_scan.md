# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T18:07:26.198025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10026`

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

- `market_context_high->unknown_24h` score `535.8902` n `64` status `ready` deltaP `3.8128` edge `44.6321` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.4293` n `50` status `ready` deltaP `50.565` edge `3.5193` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.7467` n `64` status `ready` deltaP `46.94` edge `3.2368` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.763` n `64` status `ready` deltaP `62.8899` edge `2.502` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.3053` n `50` status `ready` deltaP `46.2149` edge `2.7941` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2801` n `50` status `ready` deltaP `39.2195` edge `0.8749` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.3304` n `50` status `ready` deltaP `19.3899` edge `1.5175` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1617` n `64` status `ready` deltaP `49.5586` edge `0.3584` maxDD `-0.0251`
- `market_context_high->metal_24h` score `6.7252` n `64` status `ready` deltaP `63.5778` edge `0.5275` maxDD `-3.7989`
- `news_risk_high->commodity_24h` score `6.6482` n `50` status `ready` deltaP `43.8475` edge `0.2617` maxDD `0.0`
- `news_risk_high->index_24h` score `6.5675` n `50` status `ready` deltaP `42.2461` edge `0.296` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.3747` n `50` status `ready` deltaP `22.9756` edge `0.4323` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.9478` n `50` status `ready` deltaP `44.8415` edge `0.151` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.6792` n `50` status `ready` deltaP `27.2988` edge `0.3515` maxDD `-9.4848`
- `market_context_high->crypto_major_24h` score `4.5543` n `64` status `ready` deltaP `13.2149` edge `1.2252` maxDD `-69.0352`
- `news_risk_high->equity_1h` score `3.9732` n `50` status `ready` deltaP `21.1976` edge `0.2528` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7221` n `50` status `ready` deltaP `34.7439` edge `0.1039` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6219` n `50` status `ready` deltaP `25.4085` edge `0.0841` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1873` n `50` status `ready` deltaP `24.994` edge `0.0411` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2819` n `50` status `ready` deltaP `17.0479` edge `0.0233` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
