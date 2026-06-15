# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T14:07:37.134866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.22` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7156` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0211` n `12`; crypto_alt avg `-0.2893` n `228`; crypto_major avg `-0.3218` n `8`; equity avg `-0.2951` n `74`; fx avg `0.0057` n `6`; index avg `-0.2092` n `23`; metal avg `0.2016` n `18`; unknown avg `0.0781` n `690`
- 1h: commodity avg `0.1229` n `12`; crypto_alt avg `0.0738` n `228`; crypto_major avg `-0.0877` n `8`; equity avg `0.4387` n `74`; fx avg `0.0182` n `6`; index avg `0.1902` n `23`; metal avg `0.3891` n `18`; unknown avg `0.4588` n `689`
- 4h: commodity avg `0.4371` n `12`; crypto_alt avg `1.7618` n `228`; crypto_major avg `2.0898` n `8`; equity avg `0.3742` n `74`; fx avg `0.0074` n `6`; index avg `0.2978` n `23`; metal avg `0.769` n `18`; unknown avg `0.4857` n `689`
- 24h: commodity avg `-1.2099` n `12`; crypto_alt avg `5.5365` n `228`; crypto_major avg `5.6499` n `8`; equity avg `2.0601` n `74`; fx avg `0.0509` n `6`; index avg `1.1573` n `23`; metal avg `3.187` n `18`; unknown avg `1.9108` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
