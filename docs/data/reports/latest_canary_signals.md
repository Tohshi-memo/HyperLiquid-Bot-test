# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T02:52:30.814755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `0.0393` n `230`; crypto_major avg `0.0651` n `8`; equity avg `0.0147` n `114`; fx avg `-0.0208` n `6`; index avg `0.0078` n `25`; metal avg `0.0082` n `20`; unknown avg `0.1435` n `791`
- 1h: commodity avg `0.0147` n `12`; crypto_alt avg `0.1824` n `230`; crypto_major avg `0.1943` n `8`; equity avg `0.0133` n `114`; fx avg `0.0935` n `6`; index avg `0.0042` n `25`; metal avg `0.0063` n `20`; unknown avg `0.0182` n `791`
- 4h: commodity avg `0.0023` n `12`; crypto_alt avg `0.312` n `230`; crypto_major avg `0.5074` n `8`; equity avg `0.0164` n `114`; fx avg `0.0731` n `6`; index avg `0.0002` n `25`; metal avg `0.0485` n `20`; unknown avg `0.3175` n `791`
- 24h: commodity avg `0.1757` n `12`; crypto_alt avg `0.1366` n `230`; crypto_major avg `-0.4967` n `8`; equity avg `-0.1727` n `114`; fx avg `0.2102` n `6`; index avg `-0.0363` n `25`; metal avg `0.4328` n `20`; unknown avg `-0.1629` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
