# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T06:07:31.974085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `0.0317` n `230`; crypto_major avg `0.0865` n `8`; equity avg `0.1425` n `102`; fx avg `-0.0115` n `6`; index avg `0.0015` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.026` n `747`
- 1h: commodity avg `0.2115` n `12`; crypto_alt avg `0.2761` n `230`; crypto_major avg `0.2866` n `8`; equity avg `0.6991` n `102`; fx avg `-0.0069` n `6`; index avg `0.0551` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.0401` n `747`
- 4h: commodity avg `0.3036` n `12`; crypto_alt avg `-0.3363` n `230`; crypto_major avg `-0.4634` n `8`; equity avg `-1.234` n `102`; fx avg `-0.1105` n `6`; index avg `-0.3184` n `25`; metal avg `-0.4347` n `20`; unknown avg `0.0765` n `747`
- 24h: commodity avg `0.7816` n `12`; crypto_alt avg `-0.2066` n `230`; crypto_major avg `-0.3062` n `8`; equity avg `-1.906` n `102`; fx avg `0.0037` n `6`; index avg `-0.0711` n `25`; metal avg `-0.1112` n `20`; unknown avg `-0.5361` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
