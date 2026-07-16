# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T07:52:30.380407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.1063` n `230`; crypto_major avg `-0.1548` n `8`; equity avg `-0.162` n `94`; fx avg `-0.0003` n `6`; index avg `-0.0348` n `25`; metal avg `0.0094` n `20`; unknown avg `-0.0375` n `768`
- 1h: commodity avg `0.0179` n `12`; crypto_alt avg `-0.6062` n `230`; crypto_major avg `-0.8234` n `8`; equity avg `-0.4621` n `94`; fx avg `0.0037` n `6`; index avg `-0.0745` n `25`; metal avg `-0.0888` n `20`; unknown avg `-0.0832` n `768`
- 4h: commodity avg `-0.0354` n `12`; crypto_alt avg `-0.5718` n `230`; crypto_major avg `-0.42` n `8`; equity avg `-0.6921` n `94`; fx avg `-0.0533` n `6`; index avg `-0.1112` n `25`; metal avg `-0.1769` n `20`; unknown avg `0.0519` n `752`
- 24h: commodity avg `-0.1861` n `12`; crypto_alt avg `-0.1903` n `230`; crypto_major avg `-0.2076` n `8`; equity avg `-2.8044` n `93`; fx avg `0.0638` n `6`; index avg `-0.5049` n `25`; metal avg `-0.0702` n `20`; unknown avg `-0.1667` n `749`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
