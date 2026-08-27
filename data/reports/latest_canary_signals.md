# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T04:07:27.983363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.0228` n `231`; crypto_major avg `0.0547` n `8`; equity avg `0.0274` n `126`; fx avg `-0.0128` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0169` n `20`; unknown avg `-0.0432` n `793`
- 1h: commodity avg `0.0315` n `12`; crypto_alt avg `-0.0064` n `231`; crypto_major avg `-0.1021` n `8`; equity avg `-0.0179` n `126`; fx avg `-0.0291` n `6`; index avg `-0.0144` n `25`; metal avg `-0.0614` n `20`; unknown avg `-0.2308` n `793`
- 4h: commodity avg `0.0661` n `12`; crypto_alt avg `-0.79` n `231`; crypto_major avg `-0.576` n `8`; equity avg `-0.3582` n `126`; fx avg `-0.0512` n `6`; index avg `-0.0933` n `25`; metal avg `0.0488` n `20`; unknown avg `-0.1027` n `793`
- 24h: commodity avg `0.4682` n `12`; crypto_alt avg `0.2065` n `231`; crypto_major avg `0.3281` n `8`; equity avg `1.1352` n `126`; fx avg `-0.1066` n `6`; index avg `0.1524` n `25`; metal avg `-0.2477` n `20`; unknown avg `0.3917` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
