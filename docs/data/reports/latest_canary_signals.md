# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T11:52:33.699256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0814` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7733` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6869` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0237` n `12`; crypto_alt avg `-0.1488` n `234`; crypto_major avg `-0.0552` n `8`; equity avg `-0.0973` n `141`; fx avg `-0.011` n `6`; index avg `-0.0136` n `26`; metal avg `0.0065` n `20`; unknown avg `1.318` n `945`
- 1h: commodity avg `0.0496` n `12`; crypto_alt avg `0.0248` n `234`; crypto_major avg `-0.1203` n `8`; equity avg `-0.1231` n `141`; fx avg `-0.0092` n `6`; index avg `-0.0379` n `26`; metal avg `0.0407` n `20`; unknown avg `3.2801` n `943`
- 4h: commodity avg `0.1886` n `12`; crypto_alt avg `-1.8872` n `234`; crypto_major avg `-1.8928` n `8`; equity avg `-0.7115` n `141`; fx avg `0.0418` n `6`; index avg `-0.1195` n `26`; metal avg `-0.2059` n `20`; unknown avg `0.9533` n `937`
- 24h: commodity avg `0.5159` n `12`; crypto_alt avg `-4.5192` n `234`; crypto_major avg `-3.7239` n `8`; equity avg `-2.0714` n `141`; fx avg `0.0203` n `6`; index avg `-0.4213` n `26`; metal avg `-0.3402` n `20`; unknown avg `588.6067` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
