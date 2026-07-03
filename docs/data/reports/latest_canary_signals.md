# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T04:52:25.697121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `0.0527` n `229`; crypto_major avg `-0.0682` n `8`; equity avg `0.098` n `88`; fx avg `0.02` n `6`; index avg `0.0115` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.0242` n `765`
- 1h: commodity avg `0.0368` n `12`; crypto_alt avg `-0.0515` n `229`; crypto_major avg `-0.0557` n `8`; equity avg `0.5082` n `88`; fx avg `-0.0171` n `6`; index avg `0.1526` n `25`; metal avg `0.0158` n `20`; unknown avg `-0.0141` n `765`
- 4h: commodity avg `0.1912` n `12`; crypto_alt avg `0.5117` n `229`; crypto_major avg `0.3749` n `8`; equity avg `1.6143` n `88`; fx avg `-0.0067` n `6`; index avg `0.4366` n `25`; metal avg `0.4209` n `20`; unknown avg `0.0863` n `761`
- 24h: commodity avg `0.3862` n `12`; crypto_alt avg `1.5421` n `228`; crypto_major avg `2.2322` n `8`; equity avg `-0.3875` n `88`; fx avg `-0.0456` n `6`; index avg `0.0055` n `25`; metal avg `1.2169` n `20`; unknown avg `6.6698` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
