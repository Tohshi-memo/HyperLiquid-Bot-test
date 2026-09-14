# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T15:52:27.542327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0666` n `12`; crypto_alt avg `0.1685` n `233`; crypto_major avg `0.2101` n `8`; equity avg `0.0251` n `136`; fx avg `0.0175` n `6`; index avg `0.0105` n `27`; metal avg `-0.0496` n `20`; unknown avg `-0.0845` n `894`
- 1h: commodity avg `-0.1292` n `12`; crypto_alt avg `0.412` n `233`; crypto_major avg `0.4203` n `8`; equity avg `0.7921` n `136`; fx avg `-0.01` n `6`; index avg `0.1544` n `27`; metal avg `0.1333` n `20`; unknown avg `-0.1283` n `892`
- 4h: commodity avg `-0.1014` n `12`; crypto_alt avg `0.0388` n `233`; crypto_major avg `0.3347` n `8`; equity avg `0.7955` n `136`; fx avg `-0.008` n `6`; index avg `0.0585` n `27`; metal avg `0.0864` n `20`; unknown avg `0.805` n `872`
- 24h: commodity avg `0.4473` n `12`; crypto_alt avg `-0.1072` n `233`; crypto_major avg `1.6808` n `8`; equity avg `-0.2083` n `136`; fx avg `0.0423` n `6`; index avg `-0.1536` n `27`; metal avg `-0.3679` n `20`; unknown avg `0.962` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
