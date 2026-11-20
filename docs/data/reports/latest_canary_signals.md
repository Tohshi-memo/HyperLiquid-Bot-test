# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T02:52:26.710853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `13`; crypto_alt avg `0.2257` n `239`; crypto_major avg `0.2326` n `8`; equity avg `-0.0632` n `165`; fx avg `0.0015` n `6`; index avg `-0.0221` n `27`; metal avg `0.0755` n `20`; unknown avg `146.1916` n `1262`
- 1h: commodity avg `0.0157` n `13`; crypto_alt avg `-0.6136` n `239`; crypto_major avg `-0.3866` n `8`; equity avg `-0.1738` n `165`; fx avg `0.0313` n `6`; index avg `-0.0159` n `27`; metal avg `0.0489` n `20`; unknown avg `1.344` n `1258`
- 4h: commodity avg `-0.0292` n `13`; crypto_alt avg `-1.5813` n `239`; crypto_major avg `-1.1448` n `8`; equity avg `-1.7079` n `165`; fx avg `0.0241` n `6`; index avg `-0.1794` n `27`; metal avg `-0.6284` n `20`; unknown avg `18.0332` n `1250`
- 24h: commodity avg `-0.0287` n `13`; crypto_alt avg `-2.3078` n `239`; crypto_major avg `-1.2659` n `8`; equity avg `-5.4116` n `165`; fx avg `0.0363` n `6`; index avg `-0.3958` n `27`; metal avg `-1.3927` n `20`; unknown avg `15.289` n `1170`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
