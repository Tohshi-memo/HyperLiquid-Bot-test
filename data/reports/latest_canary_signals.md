# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T06:52:27.227072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0765` n `12`; crypto_alt avg `0.1237` n `230`; crypto_major avg `0.1124` n `8`; equity avg `0.1775` n `102`; fx avg `-0.0342` n `6`; index avg `0.0129` n `25`; metal avg `0.0356` n `20`; unknown avg `-0.007` n `774`
- 1h: commodity avg `-0.2573` n `12`; crypto_alt avg `0.1264` n `230`; crypto_major avg `0.0848` n `8`; equity avg `0.0463` n `102`; fx avg `-0.0341` n `6`; index avg `0.0052` n `25`; metal avg `0.0831` n `20`; unknown avg `-0.0189` n `758`
- 4h: commodity avg `-0.036` n `12`; crypto_alt avg `0.3107` n `230`; crypto_major avg `0.2686` n `8`; equity avg `-0.1271` n `102`; fx avg `-0.044` n `6`; index avg `-0.0362` n `25`; metal avg `0.0419` n `20`; unknown avg `-0.0273` n `758`
- 24h: commodity avg `-0.6272` n `12`; crypto_alt avg `-3.6164` n `230`; crypto_major avg `-3.6129` n `8`; equity avg `-4.0234` n `102`; fx avg `-0.2321` n `6`; index avg `-0.8603` n `25`; metal avg `-0.367` n `20`; unknown avg `1161.4957` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
