# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T02:37:27.476456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0501` n `12`; crypto_alt avg `0.1688` n `230`; crypto_major avg `0.2069` n `8`; equity avg `-0.0206` n `96`; fx avg `-0.0097` n `6`; index avg `0.0075` n `25`; metal avg `-0.0096` n `20`; unknown avg `-0.2909` n `770`
- 1h: commodity avg `-0.1073` n `12`; crypto_alt avg `0.3229` n `230`; crypto_major avg `0.513` n `8`; equity avg `0.0362` n `96`; fx avg `0.0102` n `6`; index avg `0.0061` n `25`; metal avg `0.0151` n `20`; unknown avg `0.0561` n `770`
- 4h: commodity avg `-0.0803` n `12`; crypto_alt avg `0.3803` n `230`; crypto_major avg `0.6207` n `8`; equity avg `0.2089` n `96`; fx avg `0.046` n `6`; index avg `-0.0148` n `25`; metal avg `0.0516` n `20`; unknown avg `-0.5579` n `770`
- 24h: commodity avg `0.2611` n `12`; crypto_alt avg `-0.0221` n `230`; crypto_major avg `0.9782` n `8`; equity avg `-0.1761` n `96`; fx avg `-0.0193` n `6`; index avg `-0.0044` n `25`; metal avg `-0.017` n `20`; unknown avg `0.0869` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
