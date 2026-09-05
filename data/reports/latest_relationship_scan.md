# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T15:37:41.415982+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10537`

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

- `risk_on_high->unknown_4h` score `21.931` n `140` status `ready` deltaP `2.0122` edge `1.9035` maxDD `-2.4797`
- `risk_on_and_context->unknown_4h` score `21.931` n `140` status `ready` deltaP `2.0122` edge `1.9035` maxDD `-2.4797`
- `market_context_high->unknown_4h` score `10.1142` n `228` status `ready` deltaP `4.3806` edge `0.9207` maxDD `-2.8974`
- `news_risk_high->crypto_alt_24h` score `7.2179` n `37` status `ready` deltaP `25.1783` edge `0.4606` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.7829` n `37` status `ready` deltaP `19.7917` edge `0.1833` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.5982` n `37` status `ready` deltaP `17.1803` edge `0.2266` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3795` n `37` status `ready` deltaP `24.1513` edge `0.0594` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8595` n `37` status `ready` deltaP `10.9715` edge `0.1019` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5967` n `37` status `ready` deltaP `13.2344` edge `0.0839` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2598` n `37` status `ready` deltaP `15.0146` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.2098` n `37` status `ready` deltaP `6.4655` edge `0.076` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1622` n `37` status `ready` deltaP `14.5736` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_alt_1h` score `1.0053` n `37` status `ready` deltaP `9.4757` edge `0.0471` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.943` n `37` status `ready` deltaP `16.5776` edge `0.288` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.6129` n `37` status `ready` deltaP `6.2459` edge `0.0423` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.543` n `37` status `ready` deltaP `15.6156` edge `0.0427` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.4687` n `181` status `ready` deltaP `14.3742` edge `0.3778` maxDD `-20.7654`
- `news_risk_high->commodity_1h` score `-0.0247` n `37` status `ready` deltaP `5.7251` edge `0.0033` maxDD `-0.9036`
- `risk_on_high->metal_1h` score `-0.0594` n `150` status `ready` deltaP `9.483` edge `0.0004` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0594` n `150` status `ready` deltaP `9.483` edge `0.0004` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
