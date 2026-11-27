# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T13:52:26.196309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0752` n `13`; crypto_alt avg `0.1002` n `239`; crypto_major avg `0.1719` n `8`; equity avg `0.0568` n `168`; fx avg `0.0121` n `6`; index avg `-0.008` n `27`; metal avg `0.0281` n `20`; unknown avg `1.0244` n `1264`
- 1h: commodity avg `-0.2015` n `13`; crypto_alt avg `0.2086` n `239`; crypto_major avg `0.3746` n `8`; equity avg `0.0323` n `168`; fx avg `-0.0215` n `6`; index avg `-0.0111` n `27`; metal avg `-0.1519` n `20`; unknown avg `3.9332` n `1255`
- 4h: commodity avg `-0.4762` n `13`; crypto_alt avg `0.0838` n `239`; crypto_major avg `-0.0742` n `8`; equity avg `-0.39` n `168`; fx avg `-0.0076` n `6`; index avg `-0.0009` n `27`; metal avg `-0.4226` n `20`; unknown avg `186.6103` n `1249`
- 24h: commodity avg `-0.3044` n `13`; crypto_alt avg `1.9158` n `239`; crypto_major avg `2.6418` n `8`; equity avg `3.2808` n `168`; fx avg `-0.1013` n `6`; index avg `0.2591` n `27`; metal avg `0.8527` n `20`; unknown avg `75.9746` n `1027`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
