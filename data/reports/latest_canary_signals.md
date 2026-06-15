# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T14:52:40.721969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.13` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.8561` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0261` n `12`; crypto_alt avg `-0.0483` n `228`; crypto_major avg `0.2857` n `8`; equity avg `0.1892` n `74`; fx avg `-0.0045` n `6`; index avg `-0.0295` n `23`; metal avg `-0.0395` n `18`; unknown avg `0.3382` n `690`
- 1h: commodity avg `0.0953` n `12`; crypto_alt avg `-0.1173` n `228`; crypto_major avg `0.0207` n `8`; equity avg `0.0144` n `74`; fx avg `-0.023` n `6`; index avg `-0.3346` n `23`; metal avg `-0.1629` n `18`; unknown avg `0.6709` n `690`
- 4h: commodity avg `0.303` n `12`; crypto_alt avg `1.8399` n `228`; crypto_major avg `2.1589` n `8`; equity avg `0.7067` n `74`; fx avg `-0.0209` n `6`; index avg `0.1364` n `23`; metal avg `0.3028` n `18`; unknown avg `0.6232` n `689`
- 24h: commodity avg `-1.0122` n `12`; crypto_alt avg `6.6365` n `228`; crypto_major avg `6.8557` n `8`; equity avg `2.624` n `74`; fx avg `0.026` n `6`; index avg `1.0859` n `23`; metal avg `2.8436` n `18`; unknown avg `2.7057` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
