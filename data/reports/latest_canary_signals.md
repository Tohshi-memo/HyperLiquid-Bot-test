# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T12:52:38.342223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0547` n `12`; crypto_alt avg `0.0525` n `230`; crypto_major avg `0.1714` n `8`; equity avg `0.556` n `112`; fx avg `0.029` n `6`; index avg `0.0681` n `25`; metal avg `0.0766` n `20`; unknown avg `0.0108` n `782`
- 1h: commodity avg `0.0417` n `12`; crypto_alt avg `0.0349` n `230`; crypto_major avg `0.3953` n `8`; equity avg `1.1858` n `112`; fx avg `-0.0697` n `6`; index avg `0.1841` n `25`; metal avg `0.2258` n `20`; unknown avg `0.0106` n `782`
- 4h: commodity avg `-0.2981` n `12`; crypto_alt avg `0.0596` n `230`; crypto_major avg `0.8073` n `8`; equity avg `1.2517` n `112`; fx avg `-0.082` n `6`; index avg `0.22` n `25`; metal avg `0.0877` n `20`; unknown avg `0.1028` n `782`
- 24h: commodity avg `0.0494` n `12`; crypto_alt avg `0.5234` n `230`; crypto_major avg `0.8871` n `8`; equity avg `3.5548` n `109`; fx avg `-0.151` n `6`; index avg `0.3121` n `25`; metal avg `0.6093` n `20`; unknown avg `0.3726` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
