# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T14:52:34.123875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0458` n `13`; crypto_alt avg `0.2436` n `239`; crypto_major avg `0.1086` n `8`; equity avg `0.2137` n `157`; fx avg `0.0182` n `6`; index avg `-0.0192` n `27`; metal avg `-0.0185` n `20`; unknown avg `10.8249` n `1264`
- 1h: commodity avg `0.2417` n `13`; crypto_alt avg `0.1797` n `239`; crypto_major avg `0.2675` n `8`; equity avg `0.3777` n `157`; fx avg `0.058` n `6`; index avg `-0.0372` n `27`; metal avg `-0.1856` n `20`; unknown avg `456.5581` n `1258`
- 4h: commodity avg `-0.5466` n `13`; crypto_alt avg `1.3595` n `239`; crypto_major avg `1.1807` n `8`; equity avg `1.3395` n `157`; fx avg `0.0377` n `6`; index avg `0.1154` n `27`; metal avg `0.3255` n `20`; unknown avg `97.0126` n `1226`
- 24h: commodity avg `-0.3475` n `13`; crypto_alt avg `-0.3428` n `239`; crypto_major avg `0.1114` n `8`; equity avg `-0.5195` n `157`; fx avg `0.0516` n `6`; index avg `-0.0722` n `27`; metal avg `-0.4484` n `20`; unknown avg `-0.0661` n `1020`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
