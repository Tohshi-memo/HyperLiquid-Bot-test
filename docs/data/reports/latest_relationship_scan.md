# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T09:07:36.078642+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `market_context_high->unknown_4h` score `845.8409` n `31` status `ready` deltaP `8.8415` edge `70.4278` maxDD `0.0`
- `market_context_high->unknown_1h` score `241.7308` n `31` status `ready` deltaP `9.267` edge `20.0931` maxDD `-0.1853`
- `news_risk_high->crypto_alt_24h` score `5.2387` n `106` status `ready` deltaP `25.7207` edge `0.8384` maxDD `-23.0594`
- `market_context_high->crypto_alt_4h` score `5.1598` n `31` status `ready` deltaP `22.8462` edge `0.3071` maxDD `-1.6876`
- `market_context_high->equity_4h` score `4.8096` n `31` status `ready` deltaP `4.7108` edge `0.4396` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `3.8905` n `31` status `ready` deltaP `19.5957` edge `0.2272` maxDD `-1.6901`
- `market_context_high->equity_1h` score `2.9593` n `31` status `ready` deltaP `7.9148` edge `0.2339` maxDD `-1.2043`
- `market_context_high->index_4h` score `2.432` n `31` status `ready` deltaP `23.1511` edge `0.071` maxDD `-0.1474`
- `news_risk_high->crypto_alt_4h` score `1.6476` n `128` status `ready` deltaP `10.2706` edge `0.2814` maxDD `-7.4246`
- `market_context_high->crypto_alt_1h` score `1.1739` n `31` status `ready` deltaP `8.6633` edge `0.1369` maxDD `-1.5324`
- `market_context_high->crypto_major_1h` score `1.0767` n `31` status `ready` deltaP `7.9148` edge `0.1243` maxDD `-1.1219`
- `market_context_high->fx_1h` score `0.8151` n `31` status `ready` deltaP `10.8412` edge `0.0128` maxDD `-0.0388`
- `market_context_high->commodity_4h` score `0.8114` n `31` status `ready` deltaP `17.26` edge `0.0302` maxDD `-1.633`
- `market_context_high->metal_4h` score `0.7358` n `31` status `ready` deltaP `13.3999` edge `0.0432` maxDD `-0.7228`
- `market_context_high->index_1h` score `0.147` n `31` status `ready` deltaP `0.7147` edge `0.0316` maxDD `-0.2628`
- `market_context_high->metal_1h` score `0.0381` n `31` status `ready` deltaP `2.7284` edge `0.0124` maxDD `-0.3895`
- `news_risk_high->crypto_alt_1h` score `-0.2685` n `140` status `ready` deltaP `2.7417` edge `0.0546` maxDD `-4.584`
- `news_risk_high->fx_1h` score `-0.5547` n `140` status `ready` deltaP `0.2652` edge `-0.0028` maxDD `-0.6065`
- `market_context_high->commodity_1h` score `-0.6487` n `31` status `ready` deltaP `-6.4178` edge `0.0135` maxDD `-0.6439`
- `market_context_high->fx_4h` score `-0.7535` n `31` status `ready` deltaP `-6.0582` edge `0.0167` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
