# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T21:03:12.568577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `0.0915` n `230`; crypto_major avg `0.0442` n `8`; equity avg `-0.0189` n `92`; fx avg `-0.0194` n `6`; index avg `0.0016` n `25`; metal avg `-0.0` n `20`; unknown avg `-0.0113` n `765`
- 1h: commodity avg `0.0411` n `12`; crypto_alt avg `-0.0462` n `230`; crypto_major avg `-0.0056` n `8`; equity avg `-0.0343` n `92`; fx avg `-0.034` n `6`; index avg `-0.0133` n `25`; metal avg `0.001` n `20`; unknown avg `-0.0167` n `765`
- 4h: commodity avg `0.0862` n `12`; crypto_alt avg `0.0105` n `230`; crypto_major avg `0.0221` n `8`; equity avg `0.0546` n `92`; fx avg `-0.0545` n `6`; index avg `-0.0181` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.1801` n `765`
- 24h: commodity avg `0.6251` n `12`; crypto_alt avg `-1.4778` n `230`; crypto_major avg `-0.6894` n `8`; equity avg `-0.2296` n `92`; fx avg `-0.0395` n `6`; index avg `-0.0975` n `25`; metal avg `-0.1037` n `20`; unknown avg `0.2068` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
