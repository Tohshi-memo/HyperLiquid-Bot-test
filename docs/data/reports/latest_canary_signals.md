# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T00:52:25.900649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3059` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7298` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.673` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5099` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.0284` n `230`; crypto_major avg `0.0343` n `8`; equity avg `-0.0166` n `92`; fx avg `-0.0053` n `6`; index avg `-0.0133` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.0668` n `765`
- 1h: commodity avg `0.187` n `12`; crypto_alt avg `-0.5133` n `230`; crypto_major avg `-0.5802` n `8`; equity avg `-0.0611` n `92`; fx avg `-0.0029` n `6`; index avg `-0.0221` n `25`; metal avg `-0.0376` n `20`; unknown avg `0.0125` n `765`
- 4h: commodity avg `0.5113` n `12`; crypto_alt avg `-2.1372` n `230`; crypto_major avg `-1.7946` n `8`; equity avg `-0.2847` n `92`; fx avg `0.0102` n `6`; index avg `-0.1216` n `25`; metal avg `-0.0648` n `20`; unknown avg `1.2908` n `765`
- 24h: commodity avg `0.4996` n `12`; crypto_alt avg `-1.2442` n `229`; crypto_major avg `-0.9725` n `8`; equity avg `0.0355` n `92`; fx avg `0.0203` n `6`; index avg `-0.0854` n `25`; metal avg `-0.0845` n `20`; unknown avg `-0.2317` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
