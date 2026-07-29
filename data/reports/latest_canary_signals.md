# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T07:37:34.092641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0318` n `12`; crypto_alt avg `0.0173` n `230`; crypto_major avg `0.017` n `8`; equity avg `0.0659` n `102`; fx avg `0.0118` n `6`; index avg `0.0348` n `25`; metal avg `0.0178` n `20`; unknown avg `0.0296` n `777`
- 1h: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.1051` n `230`; crypto_major avg `-0.1311` n `8`; equity avg `0.4407` n `102`; fx avg `0.0197` n `6`; index avg `0.155` n `25`; metal avg `0.052` n `20`; unknown avg `0.1185` n `777`
- 4h: commodity avg `-0.1094` n `12`; crypto_alt avg `0.0983` n `230`; crypto_major avg `0.8101` n `8`; equity avg `1.3906` n `102`; fx avg `-0.0522` n `6`; index avg `0.3449` n `25`; metal avg `0.1984` n `20`; unknown avg `0.0983` n `761`
- 24h: commodity avg `-0.1083` n `12`; crypto_alt avg `-1.3047` n `230`; crypto_major avg `1.151` n `8`; equity avg `-1.0581` n `102`; fx avg `-0.1198` n `6`; index avg `-0.1341` n `25`; metal avg `0.0537` n `20`; unknown avg `-0.1495` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
