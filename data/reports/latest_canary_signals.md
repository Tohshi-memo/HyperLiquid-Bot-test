# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T04:52:24.687614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `13`; crypto_alt avg `-0.005` n `239`; crypto_major avg `-0.0898` n `8`; equity avg `-0.0692` n `168`; fx avg `-0.0047` n `6`; index avg `-0.0136` n `27`; metal avg `0.0107` n `20`; unknown avg `-0.2707` n `1263`
- 1h: commodity avg `0.0526` n `13`; crypto_alt avg `0.0687` n `239`; crypto_major avg `0.0815` n `8`; equity avg `0.1992` n `168`; fx avg `-0.0276` n `6`; index avg `0.021` n `27`; metal avg `0.0178` n `20`; unknown avg `3.9338` n `1251`
- 4h: commodity avg `0.162` n `13`; crypto_alt avg `1.2924` n `239`; crypto_major avg `1.9333` n `8`; equity avg `2.9297` n `168`; fx avg `-0.0146` n `6`; index avg `0.3025` n `27`; metal avg `0.9943` n `20`; unknown avg `2.7397` n `1251`
- 24h: commodity avg `0.2059` n `13`; crypto_alt avg `1.7598` n `239`; crypto_major avg `1.7662` n `8`; equity avg `2.2914` n `168`; fx avg `0.0086` n `6`; index avg `0.2234` n `27`; metal avg `0.6625` n `20`; unknown avg `204.8445` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
