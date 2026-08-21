# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T15:22:31.001156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.5268` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1259` n `12`; crypto_alt avg `0.0331` n `230`; crypto_major avg `0.12` n `8`; equity avg `0.1311` n `121`; fx avg `0.0123` n `6`; index avg `-0.0066` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.0097` n `793`
- 1h: commodity avg `0.0687` n `12`; crypto_alt avg `0.7802` n `230`; crypto_major avg `0.8553` n `8`; equity avg `0.3106` n `121`; fx avg `-0.0035` n `6`; index avg `0.0344` n `25`; metal avg `-0.1339` n `20`; unknown avg `0.0001` n `793`
- 4h: commodity avg `0.0074` n `12`; crypto_alt avg `1.6544` n `230`; crypto_major avg `0.9703` n `8`; equity avg `-0.5565` n `121`; fx avg `-0.0116` n `6`; index avg `-0.0802` n `25`; metal avg `-0.1674` n `20`; unknown avg `0.0943` n `793`
- 24h: commodity avg `0.3326` n `12`; crypto_alt avg `8.0911` n `230`; crypto_major avg `6.2212` n `8`; equity avg `1.0141` n `121`; fx avg `-0.0783` n `6`; index avg `0.0589` n `25`; metal avg `0.455` n `20`; unknown avg `2.9254` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2393`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1956`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
