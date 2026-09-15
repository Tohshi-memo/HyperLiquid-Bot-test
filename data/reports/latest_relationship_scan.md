# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T00:07:27.303499+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10512`

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

- `news_risk_high->unknown_4h` score `397.8704` n `78` status `ready` deltaP `-22.4554` edge `33.3949` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.6703` n `78` status `ready` deltaP `18.9236` edge `1.9297` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.3638` n `78` status `ready` deltaP `44.6448` edge `1.5218` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.8225` n `78` status `ready` deltaP `32.265` edge `1.2505` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.1431` n `78` status `ready` deltaP `43.9503` edge `1.0636` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7267` n `78` status `ready` deltaP `61.9391` edge `0.3319` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4481` n `78` status `ready` deltaP `37.7938` edge `0.3308` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9467` n `52` status `ready` deltaP `37.6736` edge `0.2444` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9467` n `52` status `ready` deltaP `37.6736` edge `0.2444` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8042` n `136` status `ready` deltaP `31.056` edge `0.241` maxDD `-0.8155`
- `risk_on_high->fx_24h` score `4.2808` n `52` status `ready` deltaP `48.2505` edge `0.0393` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.2808` n `52` status `ready` deltaP `48.2505` edge `0.0393` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.8796` n `136` status `ready` deltaP `45.0265` edge `0.0447` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9695` n `52` status `ready` deltaP `25.6801` edge `0.0279` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9695` n `52` status `ready` deltaP `25.6801` edge `0.0279` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7699` n `137` status `ready` deltaP `21.09` edge `0.0487` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7287` n `137` status `ready` deltaP `12.2132` edge `0.017` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7245` n `78` status `ready` deltaP `17.2686` edge `0.0406` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2133` n `52` status `ready` deltaP `6.5984` edge `0.009` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2133` n `52` status `ready` deltaP `6.5984` edge `0.009` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
