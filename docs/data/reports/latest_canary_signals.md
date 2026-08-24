# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T09:58:57.918031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `-0.1302` n `231`; crypto_major avg `-0.0409` n `8`; equity avg `-0.0127` n `122`; fx avg `0.0229` n `6`; index avg `-0.0024` n `25`; metal avg `0.0591` n `20`; unknown avg `0.0502` n `793`
- 1h: commodity avg `0.0824` n `12`; crypto_alt avg `0.4622` n `231`; crypto_major avg `0.5263` n `8`; equity avg `0.032` n `122`; fx avg `-0.0217` n `6`; index avg `0.0011` n `25`; metal avg `0.0405` n `20`; unknown avg `0.2672` n `793`
- 4h: commodity avg `0.07` n `12`; crypto_alt avg `-0.0473` n `231`; crypto_major avg `0.0577` n `8`; equity avg `0.1256` n `122`; fx avg `0.0205` n `6`; index avg `0.0184` n `25`; metal avg `0.0199` n `20`; unknown avg `0.4213` n `777`
- 24h: commodity avg `-0.171` n `12`; crypto_alt avg `1.9541` n `231`; crypto_major avg `0.6004` n `8`; equity avg `-1.2107` n `122`; fx avg `-0.1525` n `6`; index avg `-0.1096` n `25`; metal avg `0.1771` n `20`; unknown avg `5.6131` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
