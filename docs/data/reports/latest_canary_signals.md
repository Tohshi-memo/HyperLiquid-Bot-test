# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T21:52:32.228165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0313` n `12`; crypto_alt avg `0.1555` n `231`; crypto_major avg `0.1203` n `8`; equity avg `0.1635` n `124`; fx avg `-0.0018` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.0489` n `795`
- 1h: commodity avg `0.0056` n `12`; crypto_alt avg `1.1422` n `231`; crypto_major avg `1.1114` n `8`; equity avg `1.0372` n `124`; fx avg `0.0004` n `6`; index avg `0.1907` n `25`; metal avg `0.046` n `20`; unknown avg `0.7372` n `795`
- 4h: commodity avg `-0.126` n `12`; crypto_alt avg `1.3487` n `231`; crypto_major avg `1.0351` n `8`; equity avg `1.7673` n `124`; fx avg `-0.0145` n `6`; index avg `0.2654` n `25`; metal avg `0.0071` n `20`; unknown avg `0.3389` n `795`
- 24h: commodity avg `0.3073` n `12`; crypto_alt avg `1.0157` n `231`; crypto_major avg `0.6973` n `8`; equity avg `1.4212` n `124`; fx avg `-0.0566` n `6`; index avg `0.248` n `25`; metal avg `-0.3521` n `20`; unknown avg `0.9954` n `777`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
