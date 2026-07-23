# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T10:07:15.720778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0442` n `12`; crypto_alt avg `-0.0321` n `230`; crypto_major avg `0.0215` n `8`; equity avg `-0.0489` n `98`; fx avg `-0.01` n `6`; index avg `-0.002` n `25`; metal avg `-0.0174` n `20`; unknown avg `-0.0012` n `773`
- 1h: commodity avg `0.0264` n `12`; crypto_alt avg `-0.1026` n `230`; crypto_major avg `-0.0874` n `8`; equity avg `-0.236` n `98`; fx avg `-0.0156` n `6`; index avg `-0.0411` n `25`; metal avg `-0.1082` n `20`; unknown avg `-0.0303` n `773`
- 4h: commodity avg `0.2006` n `12`; crypto_alt avg `0.1341` n `230`; crypto_major avg `0.0837` n `8`; equity avg `0.1932` n `98`; fx avg `-0.0149` n `6`; index avg `-0.0024` n `25`; metal avg `-0.3479` n `20`; unknown avg `0.1007` n `773`
- 24h: commodity avg `0.5781` n `12`; crypto_alt avg `-0.1457` n `230`; crypto_major avg `-0.0574` n `8`; equity avg `0.6133` n `98`; fx avg `-0.0967` n `6`; index avg `0.1364` n `25`; metal avg `-0.3936` n `20`; unknown avg `11.5078` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0831`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
