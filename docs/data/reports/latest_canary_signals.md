# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T02:04:52.700938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `0.0078` n `230`; crypto_major avg `0.0151` n `8`; equity avg `0.0482` n `121`; fx avg `0.01` n `6`; index avg `0.0006` n `25`; metal avg `0.1109` n `20`; unknown avg `-0.0065` n `792`
- 1h: commodity avg `0.0202` n `12`; crypto_alt avg `0.3601` n `230`; crypto_major avg `0.3919` n `8`; equity avg `-0.1061` n `121`; fx avg `0.0274` n `6`; index avg `0.0228` n `25`; metal avg `0.0938` n `20`; unknown avg `-0.0004` n `792`
- 4h: commodity avg `0.1091` n `12`; crypto_alt avg `0.2464` n `230`; crypto_major avg `-0.7509` n `8`; equity avg `0.4756` n `121`; fx avg `0.1333` n `6`; index avg `0.1455` n `25`; metal avg `-0.1247` n `20`; unknown avg `-0.076` n `792`
- 24h: commodity avg `-0.0892` n `12`; crypto_alt avg `5.6944` n `230`; crypto_major avg `10.094` n `8`; equity avg `0.9217` n `120`; fx avg `-0.0098` n `6`; index avg `0.3069` n `25`; metal avg `1.0622` n `20`; unknown avg `1.5864` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
