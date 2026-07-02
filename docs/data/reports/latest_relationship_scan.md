# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T11:58:41.804468+00:00`
- Price records: `672`
- Market context records: `5452`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `market_context_high->crypto_major_24h` score `3.3861` n `189` status `ready` deltaP `17.295` edge `0.6209` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.9274` n `197` status `ready` deltaP `15.435` edge `0.3703` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.4589` n `197` status `ready` deltaP `12.5356` edge `0.2852` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.2269` n `197` status `ready` deltaP `10.5083` edge `0.2796` maxDD `-9.46`
- `market_context_high->equity_24h` score `1.7729` n `189` status `ready` deltaP `10.1191` edge `0.5426` maxDD `-28.9858`
- `market_context_high->equity_1h` score `0.5087` n `199` status `ready` deltaP `8.1628` edge `0.0845` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2054` n `189` status `ready` deltaP `10.9127` edge `0.0339` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.157` n `199` status `ready` deltaP `6.7839` edge `0.0172` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.2629` n `199` status `ready` deltaP `3.9614` edge `0.0192` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.3285` n `199` status `ready` deltaP `0.9569` edge `0.0624` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4411` n `199` status `ready` deltaP `2.1439` edge `0.0735` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5788` n `199` status `ready` deltaP `0.1121` edge `-0.0001` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8275` n `197` status `ready` deltaP `7.4656` edge `0.0422` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1011` n `197` status `ready` deltaP `1.0585` edge `0.0037` maxDD `-1.5345`
- `market_context_high->index_24h` score `-1.2841` n `189` status `ready` deltaP `14.6412` edge `0.0809` maxDD `-14.784`
- `market_context_high->commodity_1h` score `-1.3828` n `199` status `ready` deltaP `-2.2718` edge `-0.0053` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6104` n `197` status `ready` deltaP `-7.9671` edge `-0.0291` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3168` n `197` status `ready` deltaP `-6.5386` edge `-0.0447` maxDD `-14.3822`
- `market_context_high->metal_24h` score `-7.3056` n `189` status `ready` deltaP `-4.5387` edge `-0.1686` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.3458` n `189` status `ready` deltaP `8.259` edge `0.2025` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
