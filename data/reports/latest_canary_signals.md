# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T07:22:27.080803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0824` n `13`; crypto_alt avg `0.0384` n `239`; crypto_major avg `0.0368` n `8`; equity avg `-0.1699` n `168`; fx avg `0.0068` n `6`; index avg `-0.0244` n `27`; metal avg `-0.041` n `20`; unknown avg `0.0617` n `1261`
- 1h: commodity avg `-0.0942` n `13`; crypto_alt avg `0.0302` n `239`; crypto_major avg `0.177` n `8`; equity avg `-0.3876` n `168`; fx avg `-0.0431` n `6`; index avg `-0.0444` n `27`; metal avg `0.0718` n `20`; unknown avg `0.185` n `1255`
- 4h: commodity avg `0.0225` n `13`; crypto_alt avg `0.2685` n `239`; crypto_major avg `0.4742` n `8`; equity avg `0.9075` n `168`; fx avg `-0.0561` n `6`; index avg `0.0266` n `27`; metal avg `0.3433` n `20`; unknown avg `57.8652` n `1233`
- 24h: commodity avg `0.5504` n `13`; crypto_alt avg `2.3187` n `239`; crypto_major avg `2.9161` n `8`; equity avg `3.6306` n `168`; fx avg `-0.0284` n `6`; index avg `0.282` n `27`; metal avg `1.2033` n `20`; unknown avg `219.8173` n `991`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
