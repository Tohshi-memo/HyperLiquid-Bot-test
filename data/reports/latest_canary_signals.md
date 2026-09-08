# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T22:07:26.173259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `0.2942` n `233`; crypto_major avg `0.229` n `8`; equity avg `-0.0121` n `134`; fx avg `-0.0007` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0458` n `20`; unknown avg `0.4183` n `771`
- 1h: commodity avg `0.0423` n `12`; crypto_alt avg `-0.0931` n `233`; crypto_major avg `0.0371` n `8`; equity avg `-0.0172` n `134`; fx avg `-0.0234` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0328` n `20`; unknown avg `0.213` n `747`
- 4h: commodity avg `0.3799` n `12`; crypto_alt avg `-0.8073` n `233`; crypto_major avg `-0.3643` n `8`; equity avg `-0.5955` n `134`; fx avg `-0.0439` n `6`; index avg `-0.1185` n `26`; metal avg `-0.2602` n `20`; unknown avg `0.3359` n `725`
- 24h: commodity avg `0.085` n `12`; crypto_alt avg `-0.3784` n `232`; crypto_major avg `0.0552` n `8`; equity avg `0.3274` n `134`; fx avg `-0.1313` n `6`; index avg `-0.1638` n `26`; metal avg `-0.3388` n `20`; unknown avg `5.7686` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
