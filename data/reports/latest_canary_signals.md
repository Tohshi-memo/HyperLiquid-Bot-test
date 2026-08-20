# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T06:37:29.466065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `12`; crypto_alt avg `0.1254` n `230`; crypto_major avg `0.2394` n `8`; equity avg `0.0786` n `121`; fx avg `-0.005` n `6`; index avg `0.012` n `25`; metal avg `-0.008` n `20`; unknown avg `0.104` n `792`
- 1h: commodity avg `0.0039` n `12`; crypto_alt avg `0.2592` n `230`; crypto_major avg `0.4083` n `8`; equity avg `0.1282` n `121`; fx avg `-0.0547` n `6`; index avg `0.0298` n `25`; metal avg `0.099` n `20`; unknown avg `5.6611` n `776`
- 4h: commodity avg `0.0445` n `12`; crypto_alt avg `0.3078` n `230`; crypto_major avg `0.5416` n `8`; equity avg `0.133` n `121`; fx avg `0.0034` n `6`; index avg `0.0127` n `25`; metal avg `0.0251` n `20`; unknown avg `0.13` n `776`
- 24h: commodity avg `-0.0673` n `12`; crypto_alt avg `5.791` n `230`; crypto_major avg `10.5013` n `8`; equity avg `1.867` n `120`; fx avg `0.0523` n `6`; index avg `0.3774` n `25`; metal avg `1.0695` n `20`; unknown avg `1.8734` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
