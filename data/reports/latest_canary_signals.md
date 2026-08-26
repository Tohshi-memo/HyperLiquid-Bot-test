# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T20:07:46.350046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `-0.0858` n `231`; crypto_major avg `0.0744` n `8`; equity avg `0.3028` n `122`; fx avg `-0.0004` n `6`; index avg `0.0112` n `25`; metal avg `0.0069` n `20`; unknown avg `0.0122` n `797`
- 1h: commodity avg `0.0184` n `12`; crypto_alt avg `0.0176` n `231`; crypto_major avg `0.217` n `8`; equity avg `0.204` n `122`; fx avg `-0.0006` n `6`; index avg `-0.0062` n `25`; metal avg `0.0066` n `20`; unknown avg `0.0519` n `797`
- 4h: commodity avg `-0.2303` n `12`; crypto_alt avg `0.3045` n `231`; crypto_major avg `0.4612` n `8`; equity avg `0.7293` n `122`; fx avg `-0.0123` n `6`; index avg `0.0734` n `25`; metal avg `-0.0352` n `20`; unknown avg `0.1267` n `797`
- 24h: commodity avg `0.3794` n `12`; crypto_alt avg `-1.0654` n `231`; crypto_major avg `-1.0828` n `8`; equity avg `0.0501` n `122`; fx avg `-0.0524` n `6`; index avg `0.0234` n `25`; metal avg `-0.4218` n `20`; unknown avg `0.5964` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
