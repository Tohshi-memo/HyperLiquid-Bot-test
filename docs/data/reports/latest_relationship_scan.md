# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T04:37:26.683043+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6373`

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

- `market_context_high->unknown_24h` score `5752.9679` n `64` status `ready` deltaP `-2.0833` edge `479.4528` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `281.1497` n `64` status `ready` deltaP `2.782` edge `23.4208` maxDD `-0.15`
- `news_risk_high->unknown_1h` score `81.592` n `108` status `ready` deltaP `-5.1951` edge `6.8626` maxDD `-0.9571`
- `market_context_high->equity_24h` score `17.614` n `64` status `ready` deltaP `34.375` edge `1.3247` maxDD `-3.8824`
- `news_risk_high->crypto_alt_24h` score `13.6045` n `97` status `ready` deltaP `32.2684` edge `1.0542` maxDD `-6.8493`
- `market_context_high->unknown_1h` score `11.738` n `64` status `ready` deltaP `3.9484` edge `0.9629` maxDD `-0.2178`
- `market_context_high->index_24h` score `6.4423` n `64` status `ready` deltaP `55.3819` edge `0.1813` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.2871` n `108` status `ready` deltaP `19.9695` edge `0.4461` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `2.8069` n `64` status `ready` deltaP `27.2866` edge `0.0854` maxDD `-0.3387`
- `market_context_high->commodity_24h` score `2.4472` n `64` status `ready` deltaP `35.0694` edge `0.1834` maxDD `-5.2761`
- `market_context_high->crypto_alt_24h` score `1.3623` n `64` status `ready` deltaP `-9.5486` edge `0.3384` maxDD `-9.5643`
- `market_context_high->equity_4h` score `1.2549` n `64` status `ready` deltaP `-0.6098` edge `0.2406` maxDD `-2.7191`
- `market_context_high->metal_4h` score `1.182` n `64` status `ready` deltaP `14.4436` edge `0.0447` maxDD `-0.7323`
- `market_context_high->crypto_major_4h` score `0.9333` n `64` status `ready` deltaP `19.7409` edge `0.1335` maxDD `-8.3027`
- `market_context_high->crypto_major_24h` score `0.8933` n `64` status `ready` deltaP `4.6875` edge `0.2083` maxDD `-7.0024`
- `news_risk_high->crypto_alt_1h` score `0.8421` n `108` status `ready` deltaP `8.8767` edge `0.1064` maxDD `-3.9659`
- `market_context_high->crypto_alt_4h` score `0.6571` n `64` status `ready` deltaP `13.7195` edge `0.1688` maxDD `-10.7483`
- `market_context_high->fx_1h` score `0.5894` n `64` status `ready` deltaP `14.128` edge `-0.0002` maxDD `-0.1407`
- `market_context_high->metal_1h` score `0.4837` n `64` status `ready` deltaP `7.2324` edge `0.0211` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.1048` n `64` status `ready` deltaP `6.936` edge `0.0016` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
