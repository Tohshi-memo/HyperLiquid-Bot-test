# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T10:07:23.845337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `12`; crypto_alt avg `0.2051` n `230`; crypto_major avg `0.0765` n `8`; equity avg `0.0125` n `96`; fx avg `-0.0029` n `6`; index avg `0.0099` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.0281` n `769`
- 1h: commodity avg `0.0337` n `12`; crypto_alt avg `0.0641` n `230`; crypto_major avg `-0.0263` n `8`; equity avg `-0.056` n `96`; fx avg `-0.0039` n `6`; index avg `-0.0138` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0456` n `769`
- 4h: commodity avg `0.1154` n `12`; crypto_alt avg `-0.1268` n `230`; crypto_major avg `0.0369` n `8`; equity avg `-0.13` n `96`; fx avg `0.0044` n `6`; index avg `0.0157` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.1982` n `769`
- 24h: commodity avg `0.684` n `12`; crypto_alt avg `-0.645` n `230`; crypto_major avg `0.0425` n `8`; equity avg `0.6942` n `96`; fx avg `0.0278` n `6`; index avg `0.1894` n `25`; metal avg `0.1687` n `20`; unknown avg `0.1943` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
