# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T15:22:30.339505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.243` n `229`; crypto_major avg `-0.3328` n `8`; equity avg `-0.0803` n `88`; fx avg `-0.0107` n `6`; index avg `0.0096` n `25`; metal avg `-0.0334` n `20`; unknown avg `0.1999` n `765`
- 1h: commodity avg `-0.0853` n `12`; crypto_alt avg `0.451` n `229`; crypto_major avg `0.6539` n `8`; equity avg `0.0722` n `88`; fx avg `0.0088` n `6`; index avg `-0.0127` n `25`; metal avg `0.0342` n `20`; unknown avg `0.6895` n `765`
- 4h: commodity avg `-0.0174` n `12`; crypto_alt avg `0.4038` n `229`; crypto_major avg `0.3207` n `8`; equity avg `-0.1747` n `88`; fx avg `-0.0153` n `6`; index avg `0.0102` n `25`; metal avg `-0.0798` n `20`; unknown avg `1.1284` n `765`
- 24h: commodity avg `0.3833` n `12`; crypto_alt avg `2.6694` n `229`; crypto_major avg `2.3387` n `8`; equity avg `1.2945` n `88`; fx avg `-0.0716` n `6`; index avg `0.4368` n `25`; metal avg `0.5473` n `20`; unknown avg `7.8496` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
