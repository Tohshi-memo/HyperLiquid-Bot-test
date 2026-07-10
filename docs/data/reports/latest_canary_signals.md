# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T22:13:35.966925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `12`; crypto_alt avg `0.0938` n `229`; crypto_major avg `0.0713` n `8`; equity avg `-0.0017` n `92`; fx avg `-0.0027` n `6`; index avg `0.0001` n `25`; metal avg `-0.0038` n `20`; unknown avg `0.1143` n `765`
- 1h: commodity avg `-0.0414` n `12`; crypto_alt avg `0.3726` n `229`; crypto_major avg `0.1552` n `8`; equity avg `0.0067` n `92`; fx avg `-0.0019` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0294` n `20`; unknown avg `-0.076` n `765`
- 4h: commodity avg `0.1105` n `12`; crypto_alt avg `0.3823` n `229`; crypto_major avg `0.1294` n `8`; equity avg `-0.1894` n `92`; fx avg `-0.0139` n `6`; index avg `-0.0042` n `25`; metal avg `0.1047` n `20`; unknown avg `-0.399` n `765`
- 24h: commodity avg `-0.2521` n `12`; crypto_alt avg `1.1401` n `229`; crypto_major avg `0.9459` n `8`; equity avg `-0.6702` n `92`; fx avg `-0.1737` n `6`; index avg `0.0348` n `25`; metal avg `0.147` n `20`; unknown avg `-0.182` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
