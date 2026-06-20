# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T05:52:33.680675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.0442` n `228`; crypto_major avg `-0.042` n `8`; equity avg `0.0349` n `78`; fx avg `0.2956` n `6`; index avg `0.012` n `23`; metal avg `-0.0138` n `18`; unknown avg `-0.1768` n `687`
- 1h: commodity avg `0.0777` n `12`; crypto_alt avg `0.18` n `228`; crypto_major avg `0.355` n `8`; equity avg `0.1614` n `78`; fx avg `0.0139` n `6`; index avg `0.0364` n `23`; metal avg `-0.0012` n `18`; unknown avg `0.02` n `687`
- 4h: commodity avg `0.1967` n `12`; crypto_alt avg `0.1614` n `228`; crypto_major avg `0.7161` n `8`; equity avg `0.4442` n `78`; fx avg `-0.0231` n `6`; index avg `0.0719` n `23`; metal avg `0.0189` n `18`; unknown avg `0.0716` n `687`
- 24h: commodity avg `0.4813` n `12`; crypto_alt avg `-3.2815` n `228`; crypto_major avg `-3.6272` n `8`; equity avg `1.3254` n `78`; fx avg `-0.1079` n `6`; index avg `0.3454` n `23`; metal avg `-4.1165` n `18`; unknown avg `-0.4914` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
