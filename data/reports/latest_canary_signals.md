# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T11:52:27.546992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0665` n `13`; crypto_alt avg `0.0796` n `235`; crypto_major avg `0.1234` n `8`; equity avg `0.0408` n `150`; fx avg `-0.005` n `6`; index avg `0.0009` n `26`; metal avg `-0.0041` n `20`; unknown avg `1.3149` n `1117`
- 1h: commodity avg `-0.0716` n `13`; crypto_alt avg `0.2438` n `235`; crypto_major avg `0.2535` n `8`; equity avg `0.0591` n `150`; fx avg `0.0175` n `6`; index avg `-0.0041` n `26`; metal avg `0.0031` n `20`; unknown avg `0.6345` n `1115`
- 4h: commodity avg `-0.0566` n `13`; crypto_alt avg `-0.1665` n `235`; crypto_major avg `0.2199` n `8`; equity avg `0.08` n `150`; fx avg `0.0228` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0114` n `20`; unknown avg `0.0054` n `1099`
- 24h: commodity avg `0.3613` n `13`; crypto_alt avg `1.0545` n `235`; crypto_major avg `0.0644` n `8`; equity avg `0.1125` n `150`; fx avg `0.0189` n `6`; index avg `-0.0064` n `26`; metal avg `0.0045` n `20`; unknown avg `0.6558` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
