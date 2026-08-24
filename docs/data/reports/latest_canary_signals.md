# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T07:37:24.003970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `-0.1554` n `231`; crypto_major avg `-0.33` n `8`; equity avg `0.0423` n `122`; fx avg `0.0098` n `6`; index avg `0.0159` n `25`; metal avg `-0.0069` n `20`; unknown avg `0.0178` n `793`
- 1h: commodity avg `0.0942` n `12`; crypto_alt avg `0.0984` n `231`; crypto_major avg `0.1329` n `8`; equity avg `0.1167` n `122`; fx avg `0.0461` n `6`; index avg `0.0314` n `25`; metal avg `-0.0318` n `20`; unknown avg `-0.0238` n `793`
- 4h: commodity avg `0.0214` n `12`; crypto_alt avg `0.4683` n `231`; crypto_major avg `0.3891` n `8`; equity avg `-0.0836` n `122`; fx avg `0.0516` n `6`; index avg `-0.0123` n `25`; metal avg `0.013` n `20`; unknown avg `-0.0845` n `777`
- 24h: commodity avg `-0.2705` n `12`; crypto_alt avg `3.3625` n `231`; crypto_major avg `1.5733` n `8`; equity avg `-1.0972` n `122`; fx avg `-0.1948` n `6`; index avg `-0.0906` n `25`; metal avg `0.2195` n `20`; unknown avg `5.255` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
