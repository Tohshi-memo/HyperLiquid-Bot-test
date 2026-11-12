# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T22:07:26.633314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `13`; crypto_alt avg `-0.0325` n `239`; crypto_major avg `-0.0388` n `8`; equity avg `-0.0259` n `162`; fx avg `-0.0023` n `6`; index avg `-0.0059` n `27`; metal avg `0.021` n `20`; unknown avg `11.9173` n `1249`
- 1h: commodity avg `-0.0302` n `13`; crypto_alt avg `0.3455` n `239`; crypto_major avg `0.2231` n `8`; equity avg `0.1051` n `162`; fx avg `-0.0162` n `6`; index avg `-0.0021` n `27`; metal avg `0.0405` n `20`; unknown avg `11.6159` n `1247`
- 4h: commodity avg `0.2396` n `13`; crypto_alt avg `0.8038` n `239`; crypto_major avg `0.1848` n `8`; equity avg `-0.157` n `162`; fx avg `0.011` n `6`; index avg `-0.012` n `27`; metal avg `-0.0327` n `20`; unknown avg `0.2342` n `1219`
- 24h: commodity avg `0.8511` n `13`; crypto_alt avg `-1.8274` n `239`; crypto_major avg `-2.7362` n `8`; equity avg `-2.2007` n `162`; fx avg `-0.1452` n `6`; index avg `-0.099` n `27`; metal avg `-0.719` n `20`; unknown avg `131.1615` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
