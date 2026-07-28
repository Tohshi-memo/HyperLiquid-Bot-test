# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T20:22:31.361124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `12`; crypto_alt avg `0.1013` n `230`; crypto_major avg `0.0771` n `8`; equity avg `0.4402` n `102`; fx avg `0.0071` n `6`; index avg `0.0135` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.0101` n `776`
- 1h: commodity avg `-0.0065` n `12`; crypto_alt avg `0.2032` n `230`; crypto_major avg `0.2847` n `8`; equity avg `0.264` n `102`; fx avg `-0.008` n `6`; index avg `-0.0752` n `25`; metal avg `-0.0096` n `20`; unknown avg `0.8688` n `776`
- 4h: commodity avg `0.1704` n `12`; crypto_alt avg `-0.2298` n `230`; crypto_major avg `0.0283` n `8`; equity avg `0.5189` n `102`; fx avg `-0.0016` n `6`; index avg `-0.1156` n `25`; metal avg `-0.1784` n `20`; unknown avg `0.7054` n `774`
- 24h: commodity avg `-0.8804` n `12`; crypto_alt avg `-1.9414` n `230`; crypto_major avg `-1.5588` n `8`; equity avg `-2.7997` n `102`; fx avg `-0.0942` n `6`; index avg `-0.425` n `25`; metal avg `-0.43` n `20`; unknown avg `1.0809` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
