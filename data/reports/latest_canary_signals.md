# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T13:16:11.165254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `0.0347` n `230`; crypto_major avg `0.1576` n `8`; equity avg `0.0626` n `120`; fx avg `0.0079` n `6`; index avg `0.015` n `25`; metal avg `0.2069` n `20`; unknown avg `0.0868` n `792`
- 1h: commodity avg `-0.031` n `12`; crypto_alt avg `0.1672` n `230`; crypto_major avg `0.6455` n `8`; equity avg `1.1942` n `120`; fx avg `0.0174` n `6`; index avg `0.165` n `25`; metal avg `0.5174` n `20`; unknown avg `0.1161` n `792`
- 4h: commodity avg `-0.0076` n `12`; crypto_alt avg `0.4414` n `230`; crypto_major avg `0.7835` n `8`; equity avg `0.7838` n `120`; fx avg `-0.0471` n `6`; index avg `0.1538` n `25`; metal avg `0.6775` n `20`; unknown avg `0.3121` n `791`
- 24h: commodity avg `0.2981` n `12`; crypto_alt avg `0.5883` n `230`; crypto_major avg `1.2535` n `8`; equity avg `-0.5116` n `120`; fx avg `-0.2075` n `6`; index avg `-0.0129` n `25`; metal avg `0.2578` n `20`; unknown avg `0.0332` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
