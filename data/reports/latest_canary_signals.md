# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T17:52:28.487699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `13`; crypto_alt avg `-0.2425` n `239`; crypto_major avg `-0.2589` n `8`; equity avg `-0.0445` n `168`; fx avg `-0.0009` n `6`; index avg `-0.0005` n `27`; metal avg `-0.0126` n `20`; unknown avg `333.1124` n `1268`
- 1h: commodity avg `-0.0187` n `13`; crypto_alt avg `-0.2407` n `239`; crypto_major avg `-0.318` n `8`; equity avg `-0.0619` n `168`; fx avg `-0.0076` n `6`; index avg `-0.0091` n `27`; metal avg `-0.0197` n `20`; unknown avg `50.6478` n `1239`
- 4h: commodity avg `-0.0624` n `13`; crypto_alt avg `-0.7447` n `239`; crypto_major avg `0.1386` n `8`; equity avg `0.0306` n `168`; fx avg `0.0033` n `6`; index avg `0.001` n `27`; metal avg `-0.0021` n `20`; unknown avg `40.7349` n `1219`
- 24h: commodity avg `-0.0655` n `13`; crypto_alt avg `-2.9423` n `239`; crypto_major avg `-0.9565` n `8`; equity avg `0.4059` n `168`; fx avg `-0.0124` n `6`; index avg `0.0349` n `27`; metal avg `0.269` n `20`; unknown avg `192.489` n `1072`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
