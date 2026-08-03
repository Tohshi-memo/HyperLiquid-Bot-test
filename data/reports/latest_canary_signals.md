# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T22:07:27.636994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `12`; crypto_alt avg `-0.2819` n `230`; crypto_major avg `-0.2498` n `8`; equity avg `0.0474` n `103`; fx avg `0.0198` n `6`; index avg `0.0153` n `25`; metal avg `-0.0495` n `20`; unknown avg `0.062` n `784`
- 1h: commodity avg `-0.0325` n `12`; crypto_alt avg `-0.2016` n `230`; crypto_major avg `-0.3993` n `8`; equity avg `0.1511` n `103`; fx avg `0.0227` n `6`; index avg `0.0338` n `25`; metal avg `-0.0669` n `20`; unknown avg `0.3595` n `784`
- 4h: commodity avg `0.0558` n `12`; crypto_alt avg `-0.1561` n `230`; crypto_major avg `-0.5627` n `8`; equity avg `0.1683` n `103`; fx avg `0.0511` n `6`; index avg `0.0361` n `25`; metal avg `0.1358` n `20`; unknown avg `0.1781` n `784`
- 24h: commodity avg `0.2322` n `12`; crypto_alt avg `-0.1134` n `230`; crypto_major avg `-0.4876` n `8`; equity avg `2.0889` n `103`; fx avg `-0.274` n `6`; index avg `0.1129` n `25`; metal avg `-0.353` n `20`; unknown avg `-0.0459` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
