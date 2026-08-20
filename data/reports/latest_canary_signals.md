# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T05:07:26.793657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `12`; crypto_alt avg `0.0392` n `230`; crypto_major avg `0.1397` n `8`; equity avg `-0.0962` n `121`; fx avg `-0.0014` n `6`; index avg `-0.035` n `25`; metal avg `0.0144` n `20`; unknown avg `0.0497` n `792`
- 1h: commodity avg `-0.0124` n `12`; crypto_alt avg `0.2582` n `230`; crypto_major avg `0.3658` n `8`; equity avg `-0.1553` n `121`; fx avg `0.0074` n `6`; index avg `-0.0429` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.2445` n `792`
- 4h: commodity avg `-0.0129` n `12`; crypto_alt avg `0.128` n `230`; crypto_major avg `0.2876` n `8`; equity avg `-0.2904` n `121`; fx avg `0.0297` n `6`; index avg `-0.0275` n `25`; metal avg `0.0866` n `20`; unknown avg `-0.0368` n `792`
- 24h: commodity avg `-0.0441` n `12`; crypto_alt avg `5.5119` n `230`; crypto_major avg `9.8938` n `8`; equity avg `1.2904` n `120`; fx avg `0.0736` n `6`; index avg `0.3017` n `25`; metal avg `1.1582` n `20`; unknown avg `1.7334` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
