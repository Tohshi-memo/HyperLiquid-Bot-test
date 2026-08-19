# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T13:52:24.778067+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11750`

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

- `market_context_high->equity_4h` score `2.0919` n `96` status `ready` deltaP `11.3059` edge `0.1878` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.778` n `96` status `ready` deltaP `14.8516` edge `0.0793` maxDD `-0.4112`
- `market_context_high->crypto_major_24h` score `1.5943` n `96` status `ready` deltaP `4.6875` edge `0.2224` maxDD `-4.9964`
- `market_context_high->metal_4h` score `1.0886` n `96` status `ready` deltaP `17.1748` edge `0.0338` maxDD `-1.273`
- `market_context_high->index_1h` score `0.9534` n `96` status `ready` deltaP `16.2113` edge `0.0101` maxDD `-0.0982`
- `market_context_high->commodity_24h` score `0.6719` n `96` status `ready` deltaP `9.8958` edge `0.2035` maxDD `-4.666`
- `market_context_high->crypto_major_4h` score `0.6502` n `96` status `ready` deltaP `9.4766` edge `0.0931` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `0.3312` n `96` status `ready` deltaP `18.2291` edge `-0.0433` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `0.1749` n `96` status `ready` deltaP `8.009` edge `-0.0161` maxDD `-0.4843`
- `market_context_high->fx_4h` score `0.1515` n `96` status `ready` deltaP `9.4766` edge `0.0065` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.1312` n `96` status `ready` deltaP `8.1046` edge `0.0224` maxDD `-0.5728`
- `market_context_high->metal_1h` score `0.0853` n `96` status `ready` deltaP `5.5202` edge `0.009` maxDD `-0.4291`
- `market_context_high->crypto_alt_4h` score `-0.1735` n `96` status `ready` deltaP `7.7744` edge `0.0607` maxDD `-5.4926`
- `market_context_high->fx_1h` score `-0.3191` n `96` status `ready` deltaP `-1.1727` edge `0.0028` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4407` n `96` status `ready` deltaP `2.6821` edge `0.0101` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4821` n `96` status `ready` deltaP `1.4783` edge `0.0085` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6136` n `96` status `ready` deltaP `0.2795` edge `0.0045` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8985` n `96` status `ready` deltaP `-7.7408` edge `-0.007` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.302` n `96` status `ready` deltaP `-4.3403` edge `0.0646` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.8156` n `96` status `ready` deltaP `-21.3541` edge `-0.0173` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
