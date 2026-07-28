# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T17:22:37.010006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6485` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1106` n `12`; crypto_alt avg `-0.2199` n `230`; crypto_major avg `-0.2565` n `8`; equity avg `-0.1532` n `102`; fx avg `-0.0059` n `6`; index avg `-0.0593` n `25`; metal avg `-0.0127` n `20`; unknown avg `0.1765` n `774`
- 1h: commodity avg `0.1929` n `12`; crypto_alt avg `-0.2471` n `230`; crypto_major avg `-0.0868` n `8`; equity avg `0.0843` n `102`; fx avg `0.0125` n `6`; index avg `-0.0431` n `25`; metal avg `-0.0762` n `20`; unknown avg `-0.0482` n `774`
- 4h: commodity avg `-0.5845` n `12`; crypto_alt avg `0.3808` n `230`; crypto_major avg `0.9795` n `8`; equity avg `-0.669` n `102`; fx avg `-0.0259` n `6`; index avg `0.0111` n `25`; metal avg `0.0904` n `20`; unknown avg `-0.1085` n `774`
- 24h: commodity avg `-0.9993` n `12`; crypto_alt avg `-2.0864` n `230`; crypto_major avg `-1.9845` n `8`; equity avg `-2.4092` n `102`; fx avg `-0.0616` n `6`; index avg `-0.1804` n `25`; metal avg `-0.3045` n `20`; unknown avg `17.8147` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
