# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T15:37:31.683036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `0.3937` n `235`; crypto_major avg `0.1212` n `8`; equity avg `-0.0081` n `150`; fx avg `0.0063` n `6`; index avg `-0.0188` n `26`; metal avg `-0.0013` n `20`; unknown avg `1.1834` n `1048`
- 1h: commodity avg `0.0505` n `13`; crypto_alt avg `0.0282` n `235`; crypto_major avg `-0.2665` n `8`; equity avg `-0.0064` n `150`; fx avg `0.0076` n `6`; index avg `-0.0081` n `26`; metal avg `0.0123` n `20`; unknown avg `1.5124` n `1046`
- 4h: commodity avg `0.4948` n `13`; crypto_alt avg `-0.2933` n `235`; crypto_major avg `-0.4266` n `8`; equity avg `-0.5587` n `150`; fx avg `-0.0068` n `6`; index avg `-0.0888` n `26`; metal avg `0.005` n `20`; unknown avg `0.475` n `1016`
- 24h: commodity avg `0.0423` n `13`; crypto_alt avg `3.0817` n `235`; crypto_major avg `1.8541` n `8`; equity avg `0.1761` n `150`; fx avg `0.0066` n `6`; index avg `0.0411` n `26`; metal avg `0.7155` n `20`; unknown avg `1.6396` n `933`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
