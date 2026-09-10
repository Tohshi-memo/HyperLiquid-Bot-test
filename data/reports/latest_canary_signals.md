# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T23:37:27.081501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0317` n `12`; crypto_alt avg `0.0103` n `233`; crypto_major avg `0.0317` n `8`; equity avg `0.0042` n `136`; fx avg `0.0131` n `6`; index avg `0.0048` n `26`; metal avg `-0.0232` n `20`; unknown avg `-0.115` n `796`
- 1h: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.588` n `233`; crypto_major avg `-0.4182` n `8`; equity avg `-0.0836` n `136`; fx avg `0.0169` n `6`; index avg `-0.0048` n `26`; metal avg `0.0183` n `20`; unknown avg `-0.3945` n `786`
- 4h: commodity avg `0.1863` n `12`; crypto_alt avg `-0.9597` n `233`; crypto_major avg `-0.7068` n `8`; equity avg `-0.3666` n `136`; fx avg `0.0316` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0447` n `20`; unknown avg `-0.23` n `716`
- 24h: commodity avg `1.1285` n `12`; crypto_alt avg `-2.6819` n `233`; crypto_major avg `-2.3708` n `8`; equity avg `-2.1382` n `136`; fx avg `0.1581` n `6`; index avg `-0.3261` n `26`; metal avg `-1.2785` n `20`; unknown avg `-1.1717` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
