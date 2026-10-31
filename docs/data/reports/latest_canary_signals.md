# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T17:22:31.434951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `13`; crypto_alt avg `-0.1632` n `238`; crypto_major avg `0.0336` n `8`; equity avg `0.0121` n `156`; fx avg `0.003` n `6`; index avg `0.0017` n `27`; metal avg `-0.001` n `20`; unknown avg `0.1962` n `1262`
- 1h: commodity avg `0.0032` n `13`; crypto_alt avg `-0.2623` n `238`; crypto_major avg `-0.0487` n `8`; equity avg `-0.0137` n `156`; fx avg `0.0081` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0005` n `20`; unknown avg `0.0148` n `1256`
- 4h: commodity avg `-0.0877` n `13`; crypto_alt avg `0.7453` n `238`; crypto_major avg `0.2062` n `8`; equity avg `0.1543` n `156`; fx avg `-0.0014` n `6`; index avg `0.0097` n `27`; metal avg `0.0229` n `20`; unknown avg `3.5868` n `1236`
- 24h: commodity avg `-0.5376` n `13`; crypto_alt avg `1.0006` n `238`; crypto_major avg `-0.1307` n `8`; equity avg `0.8812` n `156`; fx avg `-0.0097` n `6`; index avg `0.0029` n `27`; metal avg `0.04` n `20`; unknown avg `1.9156` n `1081`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
