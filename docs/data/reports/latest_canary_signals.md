# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T10:50:12.330922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0534` n `12`; crypto_alt avg `-0.3127` n `227`; crypto_major avg `-0.2213` n `8`; equity avg `-0.1455` n `106`; fx avg `0.0075` n `6`; index avg `-0.0236` n `25`; metal avg `-0.0302` n `20`; unknown avg `0.0103` n `785`
- 1h: commodity avg `0.0277` n `12`; crypto_alt avg `0.0384` n `231`; crypto_major avg `0.1691` n `8`; equity avg `-0.1223` n `122`; fx avg `0.0108` n `6`; index avg `-0.021` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0011` n `793`
- 4h: commodity avg `0.1882` n `12`; crypto_alt avg `0.0806` n `231`; crypto_major avg `-0.1607` n `8`; equity avg `0.0433` n `122`; fx avg `0.0095` n `6`; index avg `0.0283` n `25`; metal avg `-0.1085` n `20`; unknown avg `0.3965` n `793`
- 24h: commodity avg `-0.1656` n `12`; crypto_alt avg `1.4246` n `231`; crypto_major avg `0.5248` n `8`; equity avg `-1.374` n `122`; fx avg `-0.1266` n `6`; index avg `-0.1392` n `25`; metal avg `0.1457` n `20`; unknown avg `5.0758` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
