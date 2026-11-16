# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T05:52:25.880661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0468` n `13`; crypto_alt avg `-0.0999` n `239`; crypto_major avg `-0.2116` n `8`; equity avg `-0.2073` n `162`; fx avg `0.0063` n `6`; index avg `-0.0198` n `27`; metal avg `-0.1423` n `20`; unknown avg `0.1358` n `1265`
- 1h: commodity avg `0.0574` n `13`; crypto_alt avg `-0.3585` n `239`; crypto_major avg `-0.2454` n `8`; equity avg `-0.4974` n `162`; fx avg `-0.025` n `6`; index avg `-0.0495` n `27`; metal avg `-0.0958` n `20`; unknown avg `3.8859` n `1259`
- 4h: commodity avg `0.0908` n `13`; crypto_alt avg `0.2152` n `239`; crypto_major avg `-0.1169` n `8`; equity avg `-0.6541` n `162`; fx avg `-0.0573` n `6`; index avg `-0.1018` n `27`; metal avg `-0.0673` n `20`; unknown avg `-0.1644` n `1241`
- 24h: commodity avg `-0.3068` n `13`; crypto_alt avg `-0.4355` n `239`; crypto_major avg `-0.0893` n `8`; equity avg `-0.5874` n `162`; fx avg `-0.0704` n `6`; index avg `-0.0598` n `27`; metal avg `0.0525` n `20`; unknown avg `177.7025` n `1127`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
