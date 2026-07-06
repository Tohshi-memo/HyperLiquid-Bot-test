# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T07:07:25.621555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0525` n `12`; crypto_alt avg `-0.0176` n `229`; crypto_major avg `-0.0281` n `8`; equity avg `-0.0149` n `88`; fx avg `-0.0043` n `6`; index avg `-0.0022` n `25`; metal avg `0.0348` n `20`; unknown avg `0.9038` n `765`
- 1h: commodity avg `-0.0943` n `12`; crypto_alt avg `-0.0193` n `229`; crypto_major avg `-0.0074` n `8`; equity avg `0.052` n `88`; fx avg `0.0281` n `6`; index avg `0.0358` n `25`; metal avg `0.0141` n `20`; unknown avg `0.0313` n `763`
- 4h: commodity avg `0.1567` n `12`; crypto_alt avg `-1.0279` n `229`; crypto_major avg `-0.855` n `8`; equity avg `0.4416` n `88`; fx avg `0.0132` n `6`; index avg `0.117` n `25`; metal avg `-0.095` n `20`; unknown avg `-0.1528` n `731`
- 24h: commodity avg `-0.0869` n `12`; crypto_alt avg `-0.1667` n `229`; crypto_major avg `0.8652` n `8`; equity avg `-0.5976` n `88`; fx avg `0.0838` n `6`; index avg `-0.0243` n `25`; metal avg `-0.2796` n `20`; unknown avg `1.0522` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
