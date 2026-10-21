# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T07:37:32.537477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `0.1693` n `237`; crypto_major avg `0.1982` n `8`; equity avg `0.1193` n `151`; fx avg `-0.0097` n `6`; index avg `0.0327` n `26`; metal avg `0.0243` n `20`; unknown avg `0.8797` n `1200`
- 1h: commodity avg `-0.0917` n `13`; crypto_alt avg `0.4537` n `237`; crypto_major avg `0.3065` n `8`; equity avg `0.0407` n `151`; fx avg `-0.0078` n `6`; index avg `0.0264` n `26`; metal avg `0.0447` n `20`; unknown avg `3.0051` n `1194`
- 4h: commodity avg `-0.149` n `13`; crypto_alt avg `0.4832` n `237`; crypto_major avg `0.3032` n `8`; equity avg `-0.0783` n `151`; fx avg `-0.0322` n `6`; index avg `-0.0065` n `26`; metal avg `-0.0824` n `20`; unknown avg `1.7557` n `1168`
- 24h: commodity avg `-0.2202` n `13`; crypto_alt avg `3.4598` n `237`; crypto_major avg `2.478` n `8`; equity avg `2.6957` n `151`; fx avg `-0.0021` n `6`; index avg `0.3664` n `26`; metal avg `-0.159` n `20`; unknown avg `5293.0981` n `986`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
