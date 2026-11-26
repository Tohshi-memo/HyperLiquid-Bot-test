# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T20:07:27.825168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `13`; crypto_alt avg `0.0577` n `239`; crypto_major avg `0.1068` n `8`; equity avg `0.0276` n `168`; fx avg `-0.0008` n `6`; index avg `0.0039` n `27`; metal avg `0.0024` n `20`; unknown avg `0.2119` n `1241`
- 1h: commodity avg `-0.0156` n `13`; crypto_alt avg `0.1291` n `239`; crypto_major avg `0.309` n `8`; equity avg `0.1215` n `168`; fx avg `-0.0017` n `6`; index avg `0.01` n `27`; metal avg `0.0149` n `20`; unknown avg `-0.7726` n `1249`
- 4h: commodity avg `-0.0367` n `13`; crypto_alt avg `0.7599` n `239`; crypto_major avg `0.7799` n `8`; equity avg `0.1112` n `168`; fx avg `-0.022` n `6`; index avg `0.0027` n `27`; metal avg `-0.0782` n `20`; unknown avg `166.4364` n `1195`
- 24h: commodity avg `0.1775` n `13`; crypto_alt avg `2.026` n `239`; crypto_major avg `1.2923` n `8`; equity avg `1.4019` n `168`; fx avg `-0.0358` n `6`; index avg `0.0969` n `27`; metal avg `0.1824` n `20`; unknown avg `2.4789` n `1023`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
