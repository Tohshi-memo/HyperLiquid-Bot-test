# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T17:52:32.917422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `0.0287` n `233`; crypto_major avg `0.0085` n `8`; equity avg `0.0028` n `135`; fx avg `-0.0023` n `6`; index avg `-0.013` n `26`; metal avg `-0.0313` n `20`; unknown avg `0.2277` n `797`
- 1h: commodity avg `0.101` n `12`; crypto_alt avg `0.7697` n `233`; crypto_major avg `0.6991` n `8`; equity avg `-0.0141` n `135`; fx avg `-0.0065` n `6`; index avg `-0.0345` n `26`; metal avg `-0.0305` n `20`; unknown avg `1.1751` n `794`
- 4h: commodity avg `0.4864` n `12`; crypto_alt avg `0.3713` n `233`; crypto_major avg `0.2935` n `8`; equity avg `0.0726` n `135`; fx avg `0.04` n `6`; index avg `-0.0214` n `26`; metal avg `-0.2516` n `20`; unknown avg `-0.3109` n `760`
- 24h: commodity avg `0.9729` n `12`; crypto_alt avg `-4.0981` n `233`; crypto_major avg `-3.3163` n `8`; equity avg `-1.98` n `135`; fx avg `0.0806` n `6`; index avg `-0.3243` n `26`; metal avg `-1.2313` n `20`; unknown avg `-0.8958` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
