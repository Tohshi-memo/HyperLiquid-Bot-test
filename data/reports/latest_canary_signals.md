# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T02:07:34.464285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2024` n `12`; crypto_alt avg `0.2468` n `228`; crypto_major avg `0.1846` n `8`; equity avg `0.0619` n `74`; fx avg `0.0044` n `6`; index avg `0.107` n `23`; metal avg `0.0866` n `18`; unknown avg `-0.0571` n `557`
- 1h: commodity avg `-0.0484` n `12`; crypto_alt avg `0.0919` n `228`; crypto_major avg `-0.0976` n `8`; equity avg `-0.1133` n `74`; fx avg `0.0328` n `6`; index avg `0.026` n `23`; metal avg `0.307` n `18`; unknown avg `0.0036` n `556`
- 4h: commodity avg `0.277` n `12`; crypto_alt avg `-0.1574` n `228`; crypto_major avg `-0.3771` n `8`; equity avg `0.2936` n `74`; fx avg `0.0294` n `6`; index avg `0.1057` n `23`; metal avg `-0.434` n `18`; unknown avg `-0.096` n `556`
- 24h: commodity avg `-2.3883` n `12`; crypto_alt avg `2.7716` n `228`; crypto_major avg `2.64` n `8`; equity avg `3.8785` n `74`; fx avg `-0.0332` n `6`; index avg `2.1833` n `23`; metal avg `2.8482` n `18`; unknown avg `2.3038` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
