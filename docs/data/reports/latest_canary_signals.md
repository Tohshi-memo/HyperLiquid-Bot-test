# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T09:52:26.501065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `-0.0898` n `230`; crypto_major avg `-0.0883` n `8`; equity avg `-0.078` n `98`; fx avg `-0.0041` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0179` n `20`; unknown avg `-0.0157` n `773`
- 1h: commodity avg `0.0996` n `12`; crypto_alt avg `-0.0085` n `230`; crypto_major avg `0.0429` n `8`; equity avg `0.0323` n `98`; fx avg `-0.0197` n `6`; index avg `0.0238` n `25`; metal avg `0.007` n `20`; unknown avg `-0.0392` n `773`
- 4h: commodity avg `0.2511` n `12`; crypto_alt avg `0.1524` n `230`; crypto_major avg `0.0752` n `8`; equity avg `0.1594` n `98`; fx avg `0.0149` n `6`; index avg `-0.0212` n `25`; metal avg `-0.3877` n `20`; unknown avg `-0.0637` n `741`
- 24h: commodity avg `0.5513` n `12`; crypto_alt avg `-0.0249` n `230`; crypto_major avg `0.0956` n `8`; equity avg `0.7637` n `98`; fx avg `-0.0953` n `6`; index avg `0.1763` n `25`; metal avg `-0.3676` n `20`; unknown avg `11.5205` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0836`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
