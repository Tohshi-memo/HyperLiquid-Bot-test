# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T19:22:20.875948+00:00`
- Price records: `672`
- Market context records: `1147`
- Flow alert records: `5204`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `19.5806` n `152` status `ready` deltaP `43.2017` edge `1.4569` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.3147` n `152` status `ready` deltaP `19.5541` edge `0.8475` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.6474` n `152` status `ready` deltaP `19.0332` edge `0.6034` maxDD `-6.4404`
- `market_context_high->index_24h` score `6.0761` n `152` status `ready` deltaP `17.6444` edge `0.4445` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.7007` n `152` status `ready` deltaP `-1.6082` edge `0.6525` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5247` n `168` status `ready` deltaP `12.3185` edge `0.1946` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.2073` n `168` status `ready` deltaP `9.6617` edge `0.1045` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5924` n `168` status `ready` deltaP `8.3939` edge `0.0251` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5414` n `168` status `ready` deltaP `4.0775` edge `0.0557` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.3693` n `168` status `ready` deltaP `10.1336` edge `0.1719` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.1725` n `168` status `ready` deltaP `7.5813` edge `0.0404` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0657` n `168` status `ready` deltaP `7.567` edge `0.0006` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.1782` n `168` status `ready` deltaP `3.2435` edge `0.0478` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.1873` n `168` status `ready` deltaP `7.1001` edge `-0.0019` maxDD `-2.2164`
- `market_context_high->crypto_alt_4h` score `-0.8034` n `168` status `ready` deltaP `7.063` edge `0.1464` maxDD `-16.7194`
- `market_context_high->commodity_1h` score `-0.8369` n `168` status `ready` deltaP `-2.9726` edge `-0.0067` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.8685` n `168` status `ready` deltaP `-1.3502` edge `-0.0027` maxDD `-1.6381`
- `market_context_high->metal_4h` score `-2.2853` n `168` status `ready` deltaP `7.6147` edge `-0.0458` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-3.2218` n `168` status `ready` deltaP `9.1609` edge `-0.2079` maxDD `-6.7322`
- `market_context_high->unknown_24h` score `-3.2512` n `152` status `ready` deltaP `4.1301` edge `-0.0255` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
