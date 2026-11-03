# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T02:07:29.259182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0362` n `13`; crypto_alt avg `-0.3539` n `239`; crypto_major avg `-0.3213` n `8`; equity avg `-0.0076` n `157`; fx avg `-0.0351` n `6`; index avg `-0.017` n `27`; metal avg `-0.0512` n `20`; unknown avg `-0.1651` n `1258`
- 1h: commodity avg `-0.0889` n `13`; crypto_alt avg `-0.4657` n `239`; crypto_major avg `-0.3806` n `8`; equity avg `0.1028` n `157`; fx avg `-0.0306` n `6`; index avg `-0.0136` n `27`; metal avg `-0.0544` n `20`; unknown avg `-0.3153` n `1258`
- 4h: commodity avg `0.0312` n `13`; crypto_alt avg `-0.7259` n `239`; crypto_major avg `-0.2314` n `8`; equity avg `0.3713` n `157`; fx avg `-0.0831` n `6`; index avg `0.0425` n `27`; metal avg `-0.0759` n `20`; unknown avg `-0.5808` n `1246`
- 24h: commodity avg `-1.1909` n `13`; crypto_alt avg `-3.2008` n `238`; crypto_major avg `-1.9945` n `8`; equity avg `-2.8862` n `157`; fx avg `0.0698` n `6`; index avg `-0.1449` n `27`; metal avg `0.0286` n `20`; unknown avg `12.3809` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
