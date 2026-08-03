# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T19:52:28.683779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `-0.1277` n `230`; crypto_major avg `0.0191` n `8`; equity avg `0.103` n `103`; fx avg `0.0057` n `6`; index avg `0.009` n `25`; metal avg `0.0005` n `20`; unknown avg `0.0271` n `784`
- 1h: commodity avg `-0.0364` n `12`; crypto_alt avg `-0.1099` n `230`; crypto_major avg `-0.0007` n `8`; equity avg `0.2017` n `103`; fx avg `0.0121` n `6`; index avg `0.0377` n `25`; metal avg `0.0767` n `20`; unknown avg `-0.103` n `784`
- 4h: commodity avg `0.0764` n `12`; crypto_alt avg `0.2377` n `230`; crypto_major avg `0.0996` n `8`; equity avg `0.9287` n `103`; fx avg `-0.0161` n `6`; index avg `0.1475` n `25`; metal avg `0.1259` n `20`; unknown avg `-0.2194` n `784`
- 24h: commodity avg `-0.028` n `12`; crypto_alt avg `0.2363` n `230`; crypto_major avg `0.4272` n `8`; equity avg `2.0069` n `103`; fx avg `-0.2552` n `6`; index avg `0.0772` n `25`; metal avg `-0.3901` n `20`; unknown avg `0.0245` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
