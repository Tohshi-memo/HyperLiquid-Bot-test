# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T13:22:18.578988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1617` n `12`; crypto_alt avg `0.1313` n `228`; crypto_major avg `0.0311` n `8`; equity avg `-0.0344` n `66`; fx avg `-0.0098` n `6`; index avg `0.0173` n `23`; metal avg `-0.1196` n `18`; unknown avg `-0.0457` n `383`
- 1h: commodity avg `0.0388` n `12`; crypto_alt avg `0.2031` n `228`; crypto_major avg `0.0362` n `8`; equity avg `-0.1449` n `66`; fx avg `-0.0029` n `6`; index avg `-0.0198` n `23`; metal avg `-0.7342` n `18`; unknown avg `0.005` n `383`
- 4h: commodity avg `0.1627` n `12`; crypto_alt avg `-0.2286` n `228`; crypto_major avg `-0.3117` n `8`; equity avg `-0.6109` n `66`; fx avg `-0.0102` n `6`; index avg `-0.2468` n `23`; metal avg `-0.8188` n `18`; unknown avg `-0.5424` n `383`
- 24h: commodity avg `1.8181` n `12`; crypto_alt avg `0.2241` n `228`; crypto_major avg `-0.4181` n `8`; equity avg `-2.796` n `66`; fx avg `0.2327` n `6`; index avg `-1.4164` n `23`; metal avg `-1.7614` n `18`; unknown avg `0.068` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
