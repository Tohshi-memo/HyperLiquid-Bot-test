# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T12:07:24.454178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0916` n `12`; crypto_alt avg `-0.1333` n `232`; crypto_major avg `-0.1312` n `8`; equity avg `-0.1439` n `133`; fx avg `-0.013` n `6`; index avg `-0.0245` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.0053` n `791`
- 1h: commodity avg `-0.0489` n `12`; crypto_alt avg `0.0028` n `232`; crypto_major avg `-0.0281` n `8`; equity avg `-0.0779` n `133`; fx avg `-0.0259` n `6`; index avg `-0.0178` n `26`; metal avg `0.0185` n `20`; unknown avg `-0.2245` n `791`
- 4h: commodity avg `-0.0842` n `12`; crypto_alt avg `0.769` n `232`; crypto_major avg `0.6187` n `8`; equity avg `0.0738` n `133`; fx avg `-0.0565` n `6`; index avg `0.0031` n `26`; metal avg `-0.1136` n `20`; unknown avg `-0.1136` n `785`
- 24h: commodity avg `-0.6499` n `12`; crypto_alt avg `2.5744` n `232`; crypto_major avg `3.9416` n `8`; equity avg `2.2187` n `133`; fx avg `-0.0067` n `6`; index avg `0.4064` n `26`; metal avg `0.4307` n `20`; unknown avg `18.3781` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
