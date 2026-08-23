# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T22:36:06.735986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `12`; crypto_alt avg `0.0224` n `231`; crypto_major avg `0.0786` n `8`; equity avg `0.0535` n `122`; fx avg `-0.0017` n `6`; index avg `0.0028` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.0109` n `793`
- 1h: commodity avg `-0.0433` n `12`; crypto_alt avg `-0.2968` n `231`; crypto_major avg `0.0369` n `8`; equity avg `-0.1028` n `122`; fx avg `0.0263` n `6`; index avg `-0.045` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.1393` n `793`
- 4h: commodity avg `-0.093` n `12`; crypto_alt avg `0.2012` n `231`; crypto_major avg `0.499` n `8`; equity avg `0.0329` n `122`; fx avg `-0.0771` n `6`; index avg `-0.0323` n `25`; metal avg `0.0091` n `20`; unknown avg `1.022` n `793`
- 24h: commodity avg `-0.2129` n `12`; crypto_alt avg `3.612` n `231`; crypto_major avg `1.6825` n `8`; equity avg `0.7197` n `122`; fx avg `-0.0872` n `6`; index avg `0.0874` n `25`; metal avg `0.0905` n `20`; unknown avg `5.8789` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
