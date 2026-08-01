# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T08:07:32.714793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `-0.0702` n `230`; crypto_major avg `-0.0246` n `8`; equity avg `0.0587` n `102`; fx avg `-0.0248` n `6`; index avg `0.0134` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0788` n `781`
- 1h: commodity avg `0.0227` n `12`; crypto_alt avg `-0.2744` n `230`; crypto_major avg `-0.1325` n `8`; equity avg `0.1007` n `102`; fx avg `0.0023` n `6`; index avg `0.0464` n `25`; metal avg `0.0242` n `20`; unknown avg `-0.0042` n `781`
- 4h: commodity avg `-0.0347` n `12`; crypto_alt avg `-0.3452` n `230`; crypto_major avg `-0.1895` n `8`; equity avg `0.1402` n `102`; fx avg `-0.007` n `6`; index avg `0.0442` n `25`; metal avg `0.0285` n `20`; unknown avg `-0.0717` n `765`
- 24h: commodity avg `0.9072` n `12`; crypto_alt avg `-0.2411` n `230`; crypto_major avg `-1.3713` n `8`; equity avg `-2.3197` n `102`; fx avg `-0.0139` n `6`; index avg `-0.2549` n `25`; metal avg `-0.1367` n `20`; unknown avg `4.8392` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
