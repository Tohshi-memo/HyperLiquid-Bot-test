# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T06:22:36.670900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0423` n `12`; crypto_alt avg `0.2154` n `230`; crypto_major avg `0.1663` n `8`; equity avg `0.2064` n `120`; fx avg `0.037` n `6`; index avg `0.0361` n `25`; metal avg `0.1024` n `20`; unknown avg `0.0375` n `789`
- 1h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.0647` n `230`; crypto_major avg `-0.005` n `8`; equity avg `-0.1238` n `120`; fx avg `0.0233` n `6`; index avg `0.0032` n `25`; metal avg `0.0785` n `20`; unknown avg `-0.0151` n `757`
- 4h: commodity avg `-0.0268` n `12`; crypto_alt avg `0.1567` n `230`; crypto_major avg `0.0398` n `8`; equity avg `-0.7734` n `120`; fx avg `-0.0413` n `6`; index avg `-0.0691` n `25`; metal avg `-0.0711` n `20`; unknown avg `-0.1287` n `757`
- 24h: commodity avg `0.2304` n `12`; crypto_alt avg `0.2083` n `230`; crypto_major avg `-0.0856` n `8`; equity avg `-3.4337` n `120`; fx avg `-0.158` n `6`; index avg `-0.4831` n `25`; metal avg `-0.6607` n `20`; unknown avg `-0.2136` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
