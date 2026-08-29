# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T17:37:27.265055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `-0.0812` n `231`; crypto_major avg `-0.0822` n `8`; equity avg `-0.0031` n `128`; fx avg `0.0084` n `6`; index avg `0.0014` n `26`; metal avg `0.0042` n `20`; unknown avg `0.0002` n `792`
- 1h: commodity avg `0.0062` n `12`; crypto_alt avg `-0.3506` n `231`; crypto_major avg `-0.2394` n `8`; equity avg `-0.013` n `128`; fx avg `0.0069` n `6`; index avg `-0.0004` n `26`; metal avg `0.0165` n `20`; unknown avg `0.0929` n `792`
- 4h: commodity avg `-0.0135` n `12`; crypto_alt avg `0.3269` n `231`; crypto_major avg `0.4668` n `8`; equity avg `0.0225` n `128`; fx avg `0.0062` n `6`; index avg `0.0081` n `26`; metal avg `0.0578` n `20`; unknown avg `0.1421` n `778`
- 24h: commodity avg `0.0195` n `12`; crypto_alt avg `0.3718` n `231`; crypto_major avg `0.4124` n `8`; equity avg `0.1385` n `128`; fx avg `-0.0367` n `6`; index avg `0.0191` n `26`; metal avg `-0.0341` n `20`; unknown avg `-0.0319` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2252`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
