# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T10:27:11.712043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0792` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `0.0998` n `228`; crypto_major avg `0.018` n `8`; equity avg `-0.0711` n `74`; fx avg `-0.001` n `6`; index avg `-0.03` n `23`; metal avg `-0.008` n `18`; unknown avg `1.0508` n `425`
- 1h: commodity avg `-0.1` n `12`; crypto_alt avg `-1.3878` n `228`; crypto_major avg `-1.1837` n `8`; equity avg `-1.8999` n `74`; fx avg `0.012` n `6`; index avg `-0.4008` n `23`; metal avg `-0.121` n `18`; unknown avg `0.8646` n `425`
- 4h: commodity avg `-0.0566` n `12`; crypto_alt avg `-0.6979` n `228`; crypto_major avg `-1.1825` n `8`; equity avg `-0.64` n `74`; fx avg `-0.0043` n `6`; index avg `-0.1033` n `23`; metal avg `-0.0476` n `18`; unknown avg `1.3487` n `425`
- 24h: commodity avg `-1.242` n `12`; crypto_alt avg `-4.6063` n `228`; crypto_major avg `-4.1382` n `8`; equity avg `-7.1848` n `74`; fx avg `-0.2571` n `6`; index avg `-4.1881` n `23`; metal avg `-4.4702` n `18`; unknown avg `0.3475` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
