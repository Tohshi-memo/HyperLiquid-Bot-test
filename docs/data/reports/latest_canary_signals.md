# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T11:22:58.699647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.7312` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9644` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0172` n `12`; crypto_alt avg `0.0086` n `230`; crypto_major avg `0.0952` n `8`; equity avg `-0.154` n `121`; fx avg `0.0065` n `6`; index avg `-0.0306` n `25`; metal avg `-0.0525` n `20`; unknown avg `0.0425` n `792`
- 1h: commodity avg `0.0791` n `12`; crypto_alt avg `0.0712` n `230`; crypto_major avg `-0.1814` n `8`; equity avg `-0.446` n `121`; fx avg `0.013` n `6`; index avg `-0.0711` n `25`; metal avg `0.0024` n `20`; unknown avg `0.0577` n `792`
- 4h: commodity avg `0.2282` n `12`; crypto_alt avg `1.8449` n `230`; crypto_major avg `1.9989` n `8`; equity avg `-0.7323` n `121`; fx avg `0.0663` n `6`; index avg `-0.1195` n `25`; metal avg `0.0345` n `20`; unknown avg `0.1939` n `792`
- 24h: commodity avg `0.2701` n `12`; crypto_alt avg `7.4555` n `230`; crypto_major avg `12.3142` n `8`; equity avg `0.0627` n `120`; fx avg `0.2233` n `6`; index avg `0.0388` n `25`; metal avg `0.8486` n `20`; unknown avg `2.3843` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
