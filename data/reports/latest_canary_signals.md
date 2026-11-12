# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T22:52:24.602032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0302` n `13`; crypto_alt avg `0.1238` n `239`; crypto_major avg `0.0762` n `8`; equity avg `0.1115` n `162`; fx avg `0.0` n `6`; index avg `0.004` n `27`; metal avg `0.0057` n `20`; unknown avg `1.4894` n `1231`
- 1h: commodity avg `-0.0169` n `13`; crypto_alt avg `-0.0816` n `239`; crypto_major avg `-0.1738` n `8`; equity avg `0.052` n `162`; fx avg `-0.0079` n `6`; index avg `-0.0091` n `27`; metal avg `0.0255` n `20`; unknown avg `13.3852` n `1221`
- 4h: commodity avg `0.1925` n `13`; crypto_alt avg `0.8325` n `239`; crypto_major avg `0.3294` n `8`; equity avg `0.2686` n `162`; fx avg `-0.0017` n `6`; index avg `0.0217` n `27`; metal avg `-0.0051` n `20`; unknown avg `1.6471` n `1187`
- 24h: commodity avg `0.8789` n `13`; crypto_alt avg `-0.8478` n `239`; crypto_major avg `-1.9321` n `8`; equity avg `-1.0672` n `162`; fx avg `-0.1346` n `6`; index avg `-0.0008` n `27`; metal avg `-0.6995` n `20`; unknown avg `55.9406` n `1121`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
