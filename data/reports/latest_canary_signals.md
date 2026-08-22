# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T19:22:27.115431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5997` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.1547` n `230`; crypto_major avg `-0.095` n `8`; equity avg `-0.0069` n `121`; fx avg `-0.0016` n `6`; index avg `-0.0034` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.0737` n `794`
- 1h: commodity avg `-0.001` n `12`; crypto_alt avg `-0.4897` n `230`; crypto_major avg `-0.3416` n `8`; equity avg `0.0069` n `121`; fx avg `0.014` n `6`; index avg `-0.0066` n `25`; metal avg `-0.012` n `20`; unknown avg `0.1059` n `794`
- 4h: commodity avg `0.0177` n `12`; crypto_alt avg `1.2139` n `230`; crypto_major avg `1.6097` n `8`; equity avg `0.1116` n `121`; fx avg `0.0307` n `6`; index avg `-0.0063` n `25`; metal avg `0.01` n `20`; unknown avg `1.466` n `794`
- 24h: commodity avg `-0.0252` n `12`; crypto_alt avg `1.5732` n `230`; crypto_major avg `3.8883` n `8`; equity avg `-0.4125` n `121`; fx avg `0.0504` n `6`; index avg `-0.0524` n `25`; metal avg `-0.1241` n `20`; unknown avg `1.9945` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
