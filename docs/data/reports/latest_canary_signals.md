# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T14:07:20.182519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1186` n `12`; crypto_alt avg `0.231` n `228`; crypto_major avg `0.164` n `8`; equity avg `0.0912` n `67`; fx avg `-0.0031` n `6`; index avg `0.0087` n `23`; metal avg `0.2205` n `18`; unknown avg `0.8913` n `405`
- 1h: commodity avg `-0.1084` n `12`; crypto_alt avg `0.3366` n `228`; crypto_major avg `0.1928` n `8`; equity avg `0.1038` n `67`; fx avg `-0.0132` n `6`; index avg `0.0413` n `23`; metal avg `0.1743` n `18`; unknown avg `0.9952` n `405`
- 4h: commodity avg `0.3759` n `12`; crypto_alt avg `0.4401` n `228`; crypto_major avg `0.1842` n `8`; equity avg `0.0989` n `67`; fx avg `0.0151` n `6`; index avg `0.1266` n `23`; metal avg `-0.0237` n `18`; unknown avg `0.7566` n `397`
- 24h: commodity avg `0.0145` n `12`; crypto_alt avg `1.7231` n `228`; crypto_major avg `0.531` n `8`; equity avg `0.6445` n `67`; fx avg `-0.0078` n `6`; index avg `0.2229` n `23`; metal avg `0.9084` n `18`; unknown avg `1.781` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
