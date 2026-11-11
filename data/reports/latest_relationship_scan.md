# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T13:37:27.236491+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11488`

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

- `market_context_high->unknown_4h` score `75.9354` n `88` status `ready` deltaP `8.1347` edge `6.3185` maxDD `-0.9161`
- `market_context_high->equity_24h` score `30.8801` n `88` status `ready` deltaP `26.8781` edge `2.6333` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.7774` n `53` status `ready` deltaP `35.7829` edge `0.8551` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.2196` n `88` status `ready` deltaP `38.4943` edge `1.4348` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.5412` n `88` status `ready` deltaP `26.9886` edge `0.3281` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.2661` n `88` status `ready` deltaP `31.2026` edge `0.2028` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.5419` n `53` status `ready` deltaP `17.8652` edge `0.2473` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.5389` n `53` status `ready` deltaP `19.5237` edge `0.3135` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `3.5035` n `53` status `ready` deltaP `35.8779` edge `0.0904` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.1002` n `53` status `ready` deltaP `25.9492` edge `0.1107` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3157` n `53` status `ready` deltaP `21.6607` edge `0.0922` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8577` n `53` status `ready` deltaP `23.4497` edge `0.2457` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.655` n `53` status `ready` deltaP `20.6502` edge `0.0257` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.303` n `53` status `ready` deltaP `17.0263` edge `0.0252` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6376` n `53` status `ready` deltaP `17.7437` edge `0.0614` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.617` n `53` status `ready` deltaP `18.6419` edge `0.06` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2271` n `53` status `ready` deltaP `-3.0985` edge `0.0352` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3472` n `88` status `ready` deltaP `3.4976` edge `0.0154` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4853` n `88` status `ready` deltaP `1.6399` edge `-0.0049` maxDD `-1.7935`
- `market_context_high->crypto_major_24h` score `-0.5616` n `88` status `ready` deltaP `16.6983` edge `1.0044` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
