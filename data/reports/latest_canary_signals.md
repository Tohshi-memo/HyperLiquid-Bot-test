# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T11:07:30.851453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.0082` n `230`; crypto_major avg `-0.0392` n `8`; equity avg `0.018` n `98`; fx avg `-0.0006` n `6`; index avg `-0.0194` n `25`; metal avg `-0.024` n `20`; unknown avg `0.0112` n `773`
- 1h: commodity avg `-0.0791` n `12`; crypto_alt avg `0.2231` n `230`; crypto_major avg `0.2002` n `8`; equity avg `0.1295` n `98`; fx avg `-0.0165` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0268` n `20`; unknown avg `0.0132` n `773`
- 4h: commodity avg `0.0982` n `12`; crypto_alt avg `0.6753` n `230`; crypto_major avg `0.509` n `8`; equity avg `0.2829` n `98`; fx avg `-0.0168` n `6`; index avg `0.0391` n `25`; metal avg `0.0268` n `20`; unknown avg `0.1033` n `772`
- 24h: commodity avg `0.5921` n `12`; crypto_alt avg `-0.3714` n `230`; crypto_major avg `-0.9912` n `8`; equity avg `0.8171` n `98`; fx avg `-0.0133` n `6`; index avg `-0.0009` n `25`; metal avg `0.3615` n `20`; unknown avg `0.1133` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1034`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0801`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0719`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0692`, n `666`, weak_sample_signal
