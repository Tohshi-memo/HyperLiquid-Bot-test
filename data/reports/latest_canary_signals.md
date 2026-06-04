# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T07:52:27.125714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6836` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.642` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5796` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.5691` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.105` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1551` n `12`; crypto_alt avg `-0.2126` n `228`; crypto_major avg `-0.2243` n `8`; equity avg `-0.1613` n `73`; fx avg `0.0024` n `6`; index avg `0.0041` n `23`; metal avg `-0.0488` n `18`; unknown avg `-0.3039` n `424`
- 1h: commodity avg `0.1169` n `12`; crypto_alt avg `-1.3677` n `228`; crypto_major avg `-1.1211` n `8`; equity avg `-0.1742` n `73`; fx avg `0.0665` n `6`; index avg `-0.0161` n `23`; metal avg `-0.0284` n `18`; unknown avg `-0.4705` n `424`
- 4h: commodity avg `0.0718` n `12`; crypto_alt avg `-2.7344` n `228`; crypto_major avg `-2.6118` n `8`; equity avg `-0.0427` n `73`; fx avg `0.0825` n `6`; index avg `0.0302` n `23`; metal avg `-0.0322` n `18`; unknown avg `-0.8028` n `404`
- 24h: commodity avg `-0.363` n `12`; crypto_alt avg `-5.9052` n `228`; crypto_major avg `-5.3425` n `8`; equity avg `-3.8444` n `73`; fx avg `0.0312` n `6`; index avg `-1.084` n `23`; metal avg `-1.1689` n `18`; unknown avg `-1.0926` n `403`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
