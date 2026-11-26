# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T17:07:29.656031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0577` n `13`; crypto_alt avg `0.1812` n `239`; crypto_major avg `0.2018` n `8`; equity avg `0.0458` n `168`; fx avg `0.002` n `6`; index avg `0.0023` n `27`; metal avg `0.0045` n `20`; unknown avg `0.9289` n `1257`
- 1h: commodity avg `-0.16` n `13`; crypto_alt avg `0.1704` n `239`; crypto_major avg `0.0304` n `8`; equity avg `-0.144` n `168`; fx avg `-0.0178` n `6`; index avg `-0.0244` n `27`; metal avg `-0.0441` n `20`; unknown avg `0.346` n `1251`
- 4h: commodity avg `-0.0762` n `13`; crypto_alt avg `-0.1672` n `239`; crypto_major avg `-0.2795` n `8`; equity avg `-0.2191` n `168`; fx avg `-0.0154` n `6`; index avg `-0.0275` n `27`; metal avg `0.0305` n `20`; unknown avg `0.0788` n `1239`
- 24h: commodity avg `0.0279` n `13`; crypto_alt avg `3.6116` n `239`; crypto_major avg `2.7097` n `8`; equity avg `4.7582` n `168`; fx avg `-0.0007` n `6`; index avg `0.4198` n `27`; metal avg `0.9778` n `20`; unknown avg `15.3196` n `1052`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
