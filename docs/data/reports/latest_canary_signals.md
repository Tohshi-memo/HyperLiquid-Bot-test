# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T08:07:32.307614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `13`; crypto_alt avg `0.0952` n `239`; crypto_major avg `0.0404` n `8`; equity avg `0.019` n `166`; fx avg `-0.0073` n `6`; index avg `0.0039` n `27`; metal avg `-0.0041` n `20`; unknown avg `40.4696` n `1243`
- 1h: commodity avg `0.0524` n `13`; crypto_alt avg `0.3656` n `239`; crypto_major avg `0.1484` n `8`; equity avg `0.0369` n `166`; fx avg `-0.0163` n `6`; index avg `0.0099` n `27`; metal avg `-0.0029` n `20`; unknown avg `40.009` n `1245`
- 4h: commodity avg `0.025` n `13`; crypto_alt avg `0.1848` n `239`; crypto_major avg `-0.2151` n `8`; equity avg `-0.0794` n `166`; fx avg `-0.0219` n `6`; index avg `-0.0011` n `27`; metal avg `0.0126` n `20`; unknown avg `207.3625` n `1207`
- 24h: commodity avg `0.06` n `13`; crypto_alt avg `1.9673` n `239`; crypto_major avg `2.5799` n `8`; equity avg `0.7136` n `166`; fx avg `0.0475` n `6`; index avg `0.1177` n `27`; metal avg `0.0772` n `20`; unknown avg `583.5739` n `1068`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
