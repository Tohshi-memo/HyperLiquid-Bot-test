# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T08:22:37.399064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1193` n `12`; crypto_alt avg `0.0756` n `230`; crypto_major avg `0.1335` n `8`; equity avg `0.2898` n `102`; fx avg `0.0015` n `6`; index avg `0.0745` n `25`; metal avg `0.0571` n `20`; unknown avg `-0.0445` n `779`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.1871` n `230`; crypto_major avg `-0.0617` n `8`; equity avg `0.2544` n `102`; fx avg `0.0302` n `6`; index avg `0.0606` n `25`; metal avg `0.1211` n `20`; unknown avg `-0.1067` n `779`
- 4h: commodity avg `0.2625` n `12`; crypto_alt avg `0.0661` n `230`; crypto_major avg `0.1604` n `8`; equity avg `0.1685` n `102`; fx avg `-0.0188` n `6`; index avg `-0.0362` n `25`; metal avg `0.1124` n `20`; unknown avg `0.7274` n `747`
- 24h: commodity avg `0.8798` n `12`; crypto_alt avg `-0.3888` n `230`; crypto_major avg `-0.5132` n `8`; equity avg `-2.7587` n `102`; fx avg `-0.0043` n `6`; index avg `-0.4149` n `25`; metal avg `0.1035` n `20`; unknown avg `-0.6053` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
