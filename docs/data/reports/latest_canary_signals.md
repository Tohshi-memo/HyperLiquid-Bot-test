# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T09:07:27.494555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `13`; crypto_alt avg `0.1441` n `238`; crypto_major avg `0.1957` n `8`; equity avg `0.0373` n `156`; fx avg `-0.0072` n `6`; index avg `-0.0016` n `27`; metal avg `0.0096` n `20`; unknown avg `-0.0406` n `1256`
- 1h: commodity avg `0.0464` n `13`; crypto_alt avg `0.1982` n `238`; crypto_major avg `0.04` n `8`; equity avg `0.0217` n `156`; fx avg `0.0025` n `6`; index avg `-0.0001` n `27`; metal avg `0.0104` n `20`; unknown avg `0.0857` n `1256`
- 4h: commodity avg `0.0086` n `13`; crypto_alt avg `-0.1755` n `238`; crypto_major avg `-0.2196` n `8`; equity avg `-0.0274` n `156`; fx avg `0.0164` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0009` n `20`; unknown avg `0.6241` n `1212`
- 24h: commodity avg `-0.1367` n `13`; crypto_alt avg `0.8552` n `238`; crypto_major avg `-0.896` n `8`; equity avg `-2.2187` n `156`; fx avg `-0.09` n `6`; index avg `-0.2441` n `27`; metal avg `-0.5041` n `20`; unknown avg `4.4642` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
