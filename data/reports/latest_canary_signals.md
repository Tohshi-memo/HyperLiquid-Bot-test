# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T22:52:23.221804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `13`; crypto_alt avg `0.0297` n `235`; crypto_major avg `0.0012` n `8`; equity avg `-0.0038` n `150`; fx avg `0.0` n `6`; index avg `0.0001` n `26`; metal avg `0.0038` n `20`; unknown avg `0.0291` n `1116`
- 1h: commodity avg `-0.0297` n `13`; crypto_alt avg `0.2387` n `235`; crypto_major avg `0.1799` n `8`; equity avg `0.0114` n `150`; fx avg `-0.0036` n `6`; index avg `-0.0108` n `26`; metal avg `-0.011` n `20`; unknown avg `0.0886` n `1114`
- 4h: commodity avg `-0.0597` n `13`; crypto_alt avg `0.6743` n `235`; crypto_major avg `0.1978` n `8`; equity avg `-0.0279` n `150`; fx avg `-0.0038` n `6`; index avg `-0.0198` n `26`; metal avg `-0.0548` n `20`; unknown avg `0.2534` n `1026`
- 24h: commodity avg `-0.1384` n `13`; crypto_alt avg `1.951` n `235`; crypto_major avg `0.4314` n `8`; equity avg `0.7559` n `150`; fx avg `0.0088` n `6`; index avg `0.1166` n `26`; metal avg `0.544` n `20`; unknown avg `12.8494` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
