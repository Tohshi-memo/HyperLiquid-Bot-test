# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T03:37:28.092090+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6337`

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

- `market_context_high->unknown_24h` score `5279.0479` n `68` status `ready` deltaP `-4.2177` edge `439.9737` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `242.8538` n `68` status `ready` deltaP `0.4215` edge `20.2483` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `81.5128` n `108` status `ready` deltaP `-5.0454` edge `6.855` maxDD `-0.9571`
- `market_context_high->equity_24h` score `15.5222` n `68` status `ready` deltaP `30.1062` edge `1.2337` maxDD `-6.9377`
- `news_risk_high->crypto_alt_24h` score `14.3632` n `93` status `ready` deltaP `34.1454` edge `1.0926` maxDD `-6.531`
- `market_context_high->index_24h` score `5.9878` n `68` status `ready` deltaP `51.2459` edge `0.171` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.3981` n `108` status `ready` deltaP `20.4268` edge `0.4523` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `2.7721` n `68` status `ready` deltaP `27.2866` edge `0.0825` maxDD `-0.3387`
- `market_context_high->commodity_24h` score `1.5396` n `68` status `ready` deltaP `30.8415` edge `0.1443` maxDD `-7.8682`
- `market_context_high->metal_4h` score `1.2556` n `68` status `ready` deltaP `15.4232` edge `0.0443` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.8672` n `108` status `ready` deltaP `9.0264` edge `0.1075` maxDD `-3.9659`
- `market_context_high->equity_4h` score `0.792` n `68` status `ready` deltaP `-2.9412` edge `0.2199` maxDD `-3.5667`
- `market_context_high->metal_1h` score `0.6921` n `68` status `ready` deltaP `9.7481` edge `0.0217` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.6649` n `68` status `ready` deltaP `15.5513` edge `0.0` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.2862` n `68` status `ready` deltaP `9.1732` edge `0.0018` maxDD `-0.1285`
- `market_context_high->equity_1h` score `0.2092` n `68` status `ready` deltaP `-0.8718` edge `0.1202` maxDD `-2.3383`
- `market_context_high->crypto_major_4h` score `0.0894` n `68` status `ready` deltaP `15.8178` edge `0.0969` maxDD `-10.6046`
- `market_context_high->crypto_major_1h` score `-0.0801` n `68` status `ready` deltaP `3.6897` edge `0.0679` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.2816` n `68` status `ready` deltaP `1.224` edge `0.0198` maxDD `-0.4475`
- `market_context_high->crypto_alt_4h` score `-0.3743` n `68` status `ready` deltaP `10.1327` edge `0.1195` maxDD `-14.1367`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
