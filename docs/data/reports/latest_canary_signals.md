# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T10:02:53.625300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `0.1786` n `230`; crypto_major avg `0.0243` n `8`; equity avg `0.0065` n `96`; fx avg `-0.0029` n `6`; index avg `0.0025` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0229` n `769`
- 1h: commodity avg `0.0246` n `12`; crypto_alt avg `0.0376` n `230`; crypto_major avg `-0.0783` n `8`; equity avg `-0.0621` n `96`; fx avg `-0.0039` n `6`; index avg `-0.0213` n `25`; metal avg `0.002` n `20`; unknown avg `-0.0402` n `769`
- 4h: commodity avg `0.1064` n `12`; crypto_alt avg `-0.1533` n `230`; crypto_major avg `-0.0153` n `8`; equity avg `-0.136` n `96`; fx avg `0.0044` n `6`; index avg `0.0082` n `25`; metal avg `0.0086` n `20`; unknown avg `-0.2036` n `769`
- 24h: commodity avg `0.6748` n `12`; crypto_alt avg `-0.6717` n `230`; crypto_major avg `-0.009` n `8`; equity avg `0.688` n `96`; fx avg `0.0278` n `6`; index avg `0.1818` n `25`; metal avg `0.1692` n `20`; unknown avg `0.1883` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
