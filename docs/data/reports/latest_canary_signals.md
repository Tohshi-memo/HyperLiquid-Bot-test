# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T15:37:26.328681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `13`; crypto_alt avg `-0.1048` n `238`; crypto_major avg `-0.0155` n `8`; equity avg `-0.0055` n `156`; fx avg `0.0076` n `6`; index avg `-0.0063` n `27`; metal avg `0.0015` n `20`; unknown avg `-0.1155` n `1263`
- 1h: commodity avg `0.0042` n `13`; crypto_alt avg `-0.1787` n `238`; crypto_major avg `-0.048` n `8`; equity avg `-0.0039` n `156`; fx avg `0.01` n `6`; index avg `0.0112` n `27`; metal avg `0.0009` n `20`; unknown avg `0.2271` n `1257`
- 4h: commodity avg `0.036` n `13`; crypto_alt avg `-0.0094` n `238`; crypto_major avg `0.0043` n `8`; equity avg `0.0158` n `156`; fx avg `0.0072` n `6`; index avg `0.0436` n `27`; metal avg `-0.0154` n `20`; unknown avg `0.0662` n `1253`
- 24h: commodity avg `0.0503` n `13`; crypto_alt avg `-0.4029` n `238`; crypto_major avg `0.1964` n `8`; equity avg `0.426` n `156`; fx avg `-0.0136` n `6`; index avg `0.0809` n `27`; metal avg `0.0448` n `20`; unknown avg `3.5545` n `1018`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
