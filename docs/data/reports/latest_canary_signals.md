# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T03:52:38.224780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.2254` n `228`; crypto_major avg `0.1507` n `8`; equity avg `0.0503` n `77`; fx avg `0.0074` n `6`; index avg `0.0137` n `23`; metal avg `0.0657` n `18`; unknown avg `0.4843` n `687`
- 1h: commodity avg `-0.04` n `12`; crypto_alt avg `0.9008` n `228`; crypto_major avg `0.7212` n `8`; equity avg `0.3934` n `77`; fx avg `0.0159` n `6`; index avg `0.1524` n `23`; metal avg `0.3624` n `18`; unknown avg `-0.4382` n `687`
- 4h: commodity avg `-0.4686` n `12`; crypto_alt avg `0.0644` n `228`; crypto_major avg `0.0498` n `8`; equity avg `-0.0099` n `77`; fx avg `-0.0225` n `6`; index avg `0.0194` n `23`; metal avg `-0.0217` n `18`; unknown avg `0.2063` n `671`
- 24h: commodity avg `0.4469` n `12`; crypto_alt avg `0.5182` n `228`; crypto_major avg `1.8608` n `8`; equity avg `1.1177` n `76`; fx avg `-0.0643` n `6`; index avg `0.5203` n `23`; metal avg `-0.2261` n `18`; unknown avg `0.9994` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0433`, n `668`, weak_sample_signal
