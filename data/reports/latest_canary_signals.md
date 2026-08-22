# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T22:57:48.885557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.0085` n `230`; crypto_major avg `-0.2563` n `8`; equity avg `0.0091` n `121`; fx avg `0.0035` n `6`; index avg `0.0024` n `25`; metal avg `-0.0172` n `20`; unknown avg `0.0539` n `794`
- 1h: commodity avg `0.0164` n `12`; crypto_alt avg `0.9051` n `230`; crypto_major avg `0.3378` n `8`; equity avg `-0.0007` n `121`; fx avg `0.0187` n `6`; index avg `0.0033` n `25`; metal avg `-0.0184` n `20`; unknown avg `0.3743` n `794`
- 4h: commodity avg `0.0996` n `12`; crypto_alt avg `-0.6217` n `230`; crypto_major avg `-0.341` n `8`; equity avg `0.0843` n `121`; fx avg `0.0344` n `6`; index avg `-0.0026` n `25`; metal avg `0.0027` n `20`; unknown avg `0.2734` n `794`
- 24h: commodity avg `0.0541` n `12`; crypto_alt avg `-2.272` n `230`; crypto_major avg `-0.5816` n `8`; equity avg `-0.4293` n `121`; fx avg `0.0949` n `6`; index avg `-0.0647` n `25`; metal avg `-0.0725` n `20`; unknown avg `1.8326` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
