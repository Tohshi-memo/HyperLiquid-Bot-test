# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T01:07:30.963602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `13`; crypto_alt avg `0.0302` n `236`; crypto_major avg `0.0503` n `8`; equity avg `-0.0302` n `151`; fx avg `0.0133` n `6`; index avg `-0.0201` n `26`; metal avg `0.0233` n `20`; unknown avg `0.3862` n `1134`
- 1h: commodity avg `-0.1498` n `13`; crypto_alt avg `-0.6314` n `236`; crypto_major avg `-0.216` n `8`; equity avg `-0.4413` n `151`; fx avg `0.1042` n `6`; index avg `-0.1671` n `26`; metal avg `0.1551` n `20`; unknown avg `-0.2994` n `1134`
- 4h: commodity avg `-0.1657` n `13`; crypto_alt avg `-0.1301` n `236`; crypto_major avg `0.1032` n `8`; equity avg `-1.392` n `151`; fx avg `0.1969` n `6`; index avg `-0.3329` n `26`; metal avg `0.2129` n `20`; unknown avg `0.7956` n `1046`
- 24h: commodity avg `-0.4652` n `13`; crypto_alt avg `-2.7979` n `236`; crypto_major avg `-2.2706` n `8`; equity avg `-5.7819` n `151`; fx avg `0.0255` n `6`; index avg `-0.923` n `26`; metal avg `-0.6034` n `20`; unknown avg `1393.7046` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1018`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0977`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0922`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0854`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0767`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
