# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T18:22:29.417059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0753` n `13`; crypto_alt avg `0.0643` n `236`; crypto_major avg `-0.0172` n `8`; equity avg `0.0773` n `151`; fx avg `0.0049` n `6`; index avg `0.0237` n `26`; metal avg `0.0333` n `20`; unknown avg `4.6384` n `1134`
- 1h: commodity avg `0.0252` n `13`; crypto_alt avg `-0.3405` n `236`; crypto_major avg `-0.4001` n `8`; equity avg `-0.3158` n `151`; fx avg `-0.0138` n `6`; index avg `-0.0295` n `26`; metal avg `0.0016` n `20`; unknown avg `4.2141` n `1132`
- 4h: commodity avg `0.1057` n `13`; crypto_alt avg `0.204` n `236`; crypto_major avg `-0.285` n `8`; equity avg `-1.4316` n `151`; fx avg `-0.0015` n `6`; index avg `-0.2262` n `26`; metal avg `-0.1913` n `20`; unknown avg `4.1403` n `1101`
- 24h: commodity avg `-0.0113` n `13`; crypto_alt avg `-2.2311` n `236`; crypto_major avg `-2.0781` n `8`; equity avg `-3.7351` n `151`; fx avg `-0.162` n `6`; index avg `-0.5115` n `26`; metal avg `-0.8529` n `20`; unknown avg `1269.558` n `978`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0806`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0638`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0607`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0557`, n `666`, weak_sample_signal
