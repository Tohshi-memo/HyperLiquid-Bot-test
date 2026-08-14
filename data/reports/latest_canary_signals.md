# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T21:07:31.527529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.032` n `12`; crypto_alt avg `0.1248` n `230`; crypto_major avg `0.0838` n `8`; equity avg `-0.0056` n `114`; fx avg `-0.0034` n `6`; index avg `-0.0021` n `25`; metal avg `0.0136` n `20`; unknown avg `0.1205` n `791`
- 1h: commodity avg `-0.0426` n `12`; crypto_alt avg `0.0761` n `230`; crypto_major avg `-0.0293` n `8`; equity avg `0.0198` n `114`; fx avg `0.012` n `6`; index avg `-0.0028` n `25`; metal avg `0.0137` n `20`; unknown avg `-0.0987` n `791`
- 4h: commodity avg `-0.04` n `12`; crypto_alt avg `0.0254` n `230`; crypto_major avg `-0.1884` n `8`; equity avg `0.1115` n `114`; fx avg `0.0206` n `6`; index avg `0.0331` n `25`; metal avg `-0.0246` n `20`; unknown avg `-0.3749` n `791`
- 24h: commodity avg `0.1671` n `12`; crypto_alt avg `0.4029` n `230`; crypto_major avg `-1.0421` n `8`; equity avg `-0.4023` n `114`; fx avg `0.0928` n `6`; index avg `-0.083` n `25`; metal avg `0.2215` n `20`; unknown avg `-0.0293` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1881`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
