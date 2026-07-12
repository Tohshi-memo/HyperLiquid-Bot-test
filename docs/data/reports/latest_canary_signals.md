# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T01:07:30.252170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2774` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.6749` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6127` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `0.227` n `230`; crypto_major avg `0.1529` n `8`; equity avg `-0.0959` n `92`; fx avg `-0.0006` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0069` n `20`; unknown avg `0.205` n `765`
- 1h: commodity avg `0.044` n `12`; crypto_alt avg `0.2614` n `230`; crypto_major avg `0.1274` n `8`; equity avg `-0.0934` n `92`; fx avg `-0.0042` n `6`; index avg `-0.0384` n `25`; metal avg `-0.0375` n `20`; unknown avg `0.2358` n `765`
- 4h: commodity avg `0.5365` n `12`; crypto_alt avg `-1.9469` n `230`; crypto_major avg `-1.7409` n `8`; equity avg `-0.3893` n `92`; fx avg `0.0063` n `6`; index avg `-0.1282` n `25`; metal avg `-0.066` n `20`; unknown avg `1.5505` n `765`
- 24h: commodity avg `0.5211` n `12`; crypto_alt avg `-1.0005` n `229`; crypto_major avg `-0.819` n `8`; equity avg `-0.0766` n `92`; fx avg `0.0186` n `6`; index avg `-0.0933` n `25`; metal avg `-0.0888` n `20`; unknown avg `-0.2111` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
