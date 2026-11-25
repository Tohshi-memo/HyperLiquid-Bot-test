# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T15:22:29.496082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0033` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0759` n `13`; crypto_alt avg `-0.4413` n `239`; crypto_major avg `-0.4271` n `8`; equity avg `-1.0504` n `168`; fx avg `0.01` n `6`; index avg `-0.1089` n `27`; metal avg `-0.3462` n `20`; unknown avg `161.9069` n `1263`
- 1h: commodity avg `0.0818` n `13`; crypto_alt avg `-0.2942` n `239`; crypto_major avg `-0.27` n `8`; equity avg `-1.3352` n `168`; fx avg `-0.005` n `6`; index avg `-0.1117` n `27`; metal avg `-0.3992` n `20`; unknown avg `466.3716` n `1253`
- 4h: commodity avg `0.3212` n `13`; crypto_alt avg `-1.5078` n `239`; crypto_major avg `-1.232` n `8`; equity avg `-2.4514` n `168`; fx avg `0.0198` n `6`; index avg `-0.2287` n `27`; metal avg `-0.791` n `20`; unknown avg `502.1596` n `1243`
- 24h: commodity avg `0.3729` n `13`; crypto_alt avg `-2.0711` n `239`; crypto_major avg `-2.759` n `8`; equity avg `-5.4518` n `168`; fx avg `-0.0331` n `6`; index avg `-0.5303` n `27`; metal avg `-1.4574` n `20`; unknown avg `616.1133` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
