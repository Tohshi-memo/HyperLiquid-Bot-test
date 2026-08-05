# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T22:37:24.673436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.0184` n `230`; crypto_major avg `0.0008` n `8`; equity avg `0.142` n `108`; fx avg `0.0049` n `6`; index avg `0.028` n `25`; metal avg `0.0194` n `20`; unknown avg `-0.0358` n `782`
- 1h: commodity avg `-0.0778` n `12`; crypto_alt avg `0.1181` n `230`; crypto_major avg `0.0127` n `8`; equity avg `0.4009` n `108`; fx avg `0.0033` n `6`; index avg `0.0722` n `25`; metal avg `0.0238` n `20`; unknown avg `-0.0992` n `782`
- 4h: commodity avg `-0.0575` n `12`; crypto_alt avg `-0.2167` n `230`; crypto_major avg `-0.5242` n `8`; equity avg `-0.6891` n `108`; fx avg `0.0069` n `6`; index avg `-0.0421` n `25`; metal avg `-0.0087` n `20`; unknown avg `-0.0427` n `782`
- 24h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.3989` n `230`; crypto_major avg `0.5411` n `8`; equity avg `-0.6549` n `108`; fx avg `-0.0393` n `6`; index avg `-0.0713` n `25`; metal avg `0.7811` n `20`; unknown avg `0.7597` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
