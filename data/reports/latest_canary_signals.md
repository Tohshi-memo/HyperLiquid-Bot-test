# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T07:22:23.435151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `13`; crypto_alt avg `-0.2376` n `239`; crypto_major avg `-0.4278` n `8`; equity avg `-0.4753` n `168`; fx avg `-0.0125` n `6`; index avg `-0.064` n `27`; metal avg `-0.1078` n `20`; unknown avg `6.5319` n `1263`
- 1h: commodity avg `-0.1738` n `13`; crypto_alt avg `-0.2658` n `239`; crypto_major avg `-0.0951` n `8`; equity avg `-0.6926` n `168`; fx avg `-0.04` n `6`; index avg `-0.0941` n `27`; metal avg `-0.0972` n `20`; unknown avg `-0.0082` n `1255`
- 4h: commodity avg `-0.1056` n `13`; crypto_alt avg `0.3822` n `239`; crypto_major avg `-0.5589` n `8`; equity avg `-1.2419` n `168`; fx avg `-0.0836` n `6`; index avg `-0.1152` n `27`; metal avg `-0.3913` n `20`; unknown avg `206.4662` n `1219`
- 24h: commodity avg `0.2212` n `13`; crypto_alt avg `-3.0083` n `239`; crypto_major avg `-3.0577` n `8`; equity avg `-5.8954` n `167`; fx avg `0.0703` n `6`; index avg `-0.5876` n `27`; metal avg `-1.1129` n `20`; unknown avg `638.6208` n `1029`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
