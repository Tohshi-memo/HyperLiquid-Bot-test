# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T13:37:26.784467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0327` n `12`; crypto_alt avg `-0.0565` n `230`; crypto_major avg `-0.0116` n `8`; equity avg `0.1039` n `114`; fx avg `0.0176` n `6`; index avg `0.0114` n `25`; metal avg `0.0714` n `20`; unknown avg `-0.0069` n `795`
- 1h: commodity avg `0.0936` n `12`; crypto_alt avg `-0.0939` n `230`; crypto_major avg `-0.1275` n `8`; equity avg `-0.0192` n `114`; fx avg `0.0218` n `6`; index avg `0.0065` n `25`; metal avg `-0.0266` n `20`; unknown avg `-0.0531` n `795`
- 4h: commodity avg `0.1822` n `12`; crypto_alt avg `0.0653` n `230`; crypto_major avg `-0.0109` n `8`; equity avg `-0.0314` n `114`; fx avg `0.0032` n `6`; index avg `0.0213` n `25`; metal avg `0.0201` n `20`; unknown avg `0.0227` n `795`
- 24h: commodity avg `0.638` n `12`; crypto_alt avg `-0.8476` n `230`; crypto_major avg `-0.1644` n `8`; equity avg `-2.4523` n `114`; fx avg `-0.051` n `6`; index avg `-0.4999` n `25`; metal avg `-0.1427` n `20`; unknown avg `-0.1126` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
