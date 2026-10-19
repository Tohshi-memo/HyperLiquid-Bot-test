# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T06:52:31.792007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `13`; crypto_alt avg `-0.0865` n `237`; crypto_major avg `-0.0283` n `8`; equity avg `-0.1361` n `151`; fx avg `-0.0011` n `6`; index avg `-0.0324` n `26`; metal avg `0.0059` n `20`; unknown avg `0.6242` n `1194`
- 1h: commodity avg `-0.0374` n `13`; crypto_alt avg `-0.0172` n `237`; crypto_major avg `0.1314` n `8`; equity avg `0.1523` n `151`; fx avg `0.0126` n `6`; index avg `0.0225` n `26`; metal avg `-0.0708` n `20`; unknown avg `1.0945` n `1172`
- 4h: commodity avg `-0.0882` n `13`; crypto_alt avg `-0.1841` n `237`; crypto_major avg `0.0923` n `8`; equity avg `0.2677` n `151`; fx avg `-0.0102` n `6`; index avg `0.0686` n `26`; metal avg `0.0163` n `20`; unknown avg `3.5414` n `1164`
- 24h: commodity avg `-0.4591` n `13`; crypto_alt avg `0.1569` n `237`; crypto_major avg `1.1551` n `8`; equity avg `2.7981` n `151`; fx avg `-0.0367` n `6`; index avg `0.5173` n `26`; metal avg `0.2853` n `20`; unknown avg `2.8363` n `901`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.195`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1187`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0668`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0661`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0654`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
