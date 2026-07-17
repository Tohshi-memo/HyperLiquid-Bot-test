# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T23:22:32.374514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `0.1034` n `230`; crypto_major avg `0.1004` n `8`; equity avg `-0.0261` n `96`; fx avg `0.0085` n `6`; index avg `-0.0064` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.029` n `769`
- 1h: commodity avg `0.043` n `12`; crypto_alt avg `0.2061` n `230`; crypto_major avg `0.036` n `8`; equity avg `0.0079` n `96`; fx avg `0.0122` n `6`; index avg `-0.0023` n `25`; metal avg `0.0085` n `20`; unknown avg `-0.0519` n `769`
- 4h: commodity avg `0.1717` n `12`; crypto_alt avg `0.0133` n `230`; crypto_major avg `0.0744` n `8`; equity avg `-0.1553` n `96`; fx avg `-0.0556` n `6`; index avg `-0.0441` n `25`; metal avg `0.0668` n `20`; unknown avg `-0.1442` n `769`
- 24h: commodity avg `0.7387` n `12`; crypto_alt avg `-0.2238` n `230`; crypto_major avg `-0.3278` n `8`; equity avg `-0.8475` n `94`; fx avg `0.0453` n `6`; index avg `-0.2703` n `25`; metal avg `0.0276` n `20`; unknown avg `0.0982` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
