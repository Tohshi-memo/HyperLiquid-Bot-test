# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T08:22:36.284586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `13`; crypto_alt avg `-0.0042` n `239`; crypto_major avg `-0.1296` n `8`; equity avg `-0.0174` n `157`; fx avg `0.0039` n `6`; index avg `-0.0027` n `27`; metal avg `0.0049` n `20`; unknown avg `18.0739` n `1264`
- 1h: commodity avg `-0.0142` n `13`; crypto_alt avg `-0.0131` n `239`; crypto_major avg `-0.1376` n `8`; equity avg `0.3394` n `157`; fx avg `0.0275` n `6`; index avg `0.0636` n `27`; metal avg `-0.0141` n `20`; unknown avg `0.7567` n `1242`
- 4h: commodity avg `0.3531` n `13`; crypto_alt avg `-0.4619` n `239`; crypto_major avg `-0.2396` n `8`; equity avg `-0.0388` n `157`; fx avg `0.0575` n `6`; index avg `0.0301` n `27`; metal avg `-0.2333` n `20`; unknown avg `17.9852` n `1204`
- 24h: commodity avg `-0.4615` n `13`; crypto_alt avg `-2.4962` n `238`; crypto_major avg `-1.6627` n `8`; equity avg `-4.1049` n `157`; fx avg `0.0025` n `6`; index avg `-0.2697` n `27`; metal avg `-0.4193` n `20`; unknown avg `4.1925` n `1019`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
