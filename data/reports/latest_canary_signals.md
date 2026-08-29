# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T12:07:27.260210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `0.0399` n `231`; crypto_major avg `-0.049` n `8`; equity avg `-0.016` n `127`; fx avg `0.0` n `6`; index avg `-0.0011` n `26`; metal avg `-0.002` n `20`; unknown avg `1.8182` n `789`
- 1h: commodity avg `0.0082` n `12`; crypto_alt avg `0.0808` n `231`; crypto_major avg `-0.0095` n `8`; equity avg `0.0071` n `127`; fx avg `-0.0022` n `6`; index avg `0.0058` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.0532` n `767`
- 4h: commodity avg `0.0307` n `12`; crypto_alt avg `-0.0111` n `231`; crypto_major avg `0.0962` n `8`; equity avg `-0.0093` n `127`; fx avg `-0.0176` n `6`; index avg `-0.0017` n `26`; metal avg `0.0067` n `20`; unknown avg `-0.0533` n `763`
- 24h: commodity avg `0.1539` n `12`; crypto_alt avg `-2.3513` n `231`; crypto_major avg `-2.2026` n `8`; equity avg `-1.2917` n `127`; fx avg `-0.0769` n `6`; index avg `-0.1306` n `26`; metal avg `-0.7469` n `20`; unknown avg `-0.636` n `746`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1946`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
