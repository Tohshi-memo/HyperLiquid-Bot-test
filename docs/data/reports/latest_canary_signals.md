# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T04:52:27.435938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0615` n `12`; crypto_alt avg `-0.0273` n `233`; crypto_major avg `0.0653` n `8`; equity avg `0.0542` n `136`; fx avg `0.0088` n `6`; index avg `0.0099` n `26`; metal avg `0.0223` n `20`; unknown avg `1.7992` n `796`
- 1h: commodity avg `-0.1981` n `12`; crypto_alt avg `0.7557` n `233`; crypto_major avg `0.5758` n `8`; equity avg `0.3824` n `136`; fx avg `-0.0158` n `6`; index avg `0.1019` n `26`; metal avg `0.2` n `20`; unknown avg `17.3809` n `788`
- 4h: commodity avg `-0.2023` n `12`; crypto_alt avg `0.6893` n `233`; crypto_major avg `0.5801` n `8`; equity avg `-0.0301` n `136`; fx avg `-0.067` n `6`; index avg `0.0718` n `26`; metal avg `0.0168` n `20`; unknown avg `-0.0855` n `780`
- 24h: commodity avg `1.0178` n `12`; crypto_alt avg `-1.3479` n `233`; crypto_major avg `-1.9032` n `8`; equity avg `-1.9235` n `136`; fx avg `0.0739` n `6`; index avg `-0.2991` n `26`; metal avg `-1.1938` n `20`; unknown avg `-0.0779` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
