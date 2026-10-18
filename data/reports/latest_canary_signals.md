# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T09:52:32.898727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0775` n `13`; crypto_alt avg `0.1479` n `237`; crypto_major avg `0.0823` n `8`; equity avg `-0.0164` n `151`; fx avg `0.0028` n `6`; index avg `0.0095` n `26`; metal avg `0.0068` n `20`; unknown avg `0.3358` n `1193`
- 1h: commodity avg `0.0678` n `13`; crypto_alt avg `0.8166` n `237`; crypto_major avg `0.6489` n `8`; equity avg `0.1772` n `151`; fx avg `0.0013` n `6`; index avg `0.0306` n `26`; metal avg `0.0245` n `20`; unknown avg `0.704` n `1135`
- 4h: commodity avg `0.0825` n `13`; crypto_alt avg `0.8027` n `237`; crypto_major avg `0.6316` n `8`; equity avg `0.4027` n `151`; fx avg `0.0024` n `6`; index avg `0.0775` n `26`; metal avg `0.0183` n `20`; unknown avg `1.2473` n `1063`
- 24h: commodity avg `0.1147` n `13`; crypto_alt avg `-1.9942` n `236`; crypto_major avg `-0.3655` n `8`; equity avg `-0.5984` n `151`; fx avg `-0.0318` n `6`; index avg `-0.0692` n `26`; metal avg `-0.0397` n `20`; unknown avg `4.3397` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1931`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1339`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1246`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0815`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
