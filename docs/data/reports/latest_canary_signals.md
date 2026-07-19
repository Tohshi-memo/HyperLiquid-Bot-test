# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T01:07:31.976784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.0655` n `230`; crypto_major avg `-0.0431` n `8`; equity avg `-0.0027` n `96`; fx avg `0.0024` n `6`; index avg `-0.0018` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.1625` n `770`
- 1h: commodity avg `0.0161` n `12`; crypto_alt avg `-0.0939` n `230`; crypto_major avg `0.0144` n `8`; equity avg `0.1218` n `96`; fx avg `0.0376` n `6`; index avg `-0.0045` n `25`; metal avg `0.0051` n `20`; unknown avg `-0.3128` n `770`
- 4h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.132` n `230`; crypto_major avg `0.1432` n `8`; equity avg `0.1767` n `96`; fx avg `0.0355` n `6`; index avg `-0.002` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.1741` n `770`
- 24h: commodity avg `0.3549` n `12`; crypto_alt avg `-0.2141` n `230`; crypto_major avg `0.7104` n `8`; equity avg `-0.1716` n `96`; fx avg `-0.0581` n `6`; index avg `0.0188` n `25`; metal avg `-0.0643` n `20`; unknown avg `0.0515` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
