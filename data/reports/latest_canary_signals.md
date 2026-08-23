# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T11:37:28.545591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8447` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5535` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `0.1329` n `230`; crypto_major avg `0.1879` n `8`; equity avg `0.0178` n `121`; fx avg `0.0026` n `6`; index avg `0.0031` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0263` n `795`
- 1h: commodity avg `-0.0052` n `12`; crypto_alt avg `0.7248` n `230`; crypto_major avg `0.6458` n `8`; equity avg `0.0969` n `121`; fx avg `-0.0047` n `6`; index avg `0.0013` n `25`; metal avg `0.0287` n `20`; unknown avg `0.1684` n `795`
- 4h: commodity avg `-0.0213` n `12`; crypto_alt avg `2.7401` n `230`; crypto_major avg `1.8591` n `8`; equity avg `0.3056` n `121`; fx avg `-0.0924` n `6`; index avg `0.0384` n `25`; metal avg `0.0144` n `20`; unknown avg `0.5867` n `794`
- 24h: commodity avg `-0.0001` n `12`; crypto_alt avg `0.2047` n `230`; crypto_major avg `1.1544` n `8`; equity avg `0.4457` n `121`; fx avg `0.0318` n `6`; index avg `0.0328` n `25`; metal avg `0.0588` n `20`; unknown avg `3.0018` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
