# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T08:57:12.513184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `13`; crypto_alt avg `0.1039` n `235`; crypto_major avg `0.0143` n `8`; equity avg `0.0078` n `150`; fx avg `-0.0176` n `6`; index avg `0.0074` n `26`; metal avg `0.0087` n `20`; unknown avg `0.0562` n `1117`
- 1h: commodity avg `-0.0174` n `13`; crypto_alt avg `0.224` n `235`; crypto_major avg `0.0896` n `8`; equity avg `0.0144` n `150`; fx avg `-0.0122` n `6`; index avg `0.002` n `26`; metal avg `0.0047` n `20`; unknown avg `0.5245` n `1099`
- 4h: commodity avg `0.0032` n `13`; crypto_alt avg `-0.1068` n `235`; crypto_major avg `0.1602` n `8`; equity avg `-0.086` n `150`; fx avg `-0.0112` n `6`; index avg `-0.0321` n `26`; metal avg `0.0007` n `20`; unknown avg `0.8145` n `1082`
- 24h: commodity avg `0.1544` n `13`; crypto_alt avg `1.2636` n `235`; crypto_major avg `0.0534` n `8`; equity avg `-0.3535` n `150`; fx avg `-0.0496` n `6`; index avg `-0.0637` n `26`; metal avg `0.0644` n `20`; unknown avg `632.7752` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
