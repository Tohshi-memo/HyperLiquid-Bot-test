# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T22:07:26.745573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.4935` n `230`; crypto_major avg `-0.4255` n `8`; equity avg `-0.1898` n `92`; fx avg `-0.0384` n `6`; index avg `-0.063` n `25`; metal avg `-0.1389` n `20`; unknown avg `0.1176` n `765`
- 1h: commodity avg `-0.111` n `12`; crypto_alt avg `-0.8729` n `230`; crypto_major avg `-0.8274` n `8`; equity avg `-0.2098` n `92`; fx avg `-0.0273` n `6`; index avg `-0.0686` n `25`; metal avg `-0.1649` n `20`; unknown avg `0.4608` n `765`
- 4h: commodity avg `-0.0658` n `12`; crypto_alt avg `-0.7381` n `230`; crypto_major avg `-0.6986` n `8`; equity avg `-0.1275` n `92`; fx avg `-0.0753` n `6`; index avg `-0.0662` n `25`; metal avg `-0.1642` n `20`; unknown avg `0.1585` n `765`
- 24h: commodity avg `0.5198` n `12`; crypto_alt avg `-2.0378` n `230`; crypto_major avg `-1.3959` n `8`; equity avg `-0.4518` n `92`; fx avg `-0.072` n `6`; index avg `-0.1685` n `25`; metal avg `-0.2549` n `20`; unknown avg `0.2276` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
