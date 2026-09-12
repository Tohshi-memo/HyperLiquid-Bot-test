# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T18:07:29.969823+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12881`

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

- `market_context_high->unknown_24h` score `8386.6086` n `83` status `ready` deltaP `13.0418` edge `698.8023` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `5354.9329` n `43` status `ready` deltaP `15.4514` edge `446.1414` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5354.9329` n `43` status `ready` deltaP `15.4514` edge `446.1414` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.0668` n `82` status `ready` deltaP `-5.4002` edge `32.0004` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `20.909` n `68` status `ready` deltaP `46.4154` edge `1.5526` maxDD `-6.9028`
- `news_risk_high->crypto_alt_24h` score `17.1221` n `68` status `ready` deltaP `29.5854` edge `1.2784` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `16.6043` n `43` status `ready` deltaP `38.5457` edge `1.1497` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `16.6043` n `43` status `ready` deltaP `38.5457` edge `1.1497` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.4305` n `83` status `ready` deltaP `30.8965` edge `1.0793` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.7117` n `43` status `ready` deltaP `41.1458` edge `0.535` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.7117` n `43` status `ready` deltaP `41.1458` edge `0.535` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.4543` n `68` status `ready` deltaP `24.9693` edge `0.6956` maxDD `-2.9365`
- `market_context_high->equity_24h` score `9.3997` n `83` status `ready` deltaP `41.1458` edge `0.509` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4172` n `47` status `ready` deltaP `41.9402` edge `0.459` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4172` n `47` status `ready` deltaP `41.9402` edge `0.459` maxDD `-1.9733`
- `news_risk_high->index_24h` score `6.724` n `68` status `ready` deltaP `43.7091` edge `0.2866` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.485` n `68` status `ready` deltaP `41.2786` edge `0.3093` maxDD `-0.526`
- `risk_on_high->index_24h` score `4.9415` n `43` status `ready` deltaP `49.9677` edge `0.0829` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9415` n `43` status `ready` deltaP `49.9677` edge `0.0829` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.0975` n `47` status `ready` deltaP `36.6114` edge `0.1067` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
