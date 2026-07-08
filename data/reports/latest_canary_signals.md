# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T03:07:27.929149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.4004` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.5819` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5108` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `0.1443` n `229`; crypto_major avg `0.0973` n `8`; equity avg `0.1543` n `91`; fx avg `-0.0126` n `6`; index avg `0.0563` n `25`; metal avg `0.1358` n `20`; unknown avg `-0.0278` n `763`
- 1h: commodity avg `0.0296` n `12`; crypto_alt avg `0.229` n `229`; crypto_major avg `0.1743` n `8`; equity avg `0.3367` n `91`; fx avg `-0.0186` n `6`; index avg `0.0922` n `25`; metal avg `0.1282` n `20`; unknown avg `0.1809` n `763`
- 4h: commodity avg `-0.0028` n `12`; crypto_alt avg `-1.0298` n `229`; crypto_major avg `-1.3805` n `8`; equity avg `1.0199` n `91`; fx avg `-0.0289` n `6`; index avg `0.1303` n `25`; metal avg `0.2014` n `20`; unknown avg `0.8553` n `763`
- 24h: commodity avg `0.8922` n `12`; crypto_alt avg `-2.6884` n `229`; crypto_major avg `-2.0016` n `8`; equity avg `-1.466` n `91`; fx avg `-0.2055` n `6`; index avg `-0.1931` n `25`; metal avg `-0.2059` n `20`; unknown avg `-0.4233` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
