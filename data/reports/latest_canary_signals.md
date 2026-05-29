# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T13:52:22.228833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `0.1031` n `228`; crypto_major avg `0.0684` n `8`; equity avg `0.2235` n `69`; fx avg `-0.0049` n `6`; index avg `0.0589` n `23`; metal avg `0.1255` n `18`; unknown avg `0.0467` n `417`
- 1h: commodity avg `-0.0446` n `12`; crypto_alt avg `-0.0788` n `228`; crypto_major avg `-0.0918` n `8`; equity avg `0.039` n `69`; fx avg `0.0235` n `6`; index avg `-0.081` n `23`; metal avg `0.129` n `18`; unknown avg `0.9809` n `417`
- 4h: commodity avg `0.1639` n `12`; crypto_alt avg `-1.3109` n `228`; crypto_major avg `-0.8646` n `8`; equity avg `-0.2053` n `69`; fx avg `0.0352` n `6`; index avg `0.0372` n `23`; metal avg `0.0019` n `18`; unknown avg `1.08` n `417`
- 24h: commodity avg `-0.1026` n `12`; crypto_alt avg `0.78` n `228`; crypto_major avg `1.5373` n `8`; equity avg `3.1635` n `69`; fx avg `0.1044` n `6`; index avg `1.2841` n `23`; metal avg `1.9219` n `18`; unknown avg `2.0453` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
