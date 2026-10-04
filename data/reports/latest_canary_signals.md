# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T04:22:25.989970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `13`; crypto_alt avg `0.2702` n `235`; crypto_major avg `-0.0138` n `8`; equity avg `-0.0087` n `143`; fx avg `-0.0021` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0048` n `20`; unknown avg `0.093` n `1079`
- 1h: commodity avg `-0.02` n `13`; crypto_alt avg `0.2847` n `235`; crypto_major avg `0.0592` n `8`; equity avg `0.0164` n `143`; fx avg `0.0015` n `6`; index avg `-0.003` n `26`; metal avg `-0.0046` n `20`; unknown avg `-0.0898` n `1071`
- 4h: commodity avg `-0.0235` n `13`; crypto_alt avg `0.1477` n `235`; crypto_major avg `0.0155` n `8`; equity avg `-0.0013` n `143`; fx avg `-0.0042` n `6`; index avg `-0.0093` n `26`; metal avg `0.0063` n `20`; unknown avg `-0.249` n `1071`
- 24h: commodity avg `0.1014` n `13`; crypto_alt avg `1.8484` n `235`; crypto_major avg `0.8421` n `8`; equity avg `0.2445` n `143`; fx avg `-0.0318` n `6`; index avg `0.0101` n `26`; metal avg `0.0065` n `20`; unknown avg `0.1821` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2006`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
