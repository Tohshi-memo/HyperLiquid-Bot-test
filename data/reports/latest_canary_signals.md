# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T10:22:31.169605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `0.1671` n `239`; crypto_major avg `0.1938` n `8`; equity avg `0.0376` n `162`; fx avg `0.0025` n `6`; index avg `0.0052` n `27`; metal avg `0.0123` n `20`; unknown avg `0.889` n `1269`
- 1h: commodity avg `-0.1526` n `13`; crypto_alt avg `0.42` n `239`; crypto_major avg `0.4814` n `8`; equity avg `0.328` n `162`; fx avg `-0.0084` n `6`; index avg `0.0338` n `27`; metal avg `0.0496` n `20`; unknown avg `1.164` n `1255`
- 4h: commodity avg `-0.0307` n `13`; crypto_alt avg `0.04` n `239`; crypto_major avg `0.1382` n `8`; equity avg `0.447` n `162`; fx avg `0.0767` n `6`; index avg `0.02` n `27`; metal avg `-0.2153` n `20`; unknown avg `17.6271` n `1233`
- 24h: commodity avg `-0.0864` n `13`; crypto_alt avg `-1.6706` n `239`; crypto_major avg `-0.763` n `8`; equity avg `-0.5177` n `162`; fx avg `-0.0946` n `6`; index avg `0.0005` n `27`; metal avg `-0.864` n `20`; unknown avg `17.5108` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
