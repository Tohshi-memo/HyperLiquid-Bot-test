# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T22:52:27.465771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `-0.093` n `228`; crypto_major avg `0.04` n `8`; equity avg `0.0454` n `74`; fx avg `-0.0121` n `6`; index avg `0.0248` n `23`; metal avg `0.0059` n `18`; unknown avg `-0.4527` n `517`
- 1h: commodity avg `-0.1341` n `12`; crypto_alt avg `-0.956` n `228`; crypto_major avg `-0.6775` n `8`; equity avg `-0.2001` n `74`; fx avg `0.3431` n `6`; index avg `-0.2369` n `23`; metal avg `-0.144` n `18`; unknown avg `-0.7178` n `517`
- 4h: commodity avg `0.087` n `12`; crypto_alt avg `-0.7459` n `228`; crypto_major avg `-0.234` n `8`; equity avg `-0.408` n `74`; fx avg `-0.0264` n `6`; index avg `-0.1822` n `23`; metal avg `-0.0212` n `18`; unknown avg `-0.9804` n `517`
- 24h: commodity avg `-0.6975` n `12`; crypto_alt avg `0.6458` n `228`; crypto_major avg `1.4039` n `8`; equity avg `1.829` n `74`; fx avg `-0.2786` n `6`; index avg `0.987` n `23`; metal avg `0.0855` n `18`; unknown avg `-3.0663` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
