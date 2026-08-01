# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T22:07:25.248069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1619` n `12`; crypto_alt avg `0.0527` n `230`; crypto_major avg `0.0358` n `8`; equity avg `0.0096` n `102`; fx avg `0.0053` n `6`; index avg `-0.0013` n `25`; metal avg `0.003` n `20`; unknown avg `0.0746` n `782`
- 1h: commodity avg `-0.2204` n `12`; crypto_alt avg `0.2938` n `230`; crypto_major avg `0.193` n `8`; equity avg `0.358` n `102`; fx avg `0.0273` n `6`; index avg `0.0459` n `25`; metal avg `0.0342` n `20`; unknown avg `0.1308` n `782`
- 4h: commodity avg `-0.2749` n `12`; crypto_alt avg `-0.1578` n `230`; crypto_major avg `-0.1188` n `8`; equity avg `0.2346` n `102`; fx avg `0.0315` n `6`; index avg `0.025` n `25`; metal avg `0.0795` n `20`; unknown avg `-0.0091` n `782`
- 24h: commodity avg `-0.1755` n `12`; crypto_alt avg `-0.2011` n `230`; crypto_major avg `-0.7342` n `8`; equity avg `-0.0211` n `102`; fx avg `-0.0193` n `6`; index avg `0.0092` n `25`; metal avg `0.0544` n `20`; unknown avg `0.0278` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
