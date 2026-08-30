# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T14:07:24.145155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.0514` n `231`; crypto_major avg `-0.0285` n `8`; equity avg `0.0072` n `128`; fx avg `-0.0014` n `6`; index avg `-0.0156` n `26`; metal avg `0.0239` n `20`; unknown avg `1.3042` n `793`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `0.0403` n `231`; crypto_major avg `0.3216` n `8`; equity avg `0.0292` n `128`; fx avg `-0.0035` n `6`; index avg `0.0017` n `26`; metal avg `0.0424` n `20`; unknown avg `-0.1099` n `793`
- 4h: commodity avg `0.0126` n `12`; crypto_alt avg `0.9942` n `231`; crypto_major avg `1.0514` n `8`; equity avg `0.0497` n `128`; fx avg `-0.0079` n `6`; index avg `0.0082` n `26`; metal avg `0.0554` n `20`; unknown avg `0.923` n `789`
- 24h: commodity avg `-0.0244` n `12`; crypto_alt avg `1.7193` n `231`; crypto_major avg `1.5393` n `8`; equity avg `0.3167` n `128`; fx avg `0.0173` n `6`; index avg `0.0887` n `26`; metal avg `0.1278` n `20`; unknown avg `-0.0216` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
