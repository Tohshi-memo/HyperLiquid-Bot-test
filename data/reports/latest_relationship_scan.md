# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T01:07:28.539757+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7190`

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

- `market_context_high->unknown_4h` score `22.1817` n `95` status `ready` deltaP `1.741` edge `1.8704` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.6536` n `54` status `ready` deltaP `21.9908` edge `0.0821` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.8436` n `95` status `ready` deltaP `11.0896` edge `0.0526` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.2278` n `107` status `ready` deltaP `3.1171` edge `0.0103` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3314` n `107` status `ready` deltaP `-1.3977` edge `0.0023` maxDD `-0.1712`
- `market_context_high->metal_1h` score `-0.922` n `107` status `ready` deltaP `1.1836` edge `-0.0053` maxDD `-1.6873`
- `market_context_high->index_1h` score `-1.0248` n `107` status `ready` deltaP `-1.9965` edge `-0.0069` maxDD `-1.2155`
- `market_context_high->fx_4h` score `-1.0393` n `95` status `ready` deltaP `-4.4977` edge `0.004` maxDD `-0.5168`
- `market_context_high->fx_24h` score `-1.5582` n `54` status `ready` deltaP `-4.2824` edge `-0.0026` maxDD `-1.5625`
- `market_context_high->crypto_major_24h` score `-2.0194` n `54` status `ready` deltaP `0.5787` edge `-0.0295` maxDD `-13.9938`
- `market_context_high->crypto_major_1h` score `-2.3464` n `107` status `ready` deltaP `1.4746` edge `-0.0333` maxDD `-10.432`
- `market_context_high->metal_4h` score `-3.2572` n `95` status `ready` deltaP `-9.2025` edge `-0.0321` maxDD `-5.9056`
- `market_context_high->metal_24h` score `-3.2801` n `54` status `ready` deltaP `-10.706` edge `0.0069` maxDD `-7.043`
- `market_context_high->crypto_alt_1h` score `-3.2866` n `107` status `ready` deltaP `0.5079` edge `-0.0556` maxDD `-14.3999`
- `market_context_high->equity_1h` score `-4.0075` n `107` status `ready` deltaP `-1.1347` edge `-0.0935` maxDD `-12.6316`
- `market_context_high->index_4h` score `-4.8124` n `95` status `ready` deltaP `-22.5738` edge `-0.0525` maxDD `-5.1768`
- `market_context_high->crypto_alt_24h` score `-6.8863` n `54` status `ready` deltaP `3.588` edge `-0.2294` maxDD `-47.1901`
- `market_context_high->index_24h` score `-7.6166` n `54` status `ready` deltaP `-37.3842` edge `-0.1777` maxDD `-6.6229`
- `market_context_high->unknown_1h` score `-8.0569` n `107` status `ready` deltaP `-0.1973` edge `-0.6212` maxDD `-1.5781`
- `market_context_high->crypto_major_4h` score `-13.0288` n `95` status `ready` deltaP `-22.7262` edge `-0.3281` maxDD `-41.8234`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
