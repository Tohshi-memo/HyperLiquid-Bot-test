# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T11:07:27.860556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.4346` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7263` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `-0.0847` n `230`; crypto_major avg `-0.1285` n `8`; equity avg `-0.2643` n `121`; fx avg `0.0017` n `6`; index avg `-0.0535` n `25`; metal avg `-0.0118` n `20`; unknown avg `0.0229` n `792`
- 1h: commodity avg `0.0354` n `12`; crypto_alt avg `0.2435` n `230`; crypto_major avg `-0.0668` n `8`; equity avg `-0.2082` n `121`; fx avg `0.0158` n `6`; index avg `-0.0186` n `25`; metal avg `0.0424` n `20`; unknown avg `0.0982` n `792`
- 4h: commodity avg `0.2754` n `12`; crypto_alt avg `1.792` n `230`; crypto_major avg `1.7799` n `8`; equity avg `-0.6547` n `121`; fx avg `0.0783` n `6`; index avg `-0.1098` n `25`; metal avg `0.0536` n `20`; unknown avg `0.1963` n `792`
- 24h: commodity avg `0.2267` n `12`; crypto_alt avg `7.4572` n `230`; crypto_major avg `12.1681` n `8`; equity avg `0.1602` n `120`; fx avg `0.2191` n `6`; index avg `0.065` n `25`; metal avg `0.9078` n `20`; unknown avg `2.1576` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
