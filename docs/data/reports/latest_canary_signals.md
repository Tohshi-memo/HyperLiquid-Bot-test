# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T18:56:54.525703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `0.1027` n `228`; crypto_major avg `0.1153` n `8`; equity avg `-0.0114` n `88`; fx avg `0.0062` n `6`; index avg `-0.0141` n `23`; metal avg `0.0013` n `20`; unknown avg `0.0024` n `764`
- 1h: commodity avg `0.0057` n `12`; crypto_alt avg `-0.1356` n `228`; crypto_major avg `-0.1214` n `8`; equity avg `-0.0095` n `88`; fx avg `-0.0051` n `6`; index avg `-0.0089` n `23`; metal avg `0.0238` n `20`; unknown avg `0.6352` n `764`
- 4h: commodity avg `-0.0692` n `12`; crypto_alt avg `-0.9349` n `228`; crypto_major avg `-0.6431` n `8`; equity avg `-0.1149` n `88`; fx avg `-0.033` n `6`; index avg `-0.0387` n `23`; metal avg `0.0121` n `20`; unknown avg `-0.4829` n `764`
- 24h: commodity avg `0.3066` n `12`; crypto_alt avg `-0.8349` n `228`; crypto_major avg `-1.3455` n `8`; equity avg `0.059` n `88`; fx avg `-0.03` n `6`; index avg `-0.0437` n `23`; metal avg `-0.0177` n `20`; unknown avg `15.004` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
