# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T10:52:25.038269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0215` n `12`; crypto_alt avg `-0.0249` n `228`; crypto_major avg `-0.0334` n `8`; equity avg `0.1391` n `72`; fx avg `0.0149` n `6`; index avg `0.0067` n `23`; metal avg `-0.0415` n `18`; unknown avg `-0.0022` n `420`
- 1h: commodity avg `-0.1807` n `12`; crypto_alt avg `0.3334` n `228`; crypto_major avg `0.0339` n `8`; equity avg `0.1615` n `72`; fx avg `0.0045` n `6`; index avg `0.0212` n `23`; metal avg `0.2048` n `18`; unknown avg `-0.2557` n `420`
- 4h: commodity avg `0.638` n `12`; crypto_alt avg `0.4863` n `228`; crypto_major avg `0.2327` n `8`; equity avg `-0.2226` n `72`; fx avg `0.0168` n `6`; index avg `0.0024` n `23`; metal avg `-0.0097` n `18`; unknown avg `-0.1657` n `420`
- 24h: commodity avg `1.8778` n `12`; crypto_alt avg `-0.8754` n `228`; crypto_major avg `-3.1361` n `8`; equity avg `0.6232` n `72`; fx avg `0.0703` n `6`; index avg `0.9041` n `23`; metal avg `-1.39` n `18`; unknown avg `-0.2084` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0446`, n `668`, weak_sample_signal
