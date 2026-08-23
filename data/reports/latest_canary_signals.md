# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T23:37:27.197808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `12`; crypto_alt avg `0.1051` n `231`; crypto_major avg `0.0674` n `8`; equity avg `0.007` n `122`; fx avg `-0.0036` n `6`; index avg `0.0209` n `25`; metal avg `0.0356` n `20`; unknown avg `-0.1049` n `793`
- 1h: commodity avg `-0.0382` n `12`; crypto_alt avg `-0.179` n `231`; crypto_major avg `0.051` n `8`; equity avg `0.1909` n `122`; fx avg `-0.0095` n `6`; index avg `0.065` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0087` n `793`
- 4h: commodity avg `-0.1173` n `12`; crypto_alt avg `0.0751` n `231`; crypto_major avg `0.7348` n `8`; equity avg `0.1028` n `122`; fx avg `-0.0747` n `6`; index avg `0.0173` n `25`; metal avg `0.0204` n `20`; unknown avg `1.7569` n `793`
- 24h: commodity avg `-0.2414` n `12`; crypto_alt avg `3.786` n `231`; crypto_major avg `2.1618` n `8`; equity avg `0.8427` n `122`; fx avg `-0.1193` n `6`; index avg `0.1344` n `25`; metal avg `0.1024` n `20`; unknown avg `5.9066` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
