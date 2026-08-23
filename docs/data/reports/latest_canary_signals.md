# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T18:07:28.028581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.1291` n `231`; crypto_major avg `-0.1136` n `8`; equity avg `0.0401` n `122`; fx avg `-0.0085` n `6`; index avg `0.0181` n `25`; metal avg `0.0062` n `20`; unknown avg `0.084` n `793`
- 1h: commodity avg `-0.0236` n `12`; crypto_alt avg `-0.1928` n `231`; crypto_major avg `-0.3724` n `8`; equity avg `0.0659` n `122`; fx avg `0.0037` n `6`; index avg `0.0062` n `25`; metal avg `-0.0072` n `20`; unknown avg `0.047` n `793`
- 4h: commodity avg `-0.0443` n `12`; crypto_alt avg `0.3126` n `231`; crypto_major avg `-0.4897` n `8`; equity avg `0.1755` n `122`; fx avg `0.0059` n `6`; index avg `0.0475` n `25`; metal avg `0.025` n `20`; unknown avg `0.5955` n `793`
- 24h: commodity avg `-0.0046` n `12`; crypto_alt avg `1.776` n `231`; crypto_major avg `0.384` n `8`; equity avg `0.6942` n `122`; fx avg `0.035` n `6`; index avg `0.0927` n `25`; metal avg `0.068` n `20`; unknown avg `5.8198` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
