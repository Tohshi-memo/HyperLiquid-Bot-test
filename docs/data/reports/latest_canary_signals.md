# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T05:37:27.568935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.035` n `230`; crypto_major avg `-0.0237` n `8`; equity avg `-0.006` n `96`; fx avg `-0.0051` n `6`; index avg `-0.0041` n `25`; metal avg `0.0017` n `20`; unknown avg `0.1309` n `769`
- 1h: commodity avg `-0.0104` n `12`; crypto_alt avg `-0.0061` n `230`; crypto_major avg `-0.0079` n `8`; equity avg `0.011` n `96`; fx avg `-0.0005` n `6`; index avg `0.0186` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.3021` n `769`
- 4h: commodity avg `-0.0411` n `12`; crypto_alt avg `-0.3283` n `230`; crypto_major avg `-0.0548` n `8`; equity avg `-0.0639` n `96`; fx avg `-0.0108` n `6`; index avg `0.0811` n `25`; metal avg `-0.0066` n `20`; unknown avg `-0.295` n `769`
- 24h: commodity avg `0.7198` n `12`; crypto_alt avg `-0.2625` n `230`; crypto_major avg `0.4069` n `8`; equity avg `1.4771` n `96`; fx avg `0.0621` n `6`; index avg `0.2372` n `25`; metal avg `0.2839` n `20`; unknown avg `0.2979` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
