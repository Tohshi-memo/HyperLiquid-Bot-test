# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T00:52:27.472034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.1734` n `229`; crypto_major avg `-0.1269` n `8`; equity avg `0.0178` n `91`; fx avg `0.0524` n `6`; index avg `-0.0158` n `25`; metal avg `-0.0539` n `20`; unknown avg `-0.0403` n `764`
- 1h: commodity avg `-0.0355` n `12`; crypto_alt avg `-0.199` n `229`; crypto_major avg `-0.1983` n `8`; equity avg `0.1531` n `91`; fx avg `0.0291` n `6`; index avg `0.009` n `25`; metal avg `-0.044` n `20`; unknown avg `-0.1129` n `764`
- 4h: commodity avg `-0.1051` n `12`; crypto_alt avg `0.2723` n `229`; crypto_major avg `0.1798` n `8`; equity avg `0.6341` n `91`; fx avg `0.0161` n `6`; index avg `0.0601` n `25`; metal avg `0.0432` n `20`; unknown avg `-0.15` n `764`
- 24h: commodity avg `0.3808` n `12`; crypto_alt avg `-1.8658` n `229`; crypto_major avg `-2.1921` n `8`; equity avg `0.8161` n `91`; fx avg `-0.0387` n `6`; index avg `-0.1896` n `25`; metal avg `-0.8107` n `20`; unknown avg `-0.1045` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
