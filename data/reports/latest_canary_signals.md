# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T17:52:27.252340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `0.1315` n `230`; crypto_major avg `0.1591` n `8`; equity avg `0.0304` n `96`; fx avg `0.0014` n `6`; index avg `0.0046` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0406` n `770`
- 1h: commodity avg `0.0804` n `12`; crypto_alt avg `0.1961` n `230`; crypto_major avg `0.1941` n `8`; equity avg `0.0365` n `96`; fx avg `0.0014` n `6`; index avg `0.0036` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.0607` n `770`
- 4h: commodity avg `0.095` n `12`; crypto_alt avg `0.5979` n `230`; crypto_major avg `0.6796` n `8`; equity avg `-0.0716` n `96`; fx avg `-0.0526` n `6`; index avg `-0.0128` n `25`; metal avg `-0.0419` n `20`; unknown avg `0.0625` n `770`
- 24h: commodity avg `0.2566` n `12`; crypto_alt avg `-0.7121` n `230`; crypto_major avg `0.1236` n `8`; equity avg `-1.3523` n `96`; fx avg `-0.1075` n `6`; index avg `-0.0832` n `25`; metal avg `0.0102` n `20`; unknown avg `-0.0928` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
