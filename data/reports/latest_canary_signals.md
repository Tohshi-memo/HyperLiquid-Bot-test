# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T15:07:29.838296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0608` n `12`; crypto_alt avg `-0.1824` n `231`; crypto_major avg `-0.1448` n `8`; equity avg `-0.1015` n `122`; fx avg `0.0008` n `6`; index avg `-0.0172` n `25`; metal avg `-0.0221` n `20`; unknown avg `0.0361` n `795`
- 1h: commodity avg `0.065` n `12`; crypto_alt avg `0.1925` n `231`; crypto_major avg `0.3671` n `8`; equity avg `0.0927` n `122`; fx avg `-0.0147` n `6`; index avg `-0.034` n `25`; metal avg `0.102` n `20`; unknown avg `0.1013` n `795`
- 4h: commodity avg `-0.0502` n `12`; crypto_alt avg `-0.795` n `231`; crypto_major avg `-0.6722` n `8`; equity avg `0.2025` n `122`; fx avg `0.0248` n `6`; index avg `-0.0865` n `25`; metal avg `0.0516` n `20`; unknown avg `-0.1498` n `795`
- 24h: commodity avg `-0.637` n `12`; crypto_alt avg `-1.6883` n `231`; crypto_major avg `-0.8475` n `8`; equity avg `1.9244` n `122`; fx avg `0.0229` n `6`; index avg `0.2345` n `25`; metal avg `-0.4192` n `20`; unknown avg `-1.0336` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
