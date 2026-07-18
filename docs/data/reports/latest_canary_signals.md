# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T11:16:33.004660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `0.0222` n `230`; crypto_major avg `0.0271` n `8`; equity avg `0.0005` n `96`; fx avg `0.0` n `6`; index avg `0.0149` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.0028` n `770`
- 1h: commodity avg `0.0479` n `12`; crypto_alt avg `0.0325` n `230`; crypto_major avg `0.0979` n `8`; equity avg `-0.0` n `96`; fx avg `-0.0112` n `6`; index avg `0.0075` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.0176` n `769`
- 4h: commodity avg `0.1726` n `12`; crypto_alt avg `-0.1227` n `230`; crypto_major avg `0.0094` n `8`; equity avg `-0.1065` n `96`; fx avg `-0.0088` n `6`; index avg `0.0676` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.1078` n `769`
- 24h: commodity avg `0.7136` n `12`; crypto_alt avg `-0.4806` n `230`; crypto_major avg `0.2613` n `8`; equity avg `0.6396` n `96`; fx avg `0.0213` n `6`; index avg `0.1811` n `25`; metal avg `0.279` n `20`; unknown avg `0.0987` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
