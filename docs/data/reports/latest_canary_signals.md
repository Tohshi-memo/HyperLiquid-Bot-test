# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T11:07:32.422369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0406` n `12`; crypto_alt avg `0.1977` n `232`; crypto_major avg `0.1494` n `8`; equity avg `-0.0618` n `133`; fx avg `0.0048` n `6`; index avg `-0.0149` n `26`; metal avg `-0.0186` n `20`; unknown avg `2.7793` n `791`
- 1h: commodity avg `-0.0808` n `12`; crypto_alt avg `0.1209` n `232`; crypto_major avg `0.1987` n `8`; equity avg `-0.018` n `133`; fx avg `-0.0036` n `6`; index avg `0.0132` n `26`; metal avg `0.0278` n `20`; unknown avg `2.6746` n `791`
- 4h: commodity avg `-0.1683` n `12`; crypto_alt avg `0.8351` n `232`; crypto_major avg `0.3316` n `8`; equity avg `0.4636` n `133`; fx avg `-0.0198` n `6`; index avg `0.0638` n `26`; metal avg `0.0039` n `20`; unknown avg `1.8246` n `785`
- 24h: commodity avg `-0.532` n `12`; crypto_alt avg `2.863` n `232`; crypto_major avg `4.3719` n `8`; equity avg `2.2125` n `133`; fx avg `-0.0068` n `6`; index avg `0.4178` n `26`; metal avg `0.5192` n `20`; unknown avg `4.0698` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
