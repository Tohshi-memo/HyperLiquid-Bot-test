# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T00:52:33.101797+00:00`
- Price records: `672`
- Market context records: `7086`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.7414` n `168` status `ready` deltaP `17.6975` edge `0.0138` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1502` n `168` status `ready` deltaP `4.4696` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.1511` n `168` status `ready` deltaP `0.3101` edge `0.0412` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.3874` n `168` status `ready` deltaP `1.0301` edge `0.0299` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.44` n `168` status `ready` deltaP `1.5219` edge `-0.0046` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6173` n `168` status `ready` deltaP `3.2685` edge `0.0343` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.9022` n `168` status `ready` deltaP `-5.0756` edge `-0.0202` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.4592` n `168` status `ready` deltaP `-6.0629` edge `-0.0044` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.5482` n `168` status `ready` deltaP `-7.2372` edge `-0.0467` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.9731` n `168` status `ready` deltaP `3.6035` edge `-0.0347` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.1721` n `168` status `ready` deltaP `4.1594` edge `-0.0363` maxDD `-12.2591`
- `market_context_high->unknown_4h` score `-2.5158` n `168` status `ready` deltaP `-8.0865` edge `0.0077` maxDD `-4.742`
- `market_context_high->commodity_24h` score `-2.6687` n `168` status `ready` deltaP `-4.2162` edge `-0.0634` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-3.007` n `168` status `ready` deltaP `3.8763` edge `0.0171` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.1185` n `168` status `ready` deltaP `-1.2558` edge `-0.0129` maxDD `-22.2831`
- `market_context_high->metal_4h` score `-3.9147` n `168` status `ready` deltaP `-3.1504` edge `-0.0069` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.9393` n `168` status `ready` deltaP `-4.4643` edge `-0.0158` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-8.1501` n `168` status `ready` deltaP `2.6931` edge `-0.1758` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-8.4821` n `168` status `ready` deltaP `-21.2798` edge `-0.0503` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-15.377` n `168` status `ready` deltaP `-23.5863` edge `-0.1197` maxDD `-44.0246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
