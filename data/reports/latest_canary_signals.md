# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T09:07:32.607803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1303` n `12`; crypto_alt avg `0.0423` n `230`; crypto_major avg `-0.0386` n `8`; equity avg `0.1037` n `94`; fx avg `0.0004` n `6`; index avg `0.0281` n `25`; metal avg `0.0224` n `20`; unknown avg `-0.0327` n `762`
- 1h: commodity avg `-0.1151` n `12`; crypto_alt avg `-0.2618` n `230`; crypto_major avg `-0.3041` n `8`; equity avg `0.136` n `94`; fx avg `0.0128` n `6`; index avg `0.0703` n `25`; metal avg `0.0726` n `20`; unknown avg `-0.1132` n `762`
- 4h: commodity avg `-0.1271` n `12`; crypto_alt avg `-1.0593` n `230`; crypto_major avg `-0.9266` n `8`; equity avg `-0.6556` n `94`; fx avg `-0.044` n `6`; index avg `-0.0408` n `25`; metal avg `-0.0418` n `20`; unknown avg `-0.1091` n `746`
- 24h: commodity avg `-0.1357` n `12`; crypto_alt avg `-0.7772` n `230`; crypto_major avg `-0.9362` n `8`; equity avg `-2.7516` n `93`; fx avg `0.0619` n `6`; index avg `-0.4484` n `25`; metal avg `-0.0736` n `20`; unknown avg `-0.1401` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
