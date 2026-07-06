# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T15:22:35.650420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0313` n `12`; crypto_alt avg `0.0145` n `229`; crypto_major avg `0.0392` n `8`; equity avg `-0.1447` n `88`; fx avg `-0.0083` n `6`; index avg `-0.0283` n `25`; metal avg `-0.0625` n `20`; unknown avg `0.0361` n `765`
- 1h: commodity avg `-0.0134` n `12`; crypto_alt avg `0.5818` n `229`; crypto_major avg `0.7237` n `8`; equity avg `-0.0622` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0273` n `25`; metal avg `0.0085` n `20`; unknown avg `0.3811` n `765`
- 4h: commodity avg `0.1067` n `12`; crypto_alt avg `-0.1399` n `229`; crypto_major avg `-0.7522` n `8`; equity avg `0.4189` n `88`; fx avg `0.0273` n `6`; index avg `0.0719` n `25`; metal avg `-0.2139` n `20`; unknown avg `-0.283` n `765`
- 24h: commodity avg `-0.025` n `12`; crypto_alt avg `-0.1801` n `229`; crypto_major avg `-0.5927` n `8`; equity avg `-0.315` n `88`; fx avg `0.1993` n `6`; index avg `0.0199` n `25`; metal avg `-0.3716` n `20`; unknown avg `0.5716` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
