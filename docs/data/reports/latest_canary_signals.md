# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T20:22:29.839573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `0.0981` n `230`; crypto_major avg `0.1173` n `8`; equity avg `-0.1413` n `98`; fx avg `-0.0062` n `6`; index avg `-0.0188` n `25`; metal avg `0.0066` n `20`; unknown avg `0.005` n `770`
- 1h: commodity avg `-0.1184` n `12`; crypto_alt avg `0.1773` n `230`; crypto_major avg `0.1246` n `8`; equity avg `-0.1525` n `98`; fx avg `-0.0112` n `6`; index avg `-0.0152` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.1226` n `770`
- 4h: commodity avg `0.1885` n `12`; crypto_alt avg `0.1014` n `230`; crypto_major avg `-0.2048` n `8`; equity avg `-1.1889` n `98`; fx avg `-0.0198` n `6`; index avg `-0.266` n `25`; metal avg `-0.1535` n `20`; unknown avg `-0.1868` n `770`
- 24h: commodity avg `-0.4092` n `12`; crypto_alt avg `1.6031` n `230`; crypto_major avg `1.1995` n `8`; equity avg `-0.3579` n `98`; fx avg `-0.2124` n `6`; index avg `0.0096` n `25`; metal avg `0.0884` n `20`; unknown avg `0.1623` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1062`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0934`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0851`, n `666`, weak_sample_signal
