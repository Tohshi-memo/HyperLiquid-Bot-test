# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T10:37:23.911371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0765` n `13`; crypto_alt avg `0.0577` n `239`; crypto_major avg `0.219` n `8`; equity avg `0.1526` n `161`; fx avg `-0.0106` n `6`; index avg `0.0124` n `27`; metal avg `0.007` n `20`; unknown avg `0.3415` n `1259`
- 1h: commodity avg `0.2222` n `13`; crypto_alt avg `0.8108` n `239`; crypto_major avg `0.7825` n `8`; equity avg `0.3429` n `161`; fx avg `0.0519` n `6`; index avg `-0.0028` n `27`; metal avg `0.0766` n `20`; unknown avg `0.36` n `1253`
- 4h: commodity avg `0.2648` n `13`; crypto_alt avg `0.3411` n `239`; crypto_major avg `0.3921` n `8`; equity avg `0.3868` n `161`; fx avg `-0.0191` n `6`; index avg `-0.0529` n `27`; metal avg `0.1017` n `20`; unknown avg `40.8807` n `1223`
- 24h: commodity avg `1.0155` n `13`; crypto_alt avg `-0.3173` n `239`; crypto_major avg `-0.9322` n `8`; equity avg `2.4228` n `161`; fx avg `-0.2257` n `6`; index avg `0.231` n `27`; metal avg `0.2766` n `20`; unknown avg `1.3873` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
