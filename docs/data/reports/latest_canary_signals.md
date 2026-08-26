# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T05:37:26.021105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `0.347` n `231`; crypto_major avg `0.4729` n `8`; equity avg `0.0349` n `122`; fx avg `0.0114` n `6`; index avg `0.0154` n `25`; metal avg `-0.0147` n `20`; unknown avg `0.0765` n `797`
- 1h: commodity avg `0.0759` n `12`; crypto_alt avg `-0.174` n `231`; crypto_major avg `0.0734` n `8`; equity avg `-0.2063` n `122`; fx avg `0.0014` n `6`; index avg `-0.0318` n `25`; metal avg `-0.0063` n `20`; unknown avg `7.0109` n `797`
- 4h: commodity avg `0.0702` n `12`; crypto_alt avg `0.2751` n `231`; crypto_major avg `0.2663` n `8`; equity avg `0.5376` n `122`; fx avg `-0.0199` n `6`; index avg `0.1408` n `25`; metal avg `0.0659` n `20`; unknown avg `7.8711` n `796`
- 24h: commodity avg `-0.6981` n `12`; crypto_alt avg `-3.0521` n `231`; crypto_major avg `-2.7762` n `8`; equity avg `0.7992` n `122`; fx avg `0.0109` n `6`; index avg `0.1225` n `25`; metal avg `0.1885` n `20`; unknown avg `0.4959` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
