# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T17:22:26.125111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `-0.3779` n `228`; crypto_major avg `-0.3453` n `8`; equity avg `-0.0548` n `88`; fx avg `0.0069` n `6`; index avg `-0.0029` n `23`; metal avg `-0.0037` n `20`; unknown avg `0.0645` n `764`
- 1h: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.6689` n `228`; crypto_major avg `-0.5177` n `8`; equity avg `-0.019` n `88`; fx avg `-0.0227` n `6`; index avg `-0.0015` n `23`; metal avg `-0.005` n `20`; unknown avg `0.2674` n `764`
- 4h: commodity avg `0.1127` n `12`; crypto_alt avg `-0.2681` n `228`; crypto_major avg `-0.5292` n `8`; equity avg `0.001` n `88`; fx avg `-0.0249` n `6`; index avg `-0.0257` n `23`; metal avg `-0.0393` n `20`; unknown avg `0.2508` n `764`
- 24h: commodity avg `0.4052` n `12`; crypto_alt avg `-0.9511` n `228`; crypto_major avg `-1.6301` n `8`; equity avg `0.1084` n `88`; fx avg `-0.0263` n `6`; index avg `-0.0441` n `23`; metal avg `-0.0439` n `20`; unknown avg `14.7175` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
