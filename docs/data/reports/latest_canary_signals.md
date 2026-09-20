# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T14:37:31.317005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `12`; crypto_alt avg `0.2045` n `234`; crypto_major avg `0.158` n `8`; equity avg `-0.0011` n `140`; fx avg `-0.0113` n `6`; index avg `-0.0028` n `26`; metal avg `0.0005` n `20`; unknown avg `1.8205` n `943`
- 1h: commodity avg `0.048` n `12`; crypto_alt avg `0.2455` n `234`; crypto_major avg `0.262` n `8`; equity avg `-0.0155` n `140`; fx avg `-0.0097` n `6`; index avg `-0.0092` n `26`; metal avg `0.0092` n `20`; unknown avg `1.7253` n `941`
- 4h: commodity avg `0.0196` n `12`; crypto_alt avg `0.3309` n `234`; crypto_major avg `0.3009` n `8`; equity avg `0.0114` n `140`; fx avg `-0.027` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0023` n `20`; unknown avg `2.2341` n `935`
- 24h: commodity avg `0.2639` n `12`; crypto_alt avg `-2.4629` n `234`; crypto_major avg `-2.445` n `8`; equity avg `-0.3161` n `140`; fx avg `-0.0648` n `6`; index avg `-0.0549` n `26`; metal avg `-0.0288` n `20`; unknown avg `1.7714` n `818`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
