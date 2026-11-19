# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T11:37:33.211799+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `11860.4966` n `109` status `ready` deltaP `0.9477` edge `988.3882` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7357.911` n `109` status `ready` deltaP `0.1301` edge `613.1868` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `13.8978` n `95` status `ready` deltaP `41.7727` edge `1.7067` maxDD `-13.9399`
- `market_context_high->crypto_alt_24h` score `10.9829` n `95` status `ready` deltaP `22.522` edge `1.4308` maxDD `-10.1635`
- `market_context_high->crypto_major_4h` score `0.4108` n `109` status `ready` deltaP `1.9747` edge `0.337` maxDD `-17.4668`
- `market_context_high->crypto_alt_4h` score `0.0945` n `109` status `ready` deltaP `2.432` edge `0.2176` maxDD `-13.4025`
- `market_context_high->metal_24h` score `-0.0256` n `95` status `ready` deltaP `16.2902` edge `0.1981` maxDD `-14.7068`
- `market_context_high->metal_4h` score `-0.0798` n `109` status `ready` deltaP `14.946` edge `0.0227` maxDD `-5.9858`
- `market_context_high->metal_1h` score `-0.276` n `109` status `ready` deltaP `2.8347` edge `0.0122` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.7482` n `109` status `ready` deltaP `-1.2841` edge `0.003` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.8524` n `109` status `ready` deltaP `2.3856` edge `0.0613` maxDD `-10.2523`
- `market_context_high->crypto_alt_1h` score `-1.1417` n `109` status `ready` deltaP `-2.9501` edge `0.0236` maxDD `-7.6911`
- `market_context_high->index_4h` score `-1.2212` n `109` status `ready` deltaP `-3.2138` edge `-0.0008` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.5234` n `109` status `ready` deltaP `-10.6274` edge `-0.0012` maxDD `-0.392`
- `market_context_high->fx_4h` score `-2.4396` n `109` status `ready` deltaP `-15.6285` edge `-0.0044` maxDD `-2.0011`
- `market_context_high->commodity_1h` score `-2.5` n `109` status `ready` deltaP `-10.9076` edge `-0.0278` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.6349` n `109` status `ready` deltaP `1.3185` edge `-0.0205` maxDD `-10.9626`
- `market_context_high->fx_24h` score `-6.8219` n `95` status `ready` deltaP `-19.9324` edge `-0.0059` maxDD `-5.7098`
- `market_context_high->commodity_4h` score `-7.6685` n `109` status `ready` deltaP `-25.5538` edge `-0.1068` maxDD `-14.9509`
- `market_context_high->index_24h` score `-9.3698` n `95` status `ready` deltaP `-17.924` edge `-0.1191` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
