# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T23:52:26.285717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0915` n `12`; crypto_alt avg `-0.1024` n `233`; crypto_major avg `-0.1414` n `8`; equity avg `-0.0822` n `136`; fx avg `0.0038` n `6`; index avg `-0.0363` n `26`; metal avg `-0.0236` n `20`; unknown avg `-0.0744` n `796`
- 1h: commodity avg `0.1108` n `12`; crypto_alt avg `-0.5498` n `233`; crypto_major avg `-0.4374` n `8`; equity avg `-0.1247` n `136`; fx avg `0.0261` n `6`; index avg `-0.0339` n `26`; metal avg `-0.0222` n `20`; unknown avg `-0.2692` n `794`
- 4h: commodity avg `0.2919` n `12`; crypto_alt avg `-0.9048` n `233`; crypto_major avg `-0.7565` n `8`; equity avg `-0.3355` n `136`; fx avg `0.0353` n `6`; index avg `-0.0481` n `26`; metal avg `-0.0446` n `20`; unknown avg `-0.1927` n `716`
- 24h: commodity avg `1.2347` n `12`; crypto_alt avg `-2.9274` n `233`; crypto_major avg `-2.6028` n `8`; equity avg `-2.2295` n `136`; fx avg `0.1466` n `6`; index avg `-0.3766` n `26`; metal avg `-1.2818` n `20`; unknown avg `-1.1246` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
