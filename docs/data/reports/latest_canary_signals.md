# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T19:37:44.869673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `12`; crypto_alt avg `-0.0001` n `231`; crypto_major avg `0.0226` n `8`; equity avg `0.0171` n `122`; fx avg `-0.0082` n `6`; index avg `0.0021` n `25`; metal avg `0.0003` n `20`; unknown avg `0.2027` n `793`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.0593` n `231`; crypto_major avg `-0.1828` n `8`; equity avg `0.1209` n `122`; fx avg `-0.0119` n `6`; index avg `0.0152` n `25`; metal avg `-0.0117` n `20`; unknown avg `0.4004` n `793`
- 4h: commodity avg `-0.061` n `12`; crypto_alt avg `0.3052` n `231`; crypto_major avg `0.1086` n `8`; equity avg `0.2852` n `122`; fx avg `-0.016` n `6`; index avg `0.0582` n `25`; metal avg `0.0296` n `20`; unknown avg `0.7558` n `793`
- 24h: commodity avg `-0.0407` n `12`; crypto_alt avg `2.2529` n `231`; crypto_major avg `0.4061` n `8`; equity avg `0.846` n `122`; fx avg `0.0012` n `6`; index avg `0.131` n `25`; metal avg `0.0825` n `20`; unknown avg `5.5547` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
