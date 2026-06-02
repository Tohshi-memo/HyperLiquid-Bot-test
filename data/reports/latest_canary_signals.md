# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T10:52:20.283162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.77` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0272` n `12`; crypto_alt avg `0.322` n `228`; crypto_major avg `0.2889` n `8`; equity avg `0.0947` n `69`; fx avg `0.0038` n `6`; index avg `-0.0821` n `23`; metal avg `0.0321` n `18`; unknown avg `0.2366` n `422`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `0.7012` n `228`; crypto_major avg `0.5493` n `8`; equity avg `-0.1128` n `69`; fx avg `0.0006` n `6`; index avg `-0.0533` n `23`; metal avg `-0.0848` n `18`; unknown avg `0.1007` n `422`
- 4h: commodity avg `-0.173` n `12`; crypto_alt avg `0.2617` n `228`; crypto_major avg `-0.1754` n `8`; equity avg `0.0944` n `69`; fx avg `-0.0348` n `6`; index avg `0.2051` n `23`; metal avg `-0.2344` n `18`; unknown avg `-0.7194` n `422`
- 24h: commodity avg `-1.0031` n `12`; crypto_alt avg `-0.0795` n `228`; crypto_major avg `-1.9488` n `8`; equity avg `0.4435` n `69`; fx avg `0.1224` n `6`; index avg `-0.0655` n `23`; metal avg `0.6628` n `18`; unknown avg `0.0343` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
