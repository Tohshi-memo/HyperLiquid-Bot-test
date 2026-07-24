# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T08:22:25.031592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.0736` n `230`; crypto_major avg `-0.0737` n `8`; equity avg `0.0366` n `100`; fx avg `-0.0171` n `6`; index avg `0.0054` n `25`; metal avg `0.0121` n `20`; unknown avg `0.0162` n `772`
- 1h: commodity avg `-0.0245` n `12`; crypto_alt avg `-0.3276` n `230`; crypto_major avg `-0.3898` n `8`; equity avg `-0.1245` n `100`; fx avg `-0.0316` n `6`; index avg `-0.0338` n `25`; metal avg `-0.0304` n `20`; unknown avg `0.0538` n `772`
- 4h: commodity avg `-0.3052` n `12`; crypto_alt avg `0.248` n `230`; crypto_major avg `0.4067` n `8`; equity avg `0.5296` n `100`; fx avg `0.0053` n `6`; index avg `0.0898` n `25`; metal avg `0.1778` n `20`; unknown avg `0.0711` n `756`
- 24h: commodity avg `0.0351` n `12`; crypto_alt avg `-0.8556` n `230`; crypto_major avg `-1.1461` n `8`; equity avg `-1.7548` n `99`; fx avg `-0.1312` n `6`; index avg `-0.4731` n `25`; metal avg `-0.4898` n `20`; unknown avg `0.1131` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0979`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0831`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0824`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0812`, n `666`, weak_sample_signal
