# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T15:22:34.281059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0352` n `12`; crypto_alt avg `0.1474` n `230`; crypto_major avg `0.0075` n `8`; equity avg `0.2181` n `112`; fx avg `0.0107` n `6`; index avg `0.0259` n `25`; metal avg `0.0167` n `20`; unknown avg `-0.0148` n `782`
- 1h: commodity avg `0.1153` n `12`; crypto_alt avg `-0.1218` n `230`; crypto_major avg `-0.1979` n `8`; equity avg `0.4306` n `112`; fx avg `0.005` n `6`; index avg `0.0614` n `25`; metal avg `0.0247` n `20`; unknown avg `-0.0481` n `782`
- 4h: commodity avg `0.4251` n `12`; crypto_alt avg `-0.4194` n `230`; crypto_major avg `-0.2991` n `8`; equity avg `0.0873` n `112`; fx avg `-0.0174` n `6`; index avg `0.0308` n `25`; metal avg `-0.036` n `20`; unknown avg `-0.0177` n `782`
- 24h: commodity avg `0.3761` n `12`; crypto_alt avg `-0.3606` n `230`; crypto_major avg `-0.0955` n `8`; equity avg `0.5745` n `112`; fx avg `-0.1062` n `6`; index avg `-0.0206` n `25`; metal avg `0.3652` n `20`; unknown avg `0.0173` n `765`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
