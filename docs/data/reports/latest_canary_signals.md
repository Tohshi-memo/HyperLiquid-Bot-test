# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T22:14:43.265152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1567` n `12`; crypto_alt avg `-0.0874` n `230`; crypto_major avg `-0.0572` n `8`; equity avg `-0.012` n `102`; fx avg `-0.0038` n `6`; index avg `0.0181` n `25`; metal avg `-0.0414` n `20`; unknown avg `-0.016` n `776`
- 1h: commodity avg `0.3341` n `12`; crypto_alt avg `0.074` n `230`; crypto_major avg `0.1841` n `8`; equity avg `0.0472` n `102`; fx avg `0.0132` n `6`; index avg `0.0637` n `25`; metal avg `-0.021` n `20`; unknown avg `-0.1174` n `776`
- 4h: commodity avg `0.3551` n `12`; crypto_alt avg `0.2043` n `230`; crypto_major avg `0.5304` n `8`; equity avg `1.0685` n `102`; fx avg `0.0174` n `6`; index avg `0.0697` n `25`; metal avg `-0.0245` n `20`; unknown avg `0.326` n `775`
- 24h: commodity avg `-0.4938` n `12`; crypto_alt avg `-1.5898` n `230`; crypto_major avg `-0.9695` n `8`; equity avg `-2.5531` n `102`; fx avg `-0.0814` n `6`; index avg `-0.3186` n `25`; metal avg `-0.4526` n `20`; unknown avg `0.2024` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
