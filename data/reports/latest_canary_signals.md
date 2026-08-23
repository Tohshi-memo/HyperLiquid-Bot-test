# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T16:37:25.993730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.1837` n `231`; crypto_major avg `0.287` n `8`; equity avg `0.0327` n `122`; fx avg `0.008` n `6`; index avg `-0.0004` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.0594` n `793`
- 1h: commodity avg `-0.0291` n `12`; crypto_alt avg `-0.0948` n `231`; crypto_major avg `0.0814` n `8`; equity avg `0.0144` n `122`; fx avg `-0.0002` n `6`; index avg `-0.0016` n `25`; metal avg `0.0305` n `20`; unknown avg `0.0928` n `793`
- 4h: commodity avg `-0.0258` n `12`; crypto_alt avg `1.7752` n `231`; crypto_major avg `0.5173` n `8`; equity avg `0.1509` n `122`; fx avg `-0.0009` n `6`; index avg `0.0168` n `25`; metal avg `0.0362` n `20`; unknown avg `1.1519` n `793`
- 24h: commodity avg `0.0144` n `12`; crypto_alt avg `1.9855` n `231`; crypto_major avg `1.2114` n `8`; equity avg `0.6397` n `122`; fx avg `0.0291` n `6`; index avg `0.0631` n `25`; metal avg `0.0919` n `20`; unknown avg `8.0007` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
