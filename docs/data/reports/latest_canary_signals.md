# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T15:22:30.436392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0998` n `13`; crypto_alt avg `-0.7269` n `239`; crypto_major avg `-0.9123` n `8`; equity avg `-1.4197` n `165`; fx avg `-0.0327` n `6`; index avg `-0.1595` n `27`; metal avg `-0.2396` n `20`; unknown avg `10.1498` n `1263`
- 1h: commodity avg `-0.1544` n `13`; crypto_alt avg `-0.7421` n `239`; crypto_major avg `-0.7083` n `8`; equity avg `-0.9118` n `165`; fx avg `-0.0732` n `6`; index avg `-0.1442` n `27`; metal avg `-0.1354` n `20`; unknown avg `7.5694` n `1263`
- 4h: commodity avg `0.103` n `13`; crypto_alt avg `-0.6598` n `239`; crypto_major avg `-0.4175` n `8`; equity avg `-1.1031` n `165`; fx avg `-0.0816` n `6`; index avg `-0.1763` n `27`; metal avg `-0.2983` n `20`; unknown avg `10.4859` n `1257`
- 24h: commodity avg `0.1532` n `13`; crypto_alt avg `0.0863` n `239`; crypto_major avg `0.4642` n `8`; equity avg `0.9265` n `165`; fx avg `-0.0125` n `6`; index avg `0.1889` n `27`; metal avg `-0.3422` n `20`; unknown avg `1.9142` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
