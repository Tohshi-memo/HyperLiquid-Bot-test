# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T01:52:32.836025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.34` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.007` n `13`; crypto_alt avg `0.1422` n `235`; crypto_major avg `0.0541` n `8`; equity avg `0.0175` n `144`; fx avg `0.0177` n `6`; index avg `-0.0048` n `26`; metal avg `0.0472` n `20`; unknown avg `-0.1027` n `1074`
- 1h: commodity avg `-0.0694` n `13`; crypto_alt avg `-0.0418` n `235`; crypto_major avg `-0.0176` n `8`; equity avg `0.1447` n `144`; fx avg `-0.069` n `6`; index avg `0.0241` n `26`; metal avg `0.0519` n `20`; unknown avg `0.0362` n `1068`
- 4h: commodity avg `-0.2236` n `13`; crypto_alt avg `0.5151` n `235`; crypto_major avg `0.1697` n `8`; equity avg `0.4836` n `144`; fx avg `-0.0723` n `6`; index avg `0.0589` n `26`; metal avg `0.2552` n `20`; unknown avg `2.4235` n `1036`
- 24h: commodity avg `-0.3439` n `13`; crypto_alt avg `1.3662` n `235`; crypto_major avg `1.6032` n `8`; equity avg `0.7033` n `144`; fx avg `-0.0479` n `6`; index avg `0.0576` n `26`; metal avg `0.2434` n `20`; unknown avg `0.6865` n `950`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
