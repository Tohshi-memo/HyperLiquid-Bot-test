# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T15:07:29.682620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `2.0535` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.0314` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5503` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0653` n `13`; crypto_alt avg `0.9302` n `236`; crypto_major avg `0.6184` n `8`; equity avg `0.4208` n `151`; fx avg `-0.0109` n `6`; index avg `0.072` n `26`; metal avg `-0.0784` n `20`; unknown avg `0.1386` n `1130`
- 1h: commodity avg `0.0806` n `13`; crypto_alt avg `2.8125` n `236`; crypto_major avg `2.112` n `8`; equity avg `1.5543` n `151`; fx avg `-0.0474` n `6`; index avg `0.1802` n `26`; metal avg `0.0585` n `20`; unknown avg `2.2023` n `1122`
- 4h: commodity avg `0.1552` n `13`; crypto_alt avg `2.8292` n `236`; crypto_major avg `1.5752` n `8`; equity avg `1.5347` n `151`; fx avg `-0.0073` n `6`; index avg `0.2869` n `26`; metal avg `0.0249` n `20`; unknown avg `3.6932` n `1082`
- 24h: commodity avg `-0.0529` n `13`; crypto_alt avg `0.1119` n `236`; crypto_major avg `0.089` n `8`; equity avg `-2.7254` n `151`; fx avg `0.1839` n `6`; index avg `-0.4195` n `26`; metal avg `0.2906` n `20`; unknown avg `-0.4887` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1054`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0799`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0795`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0608`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0597`, n `666`, weak_sample_signal
