# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T15:37:30.395453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.6513` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.5834` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0612` n `12`; crypto_alt avg `0.3764` n `229`; crypto_major avg `0.4166` n `8`; equity avg `-0.025` n `91`; fx avg `-0.0037` n `6`; index avg `-0.0179` n `25`; metal avg `0.0326` n `20`; unknown avg `-0.0481` n `755`
- 1h: commodity avg `-0.0498` n `12`; crypto_alt avg `1.3788` n `229`; crypto_major avg `1.5995` n `8`; equity avg `0.3303` n `91`; fx avg `-0.0223` n `6`; index avg `-0.0063` n `25`; metal avg `0.0161` n `20`; unknown avg `0.3214` n `755`
- 4h: commodity avg `0.2301` n `12`; crypto_alt avg `0.1482` n `229`; crypto_major avg `0.9947` n `8`; equity avg `-1.6566` n `91`; fx avg `-0.0261` n `6`; index avg `-0.198` n `25`; metal avg `-0.0745` n `20`; unknown avg `0.101` n `755`
- 24h: commodity avg `0.3925` n `12`; crypto_alt avg `0.6039` n `229`; crypto_major avg `1.3366` n `8`; equity avg `-3.639` n `90`; fx avg `-0.1915` n `6`; index avg `-0.7461` n `25`; metal avg `-0.1129` n `20`; unknown avg `0.1799` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
