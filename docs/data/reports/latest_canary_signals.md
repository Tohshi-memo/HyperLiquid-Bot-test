# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T22:37:29.673696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5737` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.567` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0321` n `12`; crypto_alt avg `0.4457` n `234`; crypto_major avg `0.4359` n `8`; equity avg `0.0677` n `137`; fx avg `0.0009` n `6`; index avg `0.0087` n `27`; metal avg `0.0321` n `20`; unknown avg `6.1087` n `911`
- 1h: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.1743` n `234`; crypto_major avg `0.0365` n `8`; equity avg `0.0313` n `137`; fx avg `0.0166` n `6`; index avg `0.0091` n `27`; metal avg `0.0562` n `20`; unknown avg `5.4386` n `869`
- 4h: commodity avg `-0.0591` n `12`; crypto_alt avg `-1.3606` n `234`; crypto_major avg `-1.543` n `8`; equity avg `-0.0592` n `137`; fx avg `0.0032` n `6`; index avg `0.024` n `27`; metal avg `0.0307` n `20`; unknown avg `5.4869` n `845`
- 24h: commodity avg `0.4603` n `12`; crypto_alt avg `-4.2462` n `234`; crypto_major avg `-4.6534` n `8`; equity avg `-1.2479` n `137`; fx avg `0.2298` n `6`; index avg `-0.0541` n `27`; metal avg `0.1992` n `20`; unknown avg `1.9126` n `802`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
