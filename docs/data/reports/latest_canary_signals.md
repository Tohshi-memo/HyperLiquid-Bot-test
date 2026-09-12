# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T16:53:04.949440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `-0.0786` n `233`; crypto_major avg `-0.0009` n `8`; equity avg `-0.0124` n `136`; fx avg `-0.0029` n `6`; index avg `0.0025` n `26`; metal avg `0.0008` n `20`; unknown avg `1.1267` n `838`
- 1h: commodity avg `0.0371` n `12`; crypto_alt avg `-0.0506` n `233`; crypto_major avg `-0.0578` n `8`; equity avg `0.0264` n `136`; fx avg `-0.0016` n `6`; index avg `0.007` n `26`; metal avg `0.0093` n `20`; unknown avg `-0.5389` n `830`
- 4h: commodity avg `0.0051` n `12`; crypto_alt avg `0.2235` n `233`; crypto_major avg `-0.0445` n `8`; equity avg `0.0086` n `136`; fx avg `-0.0028` n `6`; index avg `0.0207` n `26`; metal avg `0.0181` n `20`; unknown avg `2.2459` n `830`
- 24h: commodity avg `-0.1677` n `12`; crypto_alt avg `0.0903` n `233`; crypto_major avg `-0.7403` n `8`; equity avg `-0.1567` n `136`; fx avg `-0.0242` n `6`; index avg `0.0275` n `26`; metal avg `-0.0254` n `20`; unknown avg `11.6166` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
