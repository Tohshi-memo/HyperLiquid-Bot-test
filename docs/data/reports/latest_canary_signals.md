# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T04:37:25.088631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.29` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3803` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2021` n `12`; crypto_alt avg `-0.2999` n `228`; crypto_major avg `-0.2373` n `8`; equity avg `-0.1139` n `74`; fx avg `0.0101` n `6`; index avg `0.0282` n `23`; metal avg `-0.1389` n `18`; unknown avg `-0.1563` n `517`
- 1h: commodity avg `0.3116` n `12`; crypto_alt avg `-0.7289` n `228`; crypto_major avg `-0.9201` n `8`; equity avg `-0.3983` n `74`; fx avg `0.0098` n `6`; index avg `-0.1354` n `23`; metal avg `0.0575` n `18`; unknown avg `2.2005` n `517`
- 4h: commodity avg `0.5566` n `12`; crypto_alt avg `-1.7793` n `228`; crypto_major avg `-1.7334` n `8`; equity avg `-0.8133` n `74`; fx avg `-0.0309` n `6`; index avg `-0.3531` n `23`; metal avg `-0.7791` n `18`; unknown avg `-0.4013` n `517`
- 24h: commodity avg `0.6496` n `12`; crypto_alt avg `0.3488` n `228`; crypto_major avg `2.3647` n `8`; equity avg `1.2515` n `74`; fx avg `-0.0982` n `6`; index avg `0.2438` n `23`; metal avg `-0.2662` n `18`; unknown avg `-5.6566` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
