# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T21:22:29.099533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.3562` n `236`; crypto_major avg `-0.2205` n `8`; equity avg `-0.2491` n `151`; fx avg `-0.0007` n `6`; index avg `-0.0139` n `26`; metal avg `0.0022` n `20`; unknown avg `-0.0523` n `1193`
- 1h: commodity avg `0.0319` n `13`; crypto_alt avg `-0.1536` n `236`; crypto_major avg `-0.0718` n `8`; equity avg `-0.293` n `151`; fx avg `0.0001` n `6`; index avg `-0.0294` n `26`; metal avg `-0.0024` n `20`; unknown avg `1.5527` n `1185`
- 4h: commodity avg `0.0062` n `13`; crypto_alt avg `0.7287` n `236`; crypto_major avg `0.5251` n `8`; equity avg `-0.1095` n `151`; fx avg `-0.0084` n `6`; index avg `0.0046` n `26`; metal avg `0.0211` n `20`; unknown avg `0.3788` n `1131`
- 24h: commodity avg `-0.0244` n `13`; crypto_alt avg `-1.5284` n `236`; crypto_major avg `-0.5551` n `8`; equity avg `-0.4813` n `151`; fx avg `-0.0342` n `6`; index avg `-0.0539` n `26`; metal avg `-0.0332` n `20`; unknown avg `4.561` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1708`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1419`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1095`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
