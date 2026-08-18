# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T03:22:27.546658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `12`; crypto_alt avg `0.0155` n `230`; crypto_major avg `-0.0184` n `8`; equity avg `-0.1896` n `114`; fx avg `0.0162` n `6`; index avg `-0.0488` n `25`; metal avg `-0.0301` n `20`; unknown avg `-0.1394` n `793`
- 1h: commodity avg `0.0332` n `12`; crypto_alt avg `-0.6961` n `230`; crypto_major avg `-0.2014` n `8`; equity avg `-0.584` n `114`; fx avg `-0.0269` n `6`; index avg `-0.1222` n `25`; metal avg `-0.0562` n `20`; unknown avg `-0.0512` n `793`
- 4h: commodity avg `0.0307` n `12`; crypto_alt avg `-1.1304` n `230`; crypto_major avg `-0.5274` n `8`; equity avg `-1.7781` n `114`; fx avg `-0.0553` n `6`; index avg `-0.3018` n `25`; metal avg `-0.2085` n `20`; unknown avg `0.3354` n `793`
- 24h: commodity avg `0.631` n `12`; crypto_alt avg `-1.4463` n `230`; crypto_major avg `-0.0375` n `8`; equity avg `-1.271` n `114`; fx avg `-0.0354` n `6`; index avg `-0.2891` n `25`; metal avg `-0.1909` n `20`; unknown avg `0.0691` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
