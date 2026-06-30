# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T00:08:04.412035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.0684` n `228`; crypto_major avg `-0.0487` n `8`; equity avg `0.0505` n `88`; fx avg `0.0487` n `6`; index avg `0.0285` n `23`; metal avg `-0.131` n `20`; unknown avg `0.0828` n `765`
- 1h: commodity avg `0.0346` n `12`; crypto_alt avg `0.0118` n `228`; crypto_major avg `-0.1946` n `8`; equity avg `0.0201` n `88`; fx avg `0.0335` n `6`; index avg `0.0312` n `23`; metal avg `-0.1434` n `20`; unknown avg `0.0613` n `765`
- 4h: commodity avg `-0.0456` n `12`; crypto_alt avg `-0.4989` n `228`; crypto_major avg `-0.5958` n `8`; equity avg `0.1906` n `88`; fx avg `0.0617` n `6`; index avg `0.0274` n `23`; metal avg `-0.0224` n `20`; unknown avg `0.8082` n `763`
- 24h: commodity avg `-0.1313` n `12`; crypto_alt avg `1.7103` n `228`; crypto_major avg `3.0067` n `8`; equity avg `1.9603` n `88`; fx avg `0.2318` n `6`; index avg `0.2715` n `23`; metal avg `-0.3071` n `20`; unknown avg `1.3526` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
