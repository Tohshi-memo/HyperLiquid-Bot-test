# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T07:52:26.578372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.0153` n `230`; crypto_major avg `0.027` n `8`; equity avg `-0.0013` n `96`; fx avg `-0.0007` n `6`; index avg `0.0023` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.1191` n `769`
- 1h: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.1071` n `230`; crypto_major avg `0.0334` n `8`; equity avg `0.0498` n `96`; fx avg `0.0056` n `6`; index avg `-0.0146` n `25`; metal avg `0.0171` n `20`; unknown avg `-0.1191` n `769`
- 4h: commodity avg `0.0071` n `12`; crypto_alt avg `-0.4248` n `230`; crypto_major avg `-0.1046` n `8`; equity avg `-0.1286` n `96`; fx avg `0.0021` n `6`; index avg `-0.0188` n `25`; metal avg `0.0198` n `20`; unknown avg `-0.098` n `737`
- 24h: commodity avg `0.8604` n `12`; crypto_alt avg `-0.0856` n `230`; crypto_major avg `0.6391` n `8`; equity avg `1.4119` n `96`; fx avg `0.0381` n `6`; index avg `0.1578` n `25`; metal avg `0.2302` n `20`; unknown avg `0.2596` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
