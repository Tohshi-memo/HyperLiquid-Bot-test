# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T15:07:31.644917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0565` n `12`; crypto_alt avg `-0.105` n `231`; crypto_major avg `-0.1845` n `8`; equity avg `-0.0169` n `127`; fx avg `0.0118` n `6`; index avg `0.0076` n `26`; metal avg `0.103` n `20`; unknown avg `-0.0304` n `793`
- 1h: commodity avg `0.1326` n `12`; crypto_alt avg `1.1322` n `231`; crypto_major avg `0.9108` n `8`; equity avg `0.4677` n `127`; fx avg `0.0408` n `6`; index avg `0.1327` n `26`; metal avg `0.305` n `20`; unknown avg `0.3188` n `793`
- 4h: commodity avg `-0.041` n `12`; crypto_alt avg `-0.3265` n `231`; crypto_major avg `-0.2154` n `8`; equity avg `-0.2931` n `127`; fx avg `-0.0288` n `6`; index avg `0.1062` n `26`; metal avg `0.1148` n `20`; unknown avg `-0.1484` n `792`
- 24h: commodity avg `0.0502` n `12`; crypto_alt avg `-1.1607` n `231`; crypto_major avg `-1.1108` n `8`; equity avg `-0.7396` n `127`; fx avg `-0.0636` n `6`; index avg `0.1213` n `26`; metal avg `0.7588` n `20`; unknown avg `0.3061` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
