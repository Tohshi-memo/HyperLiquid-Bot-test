# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T11:40:53.632195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9379` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6402` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.1931` n `230`; crypto_major avg `0.2843` n `8`; equity avg `0.0296` n `121`; fx avg `-0.0049` n `6`; index avg `0.004` n `25`; metal avg `0.0112` n `20`; unknown avg `-0.0028` n `795`
- 1h: commodity avg `-0.0069` n `12`; crypto_alt avg `0.7856` n `230`; crypto_major avg `0.7426` n `8`; equity avg `0.1087` n `121`; fx avg `-0.0122` n `6`; index avg `0.0022` n `25`; metal avg `0.0341` n `20`; unknown avg `0.14` n `795`
- 4h: commodity avg `-0.023` n `12`; crypto_alt avg `2.803` n `230`; crypto_major avg `1.9577` n `8`; equity avg `0.3175` n `121`; fx avg `-0.0999` n `6`; index avg `0.0393` n `25`; metal avg `0.0198` n `20`; unknown avg `0.5654` n `794`
- 24h: commodity avg `-0.0018` n `12`; crypto_alt avg `0.2666` n `230`; crypto_major avg `1.2515` n `8`; equity avg `0.4576` n `121`; fx avg `0.0243` n `6`; index avg `0.0337` n `25`; metal avg `0.0642` n `20`; unknown avg `2.9915` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
