# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T13:22:25.659626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0684` n `12`; crypto_alt avg `-0.0751` n `230`; crypto_major avg `-0.2102` n `8`; equity avg `-0.0175` n `121`; fx avg `-0.0008` n `6`; index avg `0.0008` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.0065` n `794`
- 1h: commodity avg `-0.0446` n `12`; crypto_alt avg `-0.7322` n `230`; crypto_major avg `-0.6157` n `8`; equity avg `-0.0393` n `121`; fx avg `-0.0035` n `6`; index avg `-0.0048` n `25`; metal avg `0.0096` n `20`; unknown avg `-0.107` n `794`
- 4h: commodity avg `-0.0714` n `12`; crypto_alt avg `-0.8402` n `230`; crypto_major avg `-0.6828` n `8`; equity avg `-0.0783` n `121`; fx avg `0.0109` n `6`; index avg `0.0054` n `25`; metal avg `0.026` n `20`; unknown avg `0.1329` n `794`
- 24h: commodity avg `-0.0621` n `12`; crypto_alt avg `1.4051` n `230`; crypto_major avg `3.5847` n `8`; equity avg `-0.7996` n `121`; fx avg `0.0601` n `6`; index avg `-0.0867` n `25`; metal avg `-0.1478` n `20`; unknown avg `0.7824` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
