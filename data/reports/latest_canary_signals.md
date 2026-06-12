# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T14:07:36.162706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0333` n `12`; crypto_alt avg `0.6952` n `228`; crypto_major avg `0.6863` n `8`; equity avg `0.8231` n `74`; fx avg `-0.0125` n `6`; index avg `0.5878` n `23`; metal avg `0.1691` n `18`; unknown avg `5.8165` n `643`
- 1h: commodity avg `0.6879` n `12`; crypto_alt avg `-0.3976` n `228`; crypto_major avg `0.0596` n `8`; equity avg `0.0454` n `74`; fx avg `0.0005` n `6`; index avg `0.2599` n `23`; metal avg `-0.0612` n `18`; unknown avg `12.1786` n `643`
- 4h: commodity avg `1.483` n `12`; crypto_alt avg `-0.7731` n `228`; crypto_major avg `-0.0251` n `8`; equity avg `-0.8368` n `74`; fx avg `-0.013` n `6`; index avg `-0.0432` n `23`; metal avg `-0.8186` n `18`; unknown avg `15.2048` n `643`
- 24h: commodity avg `-1.143` n `12`; crypto_alt avg `1.3459` n `228`; crypto_major avg `1.968` n `8`; equity avg `1.764` n `74`; fx avg `0.0301` n `6`; index avg `1.3611` n `23`; metal avg `2.347` n `18`; unknown avg `20.902` n `514`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
