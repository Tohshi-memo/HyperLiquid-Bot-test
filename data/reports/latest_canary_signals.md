# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T11:52:25.314503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.2131` n `228`; crypto_major avg `-0.0633` n `8`; equity avg `-0.0199` n `69`; fx avg `-0.0002` n `6`; index avg `-0.0296` n `23`; metal avg `-0.005` n `18`; unknown avg `-0.0961` n `422`
- 1h: commodity avg `-0.2605` n `12`; crypto_alt avg `-0.2264` n `228`; crypto_major avg `-0.0726` n `8`; equity avg `-0.1741` n `69`; fx avg `-0.0081` n `6`; index avg `-0.0809` n `23`; metal avg `0.027` n `18`; unknown avg `0.092` n `416`
- 4h: commodity avg `-0.5014` n `12`; crypto_alt avg `0.068` n `228`; crypto_major avg `0.5081` n `8`; equity avg `-0.1558` n `69`; fx avg `-0.014` n `6`; index avg `-0.555` n `23`; metal avg `0.4157` n `18`; unknown avg `0.9553` n `416`
- 24h: commodity avg `0.6984` n `12`; crypto_alt avg `-0.5582` n `228`; crypto_major avg `-0.5107` n `8`; equity avg `-0.2714` n `69`; fx avg `0.0023` n `6`; index avg `0.553` n `23`; metal avg `0.3527` n `18`; unknown avg `2.5222` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2883`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
