# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T12:37:29.051684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.5372` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0281` n `12`; crypto_alt avg `1.8481` n `233`; crypto_major avg `1.4706` n `8`; equity avg `0.3637` n `136`; fx avg `-0.0071` n `6`; index avg `0.0147` n `26`; metal avg `0.0322` n `20`; unknown avg `1.6494` n `790`
- 1h: commodity avg `-0.0742` n `12`; crypto_alt avg `1.8907` n `233`; crypto_major avg `1.5781` n `8`; equity avg `0.4152` n `136`; fx avg `-0.0004` n `6`; index avg `0.0423` n `26`; metal avg `0.0409` n `20`; unknown avg `0.8172` n `788`
- 4h: commodity avg `-0.1947` n `12`; crypto_alt avg `0.4121` n `233`; crypto_major avg `0.5912` n `8`; equity avg `0.2098` n `136`; fx avg `-0.0415` n `6`; index avg `0.0313` n `26`; metal avg `-0.0833` n `20`; unknown avg `0.4323` n `788`
- 24h: commodity avg `-0.2527` n `12`; crypto_alt avg `0.2311` n `233`; crypto_major avg `0.2918` n `8`; equity avg `0.5026` n `136`; fx avg `-0.109` n `6`; index avg `0.15` n `26`; metal avg `0.0195` n `20`; unknown avg `2.048` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
