# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T22:22:27.710104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.1018` n `230`; crypto_major avg `0.0102` n `8`; equity avg `-0.0267` n `114`; fx avg `0.0005` n `6`; index avg `-0.0094` n `25`; metal avg `-0.0078` n `20`; unknown avg `-0.0148` n `792`
- 1h: commodity avg `0.0453` n `12`; crypto_alt avg `-0.1637` n `230`; crypto_major avg `-0.0395` n `8`; equity avg `0.1401` n `114`; fx avg `0.0215` n `6`; index avg `0.0135` n `25`; metal avg `0.0053` n `20`; unknown avg `-0.0209` n `792`
- 4h: commodity avg `0.1121` n `12`; crypto_alt avg `-0.1696` n `230`; crypto_major avg `-0.1193` n `8`; equity avg `-0.0236` n `114`; fx avg `0.0143` n `6`; index avg `-0.023` n `25`; metal avg `-0.026` n `20`; unknown avg `-0.0974` n `792`
- 24h: commodity avg `0.5588` n `12`; crypto_alt avg `0.5149` n `230`; crypto_major avg `1.3275` n `8`; equity avg `1.2105` n `114`; fx avg `0.0363` n `6`; index avg `0.0525` n `25`; metal avg `0.2286` n `20`; unknown avg `0.2936` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
