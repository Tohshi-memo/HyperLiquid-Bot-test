# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T01:37:27.776163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `-0.0839` n `233`; crypto_major avg `-0.1217` n `8`; equity avg `-0.0302` n `136`; fx avg `0.0012` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.1334` n `838`
- 1h: commodity avg `-0.0384` n `12`; crypto_alt avg `0.1195` n `233`; crypto_major avg `0.0199` n `8`; equity avg `-0.0144` n `136`; fx avg `-0.0021` n `6`; index avg `-0.0025` n `26`; metal avg `0.0043` n `20`; unknown avg `2.8157` n `836`
- 4h: commodity avg `-0.0207` n `12`; crypto_alt avg `0.4499` n `233`; crypto_major avg `-0.0016` n `8`; equity avg `-0.0608` n `136`; fx avg `0.0008` n `6`; index avg `-0.0115` n `26`; metal avg `-0.004` n `20`; unknown avg `3.7467` n `804`
- 24h: commodity avg `0.0002` n `12`; crypto_alt avg `1.1249` n `233`; crypto_major avg `0.1857` n `8`; equity avg `-0.4278` n `136`; fx avg `-0.0152` n `6`; index avg `-0.0418` n `26`; metal avg `0.0206` n `20`; unknown avg `0.8934` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
