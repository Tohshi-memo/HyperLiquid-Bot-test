# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T06:52:24.972445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.0974` n `230`; crypto_major avg `-0.1327` n `8`; equity avg `0.0592` n `92`; fx avg `-0.0083` n `6`; index avg `0.0068` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0074` n `765`
- 1h: commodity avg `0.0417` n `12`; crypto_alt avg `0.0847` n `230`; crypto_major avg `0.0103` n `8`; equity avg `0.1011` n `92`; fx avg `-0.012` n `6`; index avg `0.0091` n `25`; metal avg `-0.0051` n `20`; unknown avg `-0.0105` n `733`
- 4h: commodity avg `0.0246` n `12`; crypto_alt avg `-0.1991` n `229`; crypto_major avg `-0.0154` n `8`; equity avg `0.08` n `92`; fx avg `0.0203` n `6`; index avg `0.0074` n `25`; metal avg `0.0087` n `20`; unknown avg `-0.0201` n `731`
- 24h: commodity avg `-0.3161` n `12`; crypto_alt avg `0.4908` n `229`; crypto_major avg `-0.1103` n `8`; equity avg `-0.1259` n `92`; fx avg `-0.0593` n `6`; index avg `0.1488` n `25`; metal avg `0.0238` n `20`; unknown avg `2.902` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
