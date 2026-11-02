# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T01:07:27.782916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0702` n `13`; crypto_alt avg `0.1535` n `238`; crypto_major avg `0.1952` n `8`; equity avg `0.2359` n `156`; fx avg `-0.0036` n `6`; index avg `-0.0005` n `27`; metal avg `0.0387` n `20`; unknown avg `0.0285` n `1255`
- 1h: commodity avg `-0.0938` n `13`; crypto_alt avg `-0.1348` n `238`; crypto_major avg `-0.005` n `8`; equity avg `0.3642` n `156`; fx avg `0.084` n `6`; index avg `0.1228` n `27`; metal avg `0.0235` n `20`; unknown avg `1.5752` n `1253`
- 4h: commodity avg `-0.026` n `13`; crypto_alt avg `0.045` n `238`; crypto_major avg `0.3878` n `8`; equity avg `0.6334` n `156`; fx avg `0.1149` n `6`; index avg `0.2045` n `27`; metal avg `0.1765` n `20`; unknown avg `0.7614` n `1225`
- 24h: commodity avg `-0.0111` n `13`; crypto_alt avg `-0.6585` n `238`; crypto_major avg `0.0331` n `8`; equity avg `0.93` n `156`; fx avg `0.1045` n `6`; index avg `0.2663` n `27`; metal avg `0.2062` n `20`; unknown avg `1.8542` n `1126`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
