# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T07:52:28.451499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0979` n `12`; crypto_alt avg `0.2988` n `230`; crypto_major avg `0.132` n `8`; equity avg `0.1307` n `102`; fx avg `-0.03` n `6`; index avg `-0.0122` n `25`; metal avg `0.048` n `20`; unknown avg `0.0689` n `779`
- 1h: commodity avg `-0.0309` n `12`; crypto_alt avg `0.0743` n `230`; crypto_major avg `-0.4332` n `8`; equity avg `0.2887` n `102`; fx avg `0.0435` n `6`; index avg `0.0571` n `25`; metal avg `0.0051` n `20`; unknown avg `-0.0275` n `779`
- 4h: commodity avg `-0.0521` n `12`; crypto_alt avg `0.2141` n `230`; crypto_major avg `-0.3531` n `8`; equity avg `0.3832` n `102`; fx avg `-0.0744` n `6`; index avg `0.1216` n `25`; metal avg `0.008` n `20`; unknown avg `-0.0403` n `747`
- 24h: commodity avg `-0.4358` n `12`; crypto_alt avg `0.3133` n `230`; crypto_major avg `0.6174` n `8`; equity avg `8.8646` n `102`; fx avg `-0.1713` n `6`; index avg `1.3475` n `25`; metal avg `0.5956` n `20`; unknown avg `0.041` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
