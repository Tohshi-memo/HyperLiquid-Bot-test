# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T17:07:25.326640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `-0.1108` n `228`; crypto_major avg `-0.1333` n `8`; equity avg `-0.0442` n `78`; fx avg `-0.0029` n `6`; index avg `-0.006` n `23`; metal avg `-0.0183` n `18`; unknown avg `-0.1109` n `701`
- 1h: commodity avg `0.0634` n `12`; crypto_alt avg `-0.0767` n `228`; crypto_major avg `-0.3526` n `8`; equity avg `-0.0655` n `78`; fx avg `0.0033` n `6`; index avg `-0.001` n `23`; metal avg `-0.054` n `18`; unknown avg `-0.026` n `701`
- 4h: commodity avg `0.1654` n `12`; crypto_alt avg `0.4177` n `228`; crypto_major avg `-0.1706` n `8`; equity avg `-0.1115` n `78`; fx avg `0.0368` n `6`; index avg `-0.0255` n `23`; metal avg `-0.0545` n `18`; unknown avg `0.2088` n `701`
- 24h: commodity avg `0.3771` n `12`; crypto_alt avg `0.8732` n `228`; crypto_major avg `1.3844` n `8`; equity avg `0.4103` n `78`; fx avg `0.0665` n `6`; index avg `0.0508` n `23`; metal avg `0.1394` n `18`; unknown avg `-0.1256` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
