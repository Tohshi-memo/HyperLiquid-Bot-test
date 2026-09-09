# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T17:52:34.211130+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10148`

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

- `risk_on_high->crypto_alt_24h` score `10.26` n `117` status `ready` deltaP `23.1571` edge `0.7236` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `10.26` n `117` status `ready` deltaP `23.1571` edge `0.7236` maxDD `-0.8386`
- `risk_on_high->crypto_alt_4h` score `5.8491` n `117` status `ready` deltaP `33.0741` edge `0.3041` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.8491` n `117` status `ready` deltaP `33.0741` edge `0.3041` maxDD `-1.9733`
- `market_context_high->crypto_alt_24h` score `5.2125` n `241` status `ready` deltaP `15.8123` edge `0.4117` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `5.1838` n `117` status `ready` deltaP `19.0171` edge `0.9446` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.1838` n `117` status `ready` deltaP `19.0171` edge `0.9446` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `4.0814` n `117` status `ready` deltaP `23.847` edge `0.267` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.0814` n `117` status `ready` deltaP `23.847` edge `0.267` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.2786` n `117` status `ready` deltaP `23.4776` edge `0.0376` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.2786` n `117` status `ready` deltaP `23.4776` edge `0.0376` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.5572` n `241` status `ready` deltaP `18.5728` edge `0.0453` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.8794` n `117` status `ready` deltaP `3.4982` edge `0.0852` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8794` n `117` status `ready` deltaP `3.4982` edge `0.0852` maxDD `-1.1521`
- `market_context_high->equity_24h` score `0.7992` n `241` status `ready` deltaP `6.9444` edge `0.0203` maxDD `0.0`
- `risk_on_high->metal_24h` score `0.7177` n `117` status `ready` deltaP `19.7383` edge `0.076` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7177` n `117` status `ready` deltaP `19.7383` edge `0.076` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.3226` n `117` status `ready` deltaP `13.4744` edge `-0.0098` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.3226` n `117` status `ready` deltaP `13.4744` edge `-0.0098` maxDD `-2.2516`
- `risk_on_high->index_1h` score `0.2154` n `117` status `ready` deltaP `10.0172` edge `-0.0028` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
