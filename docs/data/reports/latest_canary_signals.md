# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T00:07:24.531130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.1576` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.6202` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5459` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2676` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1626` n `12`; crypto_alt avg `-0.5165` n `230`; crypto_major avg `-0.4499` n `8`; equity avg `-0.0474` n `92`; fx avg `0.0007` n `6`; index avg `0.0078` n `25`; metal avg `-0.0068` n `20`; unknown avg `-0.0713` n `765`
- 1h: commodity avg `0.3115` n `12`; crypto_alt avg `-1.5326` n `230`; crypto_major avg `-1.322` n `8`; equity avg `-0.1481` n `92`; fx avg `0.0114` n `6`; index avg `-0.0544` n `25`; metal avg `-0.0174` n `20`; unknown avg `0.7392` n `765`
- 4h: commodity avg `0.5118` n `12`; crypto_alt avg `-2.1199` n `230`; crypto_major avg `-1.6458` n `8`; equity avg `-0.2463` n `92`; fx avg `0.0171` n `6`; index avg `-0.0999` n `25`; metal avg `-0.0256` n `20`; unknown avg `0.961` n `765`
- 24h: commodity avg `0.5117` n `12`; crypto_alt avg `-1.2606` n `229`; crypto_major avg `-0.9212` n `8`; equity avg `0.0178` n `92`; fx avg `0.0186` n `6`; index avg `-0.0588` n `25`; metal avg `-0.0538` n `20`; unknown avg `1.9623` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
