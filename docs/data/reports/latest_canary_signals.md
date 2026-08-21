# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T11:07:29.586677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9778` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.905` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.049` n `12`; crypto_alt avg `0.0286` n `230`; crypto_major avg `0.1627` n `8`; equity avg `-0.1599` n `121`; fx avg `-0.0` n `6`; index avg `-0.0008` n `25`; metal avg `0.0423` n `20`; unknown avg `0.0292` n `793`
- 1h: commodity avg `0.0328` n `12`; crypto_alt avg `0.7816` n `230`; crypto_major avg `0.2506` n `8`; equity avg `-0.1598` n `121`; fx avg `0.004` n `6`; index avg `-0.015` n `25`; metal avg `0.0596` n `20`; unknown avg `0.042` n `793`
- 4h: commodity avg `0.2466` n `12`; crypto_alt avg `2.8048` n `230`; crypto_major avg `2.1405` n `8`; equity avg `0.2355` n `121`; fx avg `-0.0195` n `6`; index avg `-0.005` n `25`; metal avg `0.1627` n `20`; unknown avg `0.5157` n `793`
- 24h: commodity avg `0.183` n `12`; crypto_alt avg `7.4505` n `230`; crypto_major avg `7.2794` n `8`; equity avg `0.6302` n `121`; fx avg `-0.0819` n `6`; index avg `0.0291` n `25`; metal avg `0.8108` n `20`; unknown avg `2.5933` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.226`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
