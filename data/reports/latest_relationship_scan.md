# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T00:22:30.711945+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `23.0757` n `95` status `ready` deltaP `1.741` edge `1.9449` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.7151` n `57` status `ready` deltaP `22.8344` edge `0.0816` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9984` n `95` status `ready` deltaP `12.8899` edge `0.0535` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.1638` n `107` status `ready` deltaP `3.902` edge `0.0104` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3795` n `107` status `ready` deltaP `0.1721` edge `0.0027` maxDD `-0.1712`
- `market_context_high->metal_1h` score `-0.9232` n `107` status `ready` deltaP `1.1836` edge `-0.0054` maxDD `-1.6873`
- `market_context_high->fx_4h` score `-0.9625` n `95` status `ready` deltaP `-3.5976` edge `0.0044` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.09` n `107` status `ready` deltaP `-2.7814` edge `-0.0071` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-1.8324` n `57` status `ready` deltaP `-5.6469` edge `-0.0027` maxDD `-1.6549`
- `market_context_high->crypto_major_24h` score `-2.5095` n `57` status `ready` deltaP `-1.9006` edge `-0.0578` maxDD `-15.4338`
- `market_context_high->crypto_major_1h` score `-2.5097` n `107` status `ready` deltaP `-0.0951` edge `-0.0363` maxDD `-10.4432`
- `market_context_high->crypto_alt_1h` score `-3.3679` n `107` status `ready` deltaP `-0.277` edge `-0.0562` maxDD `-14.4757`
- `market_context_high->metal_24h` score `-3.4675` n `57` status `ready` deltaP `-11.4857` edge `0.0109` maxDD `-7.1964`
- `market_context_high->metal_4h` score `-3.4866` n `95` status `ready` deltaP `-11.9031` edge `-0.0328` maxDD `-5.9385`
- `market_context_high->equity_1h` score `-4.0183` n `107` status `ready` deltaP `-1.1347` edge `-0.0944` maxDD `-12.6316`
- `market_context_high->index_4h` score `-5.0604` n `95` status `ready` deltaP `-25.2744` edge `-0.0539` maxDD `-5.2777`
- `market_context_high->index_24h` score `-7.772` n `57` status `ready` deltaP `-37.5457` edge `-0.1745` maxDD `-6.8288`
- `market_context_high->unknown_1h` score `-8.2273` n `107` status `ready` deltaP `-0.1973` edge `-0.6354` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `-8.4409` n `57` status `ready` deltaP `0.8589` edge `-0.3184` maxDD `-53.5593`
- `market_context_high->crypto_major_4h` score `-14.1358` n `95` status `ready` deltaP `-25.4268` edge `-0.3649` maxDD `-43.8188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
