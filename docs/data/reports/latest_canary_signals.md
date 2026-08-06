# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T05:52:31.002734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `-0.0028` n `230`; crypto_major avg `0.0321` n `8`; equity avg `-0.0709` n `108`; fx avg `0.0262` n `6`; index avg `-0.02` n `25`; metal avg `0.101` n `20`; unknown avg `2.7233` n `782`
- 1h: commodity avg `0.046` n `12`; crypto_alt avg `0.0254` n `230`; crypto_major avg `0.297` n `8`; equity avg `-0.0741` n `108`; fx avg `-0.0077` n `6`; index avg `-0.0382` n `25`; metal avg `0.0465` n `20`; unknown avg `2.4773` n `782`
- 4h: commodity avg `-0.1477` n `12`; crypto_alt avg `0.1231` n `230`; crypto_major avg `0.1002` n `8`; equity avg `0.329` n `108`; fx avg `0.0064` n `6`; index avg `0.0247` n `25`; metal avg `-0.1367` n `20`; unknown avg `0.1601` n `782`
- 24h: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.053` n `230`; crypto_major avg `-0.0353` n `8`; equity avg `-2.2821` n `108`; fx avg `-0.0426` n `6`; index avg `-0.4212` n `25`; metal avg `0.3013` n `20`; unknown avg `0.8316` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
