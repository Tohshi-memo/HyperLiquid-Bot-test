# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T19:37:26.836807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `13`; crypto_alt avg `0.0324` n `238`; crypto_major avg `-0.0426` n `8`; equity avg `-0.0039` n `156`; fx avg `0.0007` n `6`; index avg `-0.0059` n `27`; metal avg `-0.0001` n `20`; unknown avg `-0.4306` n `1255`
- 1h: commodity avg `0.0545` n `13`; crypto_alt avg `-0.5839` n `238`; crypto_major avg `-0.4337` n `8`; equity avg `-0.1063` n `156`; fx avg `-0.0025` n `6`; index avg `-0.0281` n `27`; metal avg `-0.0328` n `20`; unknown avg `13.5846` n `1241`
- 4h: commodity avg `-0.0277` n `13`; crypto_alt avg `-1.1706` n `238`; crypto_major avg `-0.653` n `8`; equity avg `-0.2` n `156`; fx avg `0.0192` n `6`; index avg `-0.0374` n `27`; metal avg `-0.0166` n `20`; unknown avg `-0.0765` n `1219`
- 24h: commodity avg `0.0465` n `13`; crypto_alt avg `-1.0659` n `238`; crypto_major avg `-0.5063` n `8`; equity avg `0.1923` n `156`; fx avg `0.0264` n `6`; index avg `0.0359` n `27`; metal avg `0.0357` n `20`; unknown avg `3.9797` n `988`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
