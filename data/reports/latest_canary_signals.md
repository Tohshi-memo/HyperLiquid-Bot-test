# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T06:37:29.475205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0201` n `12`; crypto_alt avg `0.0839` n `230`; crypto_major avg `0.0337` n `8`; equity avg `-0.0501` n `102`; fx avg `-0.0163` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0013` n `779`
- 1h: commodity avg `0.0791` n `12`; crypto_alt avg `0.0707` n `230`; crypto_major avg `-0.067` n `8`; equity avg `0.1629` n `102`; fx avg `-0.0349` n `6`; index avg `-0.0279` n `25`; metal avg `-0.022` n `20`; unknown avg `0.0341` n `747`
- 4h: commodity avg `0.4332` n `12`; crypto_alt avg `-0.1185` n `230`; crypto_major avg `-0.359` n `8`; equity avg `-0.5213` n `102`; fx avg `-0.0944` n `6`; index avg `-0.1727` n `25`; metal avg `-0.3231` n `20`; unknown avg `0.087` n `747`
- 24h: commodity avg `0.9168` n `12`; crypto_alt avg `-0.4805` n `230`; crypto_major avg `-0.9441` n `8`; equity avg `-2.7749` n `102`; fx avg `0.0036` n `6`; index avg `-0.3451` n `25`; metal avg `-0.181` n `20`; unknown avg `-0.5982` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
