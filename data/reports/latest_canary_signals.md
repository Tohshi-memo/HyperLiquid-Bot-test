# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T22:52:26.650065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.014` n `12`; crypto_alt avg `0.0258` n `228`; crypto_major avg `0.0225` n `8`; equity avg `0.017` n `88`; fx avg `-0.0005` n `6`; index avg `0.0006` n `23`; metal avg `-0.0094` n `20`; unknown avg `0.0295` n `765`
- 1h: commodity avg `-0.0628` n `12`; crypto_alt avg `-0.3687` n `228`; crypto_major avg `-0.4173` n `8`; equity avg `-0.0096` n `88`; fx avg `-0.0027` n `6`; index avg `0.0015` n `23`; metal avg `-0.0474` n `20`; unknown avg `-0.187` n `763`
- 4h: commodity avg `-0.036` n `12`; crypto_alt avg `-0.5422` n `228`; crypto_major avg `0.0938` n `8`; equity avg `0.2764` n `88`; fx avg `0.0289` n `6`; index avg `0.0092` n `23`; metal avg `-0.0369` n `20`; unknown avg `0.1918` n `763`
- 24h: commodity avg `-0.2831` n `12`; crypto_alt avg `2.1222` n `228`; crypto_major avg `3.6799` n `8`; equity avg `1.6839` n `88`; fx avg `0.2198` n `6`; index avg `0.0713` n `23`; metal avg `-0.3211` n `20`; unknown avg `1.7328` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
