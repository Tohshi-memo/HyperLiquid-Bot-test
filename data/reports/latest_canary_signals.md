# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T12:22:27.397337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2198` n `13`; crypto_alt avg `0.5899` n `239`; crypto_major avg `0.7109` n `8`; equity avg `0.337` n `157`; fx avg `-0.0007` n `6`; index avg `0.046` n `27`; metal avg `0.1121` n `20`; unknown avg `0.5456` n `1264`
- 1h: commodity avg `-0.1901` n `13`; crypto_alt avg `0.6106` n `239`; crypto_major avg `0.7398` n `8`; equity avg `0.1628` n `157`; fx avg `0.0113` n `6`; index avg `0.0301` n `27`; metal avg `0.072` n `20`; unknown avg `-0.0489` n `1252`
- 4h: commodity avg `0.0267` n `13`; crypto_alt avg `1.7859` n `239`; crypto_major avg `1.4114` n `8`; equity avg `0.9194` n `157`; fx avg `0.0483` n `6`; index avg `0.0773` n `27`; metal avg `0.016` n `20`; unknown avg `1.04` n `1212`
- 24h: commodity avg `-0.3953` n `13`; crypto_alt avg `-0.9322` n `238`; crypto_major avg `-0.3427` n `8`; equity avg `-3.3626` n `157`; fx avg `0.0216` n `6`; index avg `-0.2171` n `27`; metal avg `-0.3728` n `20`; unknown avg `4.3415` n `1020`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
