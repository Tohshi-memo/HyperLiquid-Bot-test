# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T23:37:30.875546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0063` n `13`; crypto_alt avg `-0.0188` n `235`; crypto_major avg `-0.1034` n `8`; equity avg `0.0209` n `144`; fx avg `0.0015` n `6`; index avg `0.0045` n `26`; metal avg `0.0104` n `20`; unknown avg `2.7978` n `1078`
- 1h: commodity avg `-0.0361` n `13`; crypto_alt avg `0.1372` n `235`; crypto_major avg `-0.1148` n `8`; equity avg `0.0857` n `144`; fx avg `-0.0175` n `6`; index avg `-0.0014` n `26`; metal avg `-0.005` n `20`; unknown avg `-0.2619` n `1076`
- 4h: commodity avg `-0.1868` n `13`; crypto_alt avg `0.2359` n `235`; crypto_major avg `0.5083` n `8`; equity avg `0.2843` n `144`; fx avg `-0.0098` n `6`; index avg `0.0321` n `26`; metal avg `0.0766` n `20`; unknown avg `4.1907` n `1012`
- 24h: commodity avg `-0.235` n `13`; crypto_alt avg `0.912` n `235`; crypto_major avg `1.6379` n `8`; equity avg `0.3788` n `144`; fx avg `0.0007` n `6`; index avg `0.0102` n `26`; metal avg `0.0869` n `20`; unknown avg `0.3187` n `976`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.2091`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2069`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
