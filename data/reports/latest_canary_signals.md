# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T15:52:34.085360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0558` n `12`; crypto_alt avg `0.9447` n `229`; crypto_major avg `0.8591` n `8`; equity avg `0.1988` n `88`; fx avg `0.018` n `6`; index avg `0.0037` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.9576` n `765`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `1.3532` n `229`; crypto_major avg `1.3548` n `8`; equity avg `0.1116` n `88`; fx avg `0.018` n `6`; index avg `0.0197` n `25`; metal avg `0.118` n `20`; unknown avg `1.496` n `765`
- 4h: commodity avg `0.1033` n `12`; crypto_alt avg `0.9244` n `229`; crypto_major avg `0.0488` n `8`; equity avg `0.6067` n `88`; fx avg `0.0379` n `6`; index avg `0.1114` n `25`; metal avg `-0.1312` n `20`; unknown avg `0.0232` n `765`
- 24h: commodity avg `0.0084` n `12`; crypto_alt avg `0.7761` n `229`; crypto_major avg `0.1558` n `8`; equity avg `-0.0586` n `88`; fx avg `0.1964` n `6`; index avg `0.0845` n `25`; metal avg `-0.3241` n `20`; unknown avg `0.5615` n `679`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
