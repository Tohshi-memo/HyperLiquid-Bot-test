# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T22:07:25.626849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.309` n `230`; crypto_major avg `0.307` n `8`; equity avg `0.0576` n `92`; fx avg `-0.0027` n `6`; index avg `0.0176` n `25`; metal avg `0.0014` n `20`; unknown avg `0.0561` n `766`
- 1h: commodity avg `0.0367` n `12`; crypto_alt avg `-0.3094` n `230`; crypto_major avg `-0.0872` n `8`; equity avg `0.0297` n `92`; fx avg `0.001` n `6`; index avg `0.0285` n `25`; metal avg `0.0056` n `20`; unknown avg `-0.008` n `766`
- 4h: commodity avg `0.0467` n `12`; crypto_alt avg `-0.4586` n `230`; crypto_major avg `0.027` n `8`; equity avg `-0.1412` n `92`; fx avg `-0.0069` n `6`; index avg `-0.0566` n `25`; metal avg `0.0638` n `20`; unknown avg `-0.26` n `766`
- 24h: commodity avg `0.7166` n `12`; crypto_alt avg `-2.0055` n `230`; crypto_major avg `-2.4224` n `8`; equity avg `-3.0555` n `92`; fx avg `-0.0117` n `6`; index avg `-0.5893` n `25`; metal avg `-0.3635` n `20`; unknown avg `-0.4017` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
