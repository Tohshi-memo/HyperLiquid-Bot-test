# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T14:52:38.729919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.73` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.5815` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0346` n `12`; crypto_alt avg `0.0488` n `230`; crypto_major avg `0.1691` n `8`; equity avg `-0.065` n `102`; fx avg `-0.0228` n `6`; index avg `-0.0786` n `25`; metal avg `-0.0533` n `20`; unknown avg `-0.004` n `778`
- 1h: commodity avg `0.1109` n `12`; crypto_alt avg `-0.2649` n `230`; crypto_major avg `-0.1641` n `8`; equity avg `-0.7554` n `102`; fx avg `-0.0023` n `6`; index avg `-0.1722` n `25`; metal avg `-0.0625` n `20`; unknown avg `-0.0226` n `777`
- 4h: commodity avg `0.4587` n `12`; crypto_alt avg `-0.3996` n `230`; crypto_major avg `-0.3333` n `8`; equity avg `-1.9148` n `102`; fx avg `0.0055` n `6`; index avg `-0.2993` n `25`; metal avg `-0.1765` n `20`; unknown avg `0.4858` n `777`
- 24h: commodity avg `0.7919` n `12`; crypto_alt avg `-1.7207` n `230`; crypto_major avg `0.4901` n `8`; equity avg `-1.1252` n `102`; fx avg `-0.0355` n `6`; index avg `-0.3833` n `25`; metal avg `-0.2363` n `20`; unknown avg `-0.1547` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
