# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T06:22:34.460341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0659` n `12`; crypto_alt avg `-0.058` n `228`; crypto_major avg `0.1806` n `8`; equity avg `0.0202` n `86`; fx avg `0.0161` n `6`; index avg `0.0148` n `23`; metal avg `-0.0601` n `20`; unknown avg `-0.0022` n `765`
- 1h: commodity avg `0.0504` n `12`; crypto_alt avg `-0.0304` n `228`; crypto_major avg `0.3213` n `8`; equity avg `0.0111` n `86`; fx avg `-0.0067` n `6`; index avg `0.0322` n `23`; metal avg `-0.1762` n `20`; unknown avg `20.0496` n `749`
- 4h: commodity avg `0.0835` n `12`; crypto_alt avg `0.9652` n `228`; crypto_major avg `1.1873` n `8`; equity avg `0.4948` n `86`; fx avg `-0.0252` n `6`; index avg `0.1134` n `23`; metal avg `-0.0763` n `20`; unknown avg `-0.0888` n `748`
- 24h: commodity avg `-0.4516` n `12`; crypto_alt avg `-1.0785` n `228`; crypto_major avg `-0.8632` n `8`; equity avg `-0.0883` n `86`; fx avg `-0.0014` n `6`; index avg `0.5591` n `23`; metal avg `-1.9051` n `20`; unknown avg `-0.5512` n `708`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
