# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T14:37:31.621709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0968` n `12`; crypto_alt avg `-0.2372` n `228`; crypto_major avg `-0.2303` n `8`; equity avg `-0.0071` n `69`; fx avg `0.0008` n `6`; index avg `-0.1627` n `23`; metal avg `-0.2475` n `18`; unknown avg `0.6643` n `418`
- 1h: commodity avg `0.2842` n `12`; crypto_alt avg `-0.3776` n `228`; crypto_major avg `-0.2611` n `8`; equity avg `-0.2743` n `69`; fx avg `-0.0239` n `6`; index avg `-0.2479` n `23`; metal avg `-0.3375` n `18`; unknown avg `-0.0107` n `417`
- 4h: commodity avg `0.4725` n `12`; crypto_alt avg `-1.4621` n `228`; crypto_major avg `-1.1292` n `8`; equity avg `-0.6606` n `69`; fx avg `0.0108` n `6`; index avg `-0.2787` n `23`; metal avg `-0.564` n `18`; unknown avg `1.6488` n `417`
- 24h: commodity avg `0.256` n `12`; crypto_alt avg `0.5242` n `228`; crypto_major avg `1.1709` n `8`; equity avg `1.8869` n `69`; fx avg `0.0925` n `6`; index avg `0.5762` n `23`; metal avg `0.7909` n `18`; unknown avg `1.9687` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
