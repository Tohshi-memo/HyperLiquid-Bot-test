# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T01:22:22.903958+00:00`
- Price records: `672`
- Market context records: `2616`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.899` n `146` status `ready` deltaP `18.2958` edge `0.5691` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.1125` n `146` status `ready` deltaP `24.8914` edge `0.528` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.3211` n `146` status `ready` deltaP `14.1539` edge `0.3634` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.388` n `146` status `ready` deltaP `11.73` edge `0.1562` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.1483` n `146` status `ready` deltaP `7.9895` edge `0.1474` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.8102` n `146` status `ready` deltaP `9.149` edge `0.1046` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.7664` n `146` status `ready` deltaP `9.1625` edge `0.1222` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.5308` n `146` status `ready` deltaP `2.0643` edge `0.6683` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2096` n `146` status `ready` deltaP `8.8227` edge `0.0428` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0832` n `146` status `ready` deltaP `4.3905` edge `0.0132` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3679` n `146` status `ready` deltaP `5.8014` edge `0.0185` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4416` n `146` status `ready` deltaP `1.9502` edge `0.0165` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.6177` n `146` status `ready` deltaP `1.4109` edge `0.0139` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6389` n `146` status `ready` deltaP `-0.5352` edge `0.0038` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7629` n `146` status `ready` deltaP `-0.2276` edge `0.0218` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8606` n `146` status `ready` deltaP `3.7399` edge `0.0421` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.9089` n `146` status `ready` deltaP `3.8884` edge `-0.0023` maxDD `-1.6157`
- `market_context_high->fx_4h` score `-0.9264` n `146` status `ready` deltaP `-0.378` edge `0.0111` maxDD `-0.8621`
- `market_context_high->commodity_4h` score `-0.997` n `146` status `ready` deltaP `4.1012` edge `0.0391` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.3842` n `146` status `ready` deltaP `1.6497` edge `0.0141` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
