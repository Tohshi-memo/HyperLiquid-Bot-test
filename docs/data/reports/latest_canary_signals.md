# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T03:07:30.055368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2356` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.1518` n `230`; crypto_major avg `-0.1011` n `8`; equity avg `-0.0327` n `102`; fx avg `0.0244` n `6`; index avg `-0.0058` n `25`; metal avg `-0.004` n `20`; unknown avg `0.2249` n `779`
- 1h: commodity avg `0.0941` n `12`; crypto_alt avg `-0.5313` n `230`; crypto_major avg `-0.5046` n `8`; equity avg `-0.2151` n `102`; fx avg `0.0354` n `6`; index avg `-0.0178` n `25`; metal avg `-0.0926` n `20`; unknown avg `0.088` n `779`
- 4h: commodity avg `-0.2418` n `12`; crypto_alt avg `-0.6048` n `230`; crypto_major avg `-1.0209` n `8`; equity avg `0.3415` n `102`; fx avg `0.2369` n `6`; index avg `0.2147` n `25`; metal avg `-0.3163` n `20`; unknown avg `1.0276` n `779`
- 24h: commodity avg `-0.1143` n `12`; crypto_alt avg `-0.4237` n `230`; crypto_major avg `0.367` n `8`; equity avg `7.5586` n `102`; fx avg `-0.1696` n `6`; index avg `1.0208` n `25`; metal avg `0.3607` n `20`; unknown avg `0.0308` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
