# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T03:22:29.399466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.054` n `12`; crypto_alt avg `-0.1408` n `230`; crypto_major avg `-0.0186` n `8`; equity avg `-0.0029` n `98`; fx avg `0.0038` n `6`; index avg `-0.0119` n `25`; metal avg `0.0559` n `20`; unknown avg `0.1024` n `773`
- 1h: commodity avg `0.0993` n `12`; crypto_alt avg `-0.215` n `230`; crypto_major avg `0.0041` n `8`; equity avg `-0.0347` n `98`; fx avg `0.0177` n `6`; index avg `-0.0267` n `25`; metal avg `0.1298` n `20`; unknown avg `0.0262` n `773`
- 4h: commodity avg `0.1985` n `12`; crypto_alt avg `-0.2659` n `230`; crypto_major avg `-0.1871` n `8`; equity avg `-0.0032` n `98`; fx avg `-0.0595` n `6`; index avg `0.0379` n `25`; metal avg `0.2283` n `20`; unknown avg `-0.0831` n `773`
- 24h: commodity avg `0.7979` n `12`; crypto_alt avg `-0.8942` n `230`; crypto_major avg `-0.7781` n `8`; equity avg `-0.7717` n `98`; fx avg `-0.1362` n `6`; index avg `-0.1333` n `25`; metal avg `-0.1356` n `20`; unknown avg `1.7986` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0962`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0809`, n `666`, weak_sample_signal
