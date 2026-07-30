# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T11:07:26.767981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `-0.0495` n `230`; crypto_major avg `-0.0451` n `8`; equity avg `0.2211` n `102`; fx avg `-0.0256` n `6`; index avg `0.0186` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.0024` n `779`
- 1h: commodity avg `-0.2128` n `12`; crypto_alt avg `-0.3487` n `230`; crypto_major avg `-0.17` n `8`; equity avg `0.8004` n `102`; fx avg `-0.0716` n `6`; index avg `0.1257` n `25`; metal avg `0.0557` n `20`; unknown avg `-0.0349` n `779`
- 4h: commodity avg `-0.3253` n `12`; crypto_alt avg `-0.1898` n `230`; crypto_major avg `0.4147` n `8`; equity avg `1.3914` n `102`; fx avg `-0.0253` n `6`; index avg `0.184` n `25`; metal avg `0.3732` n `20`; unknown avg `-0.0191` n `771`
- 24h: commodity avg `0.2165` n `12`; crypto_alt avg `-0.3522` n `230`; crypto_major avg `-0.1255` n `8`; equity avg `-1.9576` n `102`; fx avg `-0.0706` n `6`; index avg `-0.3321` n `25`; metal avg `0.5014` n `20`; unknown avg `-0.1204` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
