# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T13:52:29.863912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0381` n `13`; crypto_alt avg `0.0547` n `239`; crypto_major avg `-0.0394` n `8`; equity avg `0.1207` n `166`; fx avg `0.0038` n `6`; index avg `0.0136` n `27`; metal avg `-0.0053` n `20`; unknown avg `0.7244` n `1263`
- 1h: commodity avg `0.1408` n `13`; crypto_alt avg `-0.4272` n `239`; crypto_major avg `-0.5307` n `8`; equity avg `-0.3732` n `166`; fx avg `0.0166` n `6`; index avg `-0.0497` n `27`; metal avg `-0.2161` n `20`; unknown avg `318.2826` n `1257`
- 4h: commodity avg `0.1748` n `13`; crypto_alt avg `-1.0615` n `239`; crypto_major avg `-0.4994` n `8`; equity avg `-0.8371` n `166`; fx avg `0.0796` n `6`; index avg `-0.1673` n `27`; metal avg `0.016` n `20`; unknown avg `532.792` n `1220`
- 24h: commodity avg `0.0643` n `13`; crypto_alt avg `-1.6215` n `239`; crypto_major avg `-1.4675` n `8`; equity avg `1.5813` n `166`; fx avg `0.0982` n `6`; index avg `0.3253` n `27`; metal avg `-0.113` n `20`; unknown avg `0.4132` n `1142`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
