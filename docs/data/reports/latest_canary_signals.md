# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T18:07:29.722241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `13`; crypto_alt avg `0.2102` n `239`; crypto_major avg `0.0624` n `8`; equity avg `0.0036` n `168`; fx avg `0.0002` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0075` n `20`; unknown avg `3.6472` n `1257`
- 1h: commodity avg `0.0912` n `13`; crypto_alt avg `0.1632` n `239`; crypto_major avg `0.0497` n `8`; equity avg `-0.0973` n `168`; fx avg `-0.002` n `6`; index avg `-0.002` n `27`; metal avg `-0.0492` n `20`; unknown avg `3.5762` n `1263`
- 4h: commodity avg `0.0258` n `13`; crypto_alt avg `-0.0743` n `239`; crypto_major avg `-0.3282` n `8`; equity avg `-0.2487` n `168`; fx avg `-0.0356` n `6`; index avg `-0.0217` n `27`; metal avg `-0.0316` n `20`; unknown avg `1.0166` n `1239`
- 24h: commodity avg `0.0173` n `13`; crypto_alt avg `2.431` n `239`; crypto_major avg `1.4372` n `8`; equity avg `2.8672` n `168`; fx avg `-0.0136` n `6`; index avg `0.2248` n `27`; metal avg `0.5358` n `20`; unknown avg `11.8555` n `1053`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
