# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T04:07:20.531580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3763` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `-2.0323` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2118` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.122` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.5903` n `228`; crypto_major avg `-0.1991` n `8`; equity avg `-0.3111` n `67`; fx avg `-0.0395` n `6`; index avg `-0.0907` n `23`; metal avg `0.0615` n `18`; unknown avg `-0.6813` n `419`
- 1h: commodity avg `0.4212` n `12`; crypto_alt avg `-2.2358` n `228`; crypto_major avg `-1.6111` n `8`; equity avg `-1.3595` n `67`; fx avg `-0.084` n `6`; index avg `-0.4891` n `23`; metal avg `-0.5312` n `18`; unknown avg `-0.1826` n `419`
- 4h: commodity avg `0.6368` n `12`; crypto_alt avg `-2.5989` n `228`; crypto_major avg `-1.7395` n `8`; equity avg `-1.6632` n `67`; fx avg `-0.1021` n `6`; index avg `-0.5277` n `23`; metal avg `-1.5486` n `18`; unknown avg `-0.1724` n `419`
- 24h: commodity avg `0.4347` n `12`; crypto_alt avg `-4.0629` n `228`; crypto_major avg `-3.2202` n `8`; equity avg `-2.3234` n `67`; fx avg `-0.1134` n `6`; index avg `-1.3421` n `23`; metal avg `-2.7157` n `18`; unknown avg `-1.3128` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
