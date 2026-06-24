# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T17:22:29.751593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.5795` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.3197` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.2835` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.2399` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.1132` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.031` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.031` n `12`; crypto_alt avg `-1.186` n `228`; crypto_major avg `-0.8252` n `8`; equity avg `-0.3709` n `86`; fx avg `0.0034` n `6`; index avg `-0.049` n `23`; metal avg `-0.1711` n `20`; unknown avg `-0.4351` n `764`
- 1h: commodity avg `-0.046` n `12`; crypto_alt avg `-3.3451` n `228`; crypto_major avg `-2.2859` n `8`; equity avg `-1.268` n `86`; fx avg `0.0239` n `6`; index avg `-0.1727` n `23`; metal avg `-0.2549` n `20`; unknown avg `-0.9816` n `764`
- 4h: commodity avg `0.1493` n `12`; crypto_alt avg `-3.9159` n `228`; crypto_major avg `-3.4302` n `8`; equity avg `-2.0358` n `86`; fx avg `0.0262` n `6`; index avg `-0.1467` n `23`; metal avg `-0.1105` n `20`; unknown avg `-0.1947` n `764`
- 24h: commodity avg `-0.4689` n `12`; crypto_alt avg `-5.2551` n `228`; crypto_major avg `-4.6481` n `8`; equity avg `1.2371` n `86`; fx avg `0.0654` n `6`; index avg `-0.0799` n `23`; metal avg `-1.9149` n `20`; unknown avg `-0.1214` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
