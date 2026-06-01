# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T02:07:24.310398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `12`; crypto_alt avg `-0.0182` n `228`; crypto_major avg `0.0576` n `8`; equity avg `0.0283` n `69`; fx avg `-0.0065` n `6`; index avg `-0.107` n `23`; metal avg `0.1514` n `18`; unknown avg `1.1596` n `421`
- 1h: commodity avg `0.11` n `12`; crypto_alt avg `-0.5747` n `228`; crypto_major avg `-0.637` n `8`; equity avg `-0.4284` n `69`; fx avg `0.0023` n `6`; index avg `-0.0604` n `23`; metal avg `0.3975` n `18`; unknown avg `0.8176` n `421`
- 4h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.3867` n `228`; crypto_major avg `-0.2096` n `8`; equity avg `-0.0176` n `69`; fx avg `0.0742` n `6`; index avg `-0.0326` n `23`; metal avg `0.8387` n `18`; unknown avg `1.3664` n `421`
- 24h: commodity avg `1.0563` n `12`; crypto_alt avg `0.1698` n `228`; crypto_major avg `-0.6369` n `8`; equity avg `0.5176` n `69`; fx avg `0.0385` n `6`; index avg `0.2057` n `23`; metal avg `0.4104` n `18`; unknown avg `1.5665` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2839`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2556`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
