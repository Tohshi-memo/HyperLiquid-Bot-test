# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T14:52:31.688754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.1034` n `233`; crypto_major avg `-0.0981` n `8`; equity avg `-0.0998` n `136`; fx avg `-0.0038` n `6`; index avg `-0.0211` n `27`; metal avg `0.0314` n `20`; unknown avg `0.2442` n `880`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.2118` n `233`; crypto_major avg `-0.1912` n `8`; equity avg `-0.1919` n `136`; fx avg `-0.0286` n `6`; index avg `-0.1124` n `27`; metal avg `-0.0371` n `20`; unknown avg `0.2484` n `878`
- 4h: commodity avg `0.1595` n `12`; crypto_alt avg `-0.5507` n `233`; crypto_major avg `-0.2139` n `8`; equity avg `-0.2817` n `136`; fx avg `0.0131` n `6`; index avg `-0.1096` n `27`; metal avg `-0.0594` n `20`; unknown avg `0.5367` n `872`
- 24h: commodity avg `0.6864` n `12`; crypto_alt avg `-1.0736` n `233`; crypto_major avg `1.0375` n `8`; equity avg `-1.1268` n `136`; fx avg `0.057` n `6`; index avg `-0.3438` n `27`; metal avg `-0.5241` n `20`; unknown avg `1.3048` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
