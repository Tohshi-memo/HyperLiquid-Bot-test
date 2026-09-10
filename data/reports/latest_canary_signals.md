# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T18:22:31.807393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.041` n `12`; crypto_alt avg `0.0051` n `233`; crypto_major avg `-0.0606` n `8`; equity avg `-0.0905` n `135`; fx avg `-0.007` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0248` n `20`; unknown avg `-0.0478` n `797`
- 1h: commodity avg `0.1913` n `12`; crypto_alt avg `-0.0913` n `233`; crypto_major avg `-0.1423` n `8`; equity avg `-0.2418` n `135`; fx avg `-0.0037` n `6`; index avg `-0.0449` n `26`; metal avg `-0.1141` n `20`; unknown avg `0.0227` n `795`
- 4h: commodity avg `0.6389` n `12`; crypto_alt avg `-0.0593` n `233`; crypto_major avg `-0.1891` n `8`; equity avg `-0.3013` n `135`; fx avg `0.0308` n `6`; index avg `-0.0762` n `26`; metal avg `-0.2708` n `20`; unknown avg `-0.1544` n `760`
- 24h: commodity avg `1.0689` n `12`; crypto_alt avg `-4.4421` n `233`; crypto_major avg `-3.6505` n `8`; equity avg `-2.1613` n `135`; fx avg `0.0965` n `6`; index avg `-0.3267` n `26`; metal avg `-1.3158` n `20`; unknown avg `-0.7261` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
