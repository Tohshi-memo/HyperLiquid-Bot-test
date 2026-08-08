# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T02:52:32.296733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `0.0087` n `230`; crypto_major avg `-0.0064` n `8`; equity avg `-0.0418` n `112`; fx avg `-0.0006` n `6`; index avg `0.0005` n `25`; metal avg `-0.01` n `20`; unknown avg `0.1114` n `783`
- 1h: commodity avg `0.028` n `12`; crypto_alt avg `0.0177` n `230`; crypto_major avg `-0.0139` n `8`; equity avg `-0.0782` n `112`; fx avg `-0.0068` n `6`; index avg `0.0041` n `25`; metal avg `-0.025` n `20`; unknown avg `-0.0281` n `783`
- 4h: commodity avg `0.0101` n `12`; crypto_alt avg `0.2511` n `230`; crypto_major avg `0.1769` n `8`; equity avg `0.0417` n `112`; fx avg `-0.008` n `6`; index avg `0.0023` n `25`; metal avg `-0.0069` n `20`; unknown avg `-0.2314` n `782`
- 24h: commodity avg `-0.1526` n `12`; crypto_alt avg `-0.4824` n `230`; crypto_major avg `0.044` n `8`; equity avg `1.5709` n `112`; fx avg `-0.0783` n `6`; index avg `0.2143` n `25`; metal avg `0.358` n `20`; unknown avg `-0.0488` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
