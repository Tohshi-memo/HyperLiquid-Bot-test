# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T09:07:30.607497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0686` n `13`; crypto_alt avg `0.1585` n `235`; crypto_major avg `-0.0078` n `8`; equity avg `0.0909` n `151`; fx avg `0.0126` n `6`; index avg `-0.0112` n `26`; metal avg `0.032` n `20`; unknown avg `0.0496` n `1105`
- 1h: commodity avg `0.2808` n `13`; crypto_alt avg `-0.13` n `235`; crypto_major avg `-0.3336` n `8`; equity avg `-0.407` n `151`; fx avg `0.0011` n `6`; index avg `-0.0834` n `26`; metal avg `-0.0607` n `20`; unknown avg `0.2787` n `1091`
- 4h: commodity avg `0.3916` n `13`; crypto_alt avg `-0.9035` n `235`; crypto_major avg `-0.6786` n `8`; equity avg `-0.8181` n `151`; fx avg `-0.0527` n `6`; index avg `-0.1316` n `26`; metal avg `-0.1046` n `20`; unknown avg `0.5924` n `1031`
- 24h: commodity avg `-0.1015` n `13`; crypto_alt avg `2.1059` n `235`; crypto_major avg `1.3793` n `8`; equity avg `-1.0556` n `151`; fx avg `-0.0992` n `6`; index avg `-0.127` n `26`; metal avg `-0.0211` n `20`; unknown avg `0.1366` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
