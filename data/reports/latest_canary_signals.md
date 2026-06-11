# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T15:37:30.373268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1585` n `12`; crypto_alt avg `0.1221` n `228`; crypto_major avg `0.1728` n `8`; equity avg `0.2013` n `74`; fx avg `-0.0099` n `6`; index avg `0.0605` n `23`; metal avg `-0.0155` n `18`; unknown avg `0.0307` n `556`
- 1h: commodity avg `-0.025` n `12`; crypto_alt avg `0.0047` n `228`; crypto_major avg `0.0592` n `8`; equity avg `0.0975` n `74`; fx avg `-0.0164` n `6`; index avg `0.0478` n `23`; metal avg `-0.0681` n `18`; unknown avg `0.4794` n `556`
- 4h: commodity avg `0.4083` n `12`; crypto_alt avg `0.1031` n `228`; crypto_major avg `-0.0751` n `8`; equity avg `-0.0301` n `74`; fx avg `-0.0818` n `6`; index avg `0.0907` n `23`; metal avg `0.2745` n `18`; unknown avg `0.7132` n `556`
- 24h: commodity avg `-0.2172` n `12`; crypto_alt avg `0.2648` n `228`; crypto_major avg `0.08` n `8`; equity avg `0.2055` n `74`; fx avg `-0.0469` n `6`; index avg `0.2583` n `23`; metal avg `-0.5685` n `18`; unknown avg `3.0237` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
