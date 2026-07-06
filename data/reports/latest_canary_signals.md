# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T09:52:29.272325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `0.125` n `229`; crypto_major avg `0.0464` n `8`; equity avg `-0.0172` n `88`; fx avg `-0.0075` n `6`; index avg `-0.0032` n `25`; metal avg `0.0188` n `20`; unknown avg `0.0041` n `765`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.0517` n `229`; crypto_major avg `-0.3447` n `8`; equity avg `-0.0751` n `88`; fx avg `-0.0087` n `6`; index avg `-0.0051` n `25`; metal avg `-0.0837` n `20`; unknown avg `-0.0335` n `765`
- 4h: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.1687` n `229`; crypto_major avg `-0.5492` n `8`; equity avg `0.0328` n `88`; fx avg `0.0167` n `6`; index avg `0.0695` n `25`; metal avg `-0.0113` n `20`; unknown avg `-0.0779` n `731`
- 24h: commodity avg `-0.138` n `12`; crypto_alt avg `0.2028` n `229`; crypto_major avg `0.7577` n `8`; equity avg `-0.5754` n `88`; fx avg `0.0734` n `6`; index avg `0.0024` n `25`; metal avg `-0.2743` n `20`; unknown avg `1.1346` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
