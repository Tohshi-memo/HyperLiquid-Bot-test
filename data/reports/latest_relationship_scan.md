# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T03:52:26.843367+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7710`

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

- `market_context_high->unknown_4h` score `52.5693` n `95` status `ready` deltaP `0.8408` edge `4.4087` maxDD `-1.016`
- `market_context_high->unknown_1h` score `17.6463` n `107` status `ready` deltaP `2.9423` edge `1.4998` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `1.2215` n `43` status `ready` deltaP `16.5738` edge `0.0822` maxDD `-3.6055`
- `market_context_high->crypto_alt_24h` score `0.199` n `43` status `ready` deltaP `16.8524` edge `0.2445` maxDD `-23.1738`
- `market_context_high->commodity_1h` score `-0.2906` n `107` status `ready` deltaP `2.3323` edge `0.0103` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3303` n `107` status `ready` deltaP `-1.3977` edge `0.0022` maxDD `-0.1513`
- `market_context_high->crypto_major_24h` score `-0.4032` n `43` status `ready` deltaP `11.6441` edge `0.0671` maxDD `-11.0468`
- `market_context_high->commodity_4h` score `-0.4426` n `95` status `ready` deltaP `1.1874` edge `0.0406` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5328` n `107` status `ready` deltaP `0.3582` edge `-0.0055` maxDD `-1.2155`
- `market_context_high->fx_4h` score `-0.6118` n `95` status `ready` deltaP `-3.5976` edge `0.0054` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.6895` n `43` status `ready` deltaP `2.3498` edge `0.0022` maxDD `-1.0258`
- `market_context_high->metal_1h` score `-0.7912` n `107` status `ready` deltaP `2.7534` edge `-0.0051` maxDD `-1.6682`
- `market_context_high->crypto_major_1h` score `-0.966` n `107` status `ready` deltaP `6.1839` edge `-0.007` maxDD `-9.3126`
- `market_context_high->equity_1h` score `-2.346` n `107` status `ready` deltaP `2.0049` edge `-0.0868` maxDD `-12.1865`
- `market_context_high->crypto_alt_1h` score `-2.3676` n `107` status `ready` deltaP `2.0776` edge `-0.0321` maxDD `-11.3243`
- `market_context_high->metal_4h` score `-2.4378` n `95` status `ready` deltaP `-0.2006` edge `-0.0275` maxDD `-5.612`
- `market_context_high->metal_24h` score `-2.6106` n `43` status `ready` deltaP `-6.9161` edge `-0.0145` maxDD `-6.5552`
- `market_context_high->index_4h` score `-3.8601` n `95` status `ready` deltaP `-12.6717` edge `-0.0459` maxDD `-4.637`
- `market_context_high->crypto_major_4h` score `-6.4981` n `95` status `ready` deltaP `-12.8242` edge `-0.2117` maxDD `-36.2049`
- `market_context_high->index_24h` score `-6.9436` n `43` status `ready` deltaP `-35.1098` edge `-0.1921` maxDD `-5.864`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
