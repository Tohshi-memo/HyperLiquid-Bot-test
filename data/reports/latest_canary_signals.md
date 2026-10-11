# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T07:22:26.708781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `13`; crypto_alt avg `-0.1764` n `235`; crypto_major avg `-0.1617` n `8`; equity avg `-0.0273` n `150`; fx avg `0.003` n `6`; index avg `-0.0008` n `26`; metal avg `0.0005` n `20`; unknown avg `0.0243` n `1117`
- 1h: commodity avg `0.0054` n `13`; crypto_alt avg `0.246` n `235`; crypto_major avg `-0.0292` n `8`; equity avg `0.0187` n `150`; fx avg `0.0036` n `6`; index avg `0.0068` n `26`; metal avg `0.0132` n `20`; unknown avg `0.1117` n `1115`
- 4h: commodity avg `-0.0157` n `13`; crypto_alt avg `0.5879` n `235`; crypto_major avg `-0.1279` n `8`; equity avg `-0.0253` n `150`; fx avg `-0.0004` n `6`; index avg `-0.0009` n `26`; metal avg `0.0066` n `20`; unknown avg `0.169` n `1093`
- 24h: commodity avg `0.1537` n `13`; crypto_alt avg `1.0616` n `235`; crypto_major avg `-0.1242` n `8`; equity avg `0.0228` n `150`; fx avg `-0.0021` n `6`; index avg `-0.0134` n `26`; metal avg `0.0048` n `20`; unknown avg `0.4121` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
