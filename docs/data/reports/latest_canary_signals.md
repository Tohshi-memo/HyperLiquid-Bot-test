# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T15:52:45.898979+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.1` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7145` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6983` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.5676` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.2085` n `12`; crypto_alt avg `0.7193` n `228`; crypto_major avg `0.8255` n `8`; equity avg `0.7424` n `74`; fx avg `0.0001` n `6`; index avg `0.1338` n `23`; metal avg `-0.0187` n `18`; unknown avg `0.5151` n `690`
- 1h: commodity avg `-0.0312` n `12`; crypto_alt avg `0.5298` n `228`; crypto_major avg `1.0715` n `8`; equity avg `-0.4961` n `74`; fx avg `0.0053` n `6`; index avg `0.3618` n `23`; metal avg `-0.0332` n `18`; unknown avg `0.4193` n `690`
- 4h: commodity avg `0.2727` n `12`; crypto_alt avg `1.1985` n `228`; crypto_major avg `1.8079` n `8`; equity avg `0.0934` n `74`; fx avg `-0.0209` n `6`; index avg `0.4183` n `23`; metal avg `0.1096` n `18`; unknown avg `1.0417` n `689`
- 24h: commodity avg `-1.1734` n `12`; crypto_alt avg `6.722` n `228`; crypto_major avg `7.5808` n `8`; equity avg `1.8756` n `74`; fx avg `0.0516` n `6`; index avg `1.2951` n `23`; metal avg `2.8389` n `18`; unknown avg `2.6082` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
