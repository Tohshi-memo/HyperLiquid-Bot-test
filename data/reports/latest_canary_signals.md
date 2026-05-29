# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T21:07:21.395493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2222` n `12`; crypto_alt avg `0.09` n `228`; crypto_major avg `0.0535` n `8`; equity avg `0.0105` n `69`; fx avg `-0.0021` n `6`; index avg `-0.0247` n `23`; metal avg `-0.0549` n `18`; unknown avg `-0.0021` n `419`
- 1h: commodity avg `0.1919` n `12`; crypto_alt avg `0.1301` n `228`; crypto_major avg `-0.0109` n `8`; equity avg `-0.0429` n `69`; fx avg `-0.0397` n `6`; index avg `-0.0585` n `23`; metal avg `-0.1714` n `18`; unknown avg `-0.1442` n `419`
- 4h: commodity avg `0.3545` n `12`; crypto_alt avg `-0.4383` n `228`; crypto_major avg `-0.556` n `8`; equity avg `0.025` n `69`; fx avg `-0.0167` n `6`; index avg `-0.0903` n `23`; metal avg `-0.3726` n `18`; unknown avg `-0.3057` n `419`
- 24h: commodity avg `-0.5849` n `12`; crypto_alt avg `0.635` n `228`; crypto_major avg `1.0965` n `8`; equity avg `1.3133` n `69`; fx avg `0.182` n `6`; index avg `0.1139` n `23`; metal avg `-0.0081` n `18`; unknown avg `0.5813` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
