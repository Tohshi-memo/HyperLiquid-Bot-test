# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T09:07:26.991212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.601` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.5997` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.5262` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `-0.6565` n `230`; crypto_major avg `-0.4069` n `8`; equity avg `-0.0244` n `121`; fx avg `0.0019` n `6`; index avg `-0.005` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.12` n `794`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `-1.8655` n `230`; crypto_major avg `-1.6016` n `8`; equity avg `-0.0754` n `121`; fx avg `0.0098` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.322` n `794`
- 4h: commodity avg `0.0339` n `12`; crypto_alt avg `-0.4793` n `230`; crypto_major avg `-0.4061` n `8`; equity avg `0.2833` n `121`; fx avg `-0.0031` n `6`; index avg `0.0312` n `25`; metal avg `0.1691` n `20`; unknown avg `0.85` n `778`
- 24h: commodity avg `0.1706` n `12`; crypto_alt avg `3.6458` n `230`; crypto_major avg `4.1048` n `8`; equity avg `-0.6971` n `121`; fx avg `0.0666` n `6`; index avg `-0.0954` n `25`; metal avg `-0.2344` n `20`; unknown avg `1.352` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
