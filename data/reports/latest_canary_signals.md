# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T14:52:25.185177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.834` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0463` n `12`; crypto_alt avg `-0.0996` n `230`; crypto_major avg `-0.0092` n `8`; equity avg `-0.0226` n `113`; fx avg `-0.0115` n `6`; index avg `-0.0276` n `25`; metal avg `-0.0471` n `20`; unknown avg `-0.0586` n `786`
- 1h: commodity avg `0.0493` n `12`; crypto_alt avg `-0.6394` n `230`; crypto_major avg `-0.4092` n `8`; equity avg `0.0213` n `113`; fx avg `-0.0055` n `6`; index avg `-0.0234` n `25`; metal avg `-0.0791` n `20`; unknown avg `-0.0147` n `786`
- 4h: commodity avg `-0.0823` n `12`; crypto_alt avg `-0.6079` n `230`; crypto_major avg `-0.7999` n `8`; equity avg `1.0341` n `113`; fx avg `-0.0061` n `6`; index avg `0.1419` n `25`; metal avg `-0.0394` n `20`; unknown avg `0.0302` n `786`
- 24h: commodity avg `0.1983` n `12`; crypto_alt avg `-0.9044` n `230`; crypto_major avg `0.6446` n `8`; equity avg `2.6719` n `113`; fx avg `0.0374` n `6`; index avg `0.2685` n `25`; metal avg `0.2002` n `20`; unknown avg `-0.0979` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2095`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
