# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T07:37:31.343539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0531` n `12`; crypto_alt avg `0.0773` n `229`; crypto_major avg `0.2147` n `8`; equity avg `0.2627` n `91`; fx avg `0.0058` n `6`; index avg `0.0429` n `25`; metal avg `0.0452` n `20`; unknown avg `0.026` n `763`
- 1h: commodity avg `-0.1177` n `12`; crypto_alt avg `0.3076` n `229`; crypto_major avg `0.3502` n `8`; equity avg `0.1548` n `91`; fx avg `0.0384` n `6`; index avg `0.0206` n `25`; metal avg `-0.1646` n `20`; unknown avg `0.0526` n `763`
- 4h: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.2534` n `229`; crypto_major avg `-0.4023` n `8`; equity avg `-0.7332` n `91`; fx avg `-0.0563` n `6`; index avg `-0.2807` n `25`; metal avg `-0.1388` n `20`; unknown avg `-0.2287` n `743`
- 24h: commodity avg `0.6693` n `12`; crypto_alt avg `-2.589` n `229`; crypto_major avg `-2.1989` n `8`; equity avg `-1.6542` n `91`; fx avg `-0.2401` n `6`; index avg `-0.3737` n `25`; metal avg `-0.1337` n `20`; unknown avg `-0.5846` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
