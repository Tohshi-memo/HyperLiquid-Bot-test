# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T15:22:38.475644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0767` n `12`; crypto_alt avg `0.1464` n `230`; crypto_major avg `0.2314` n `8`; equity avg `0.217` n `96`; fx avg `0.0071` n `6`; index avg `0.0746` n `25`; metal avg `0.0308` n `20`; unknown avg `-0.0351` n `769`
- 1h: commodity avg `-0.1224` n `12`; crypto_alt avg `-0.2864` n `230`; crypto_major avg `-0.2342` n `8`; equity avg `-0.6147` n `96`; fx avg `0.0299` n `6`; index avg `-0.0269` n `25`; metal avg `0.0671` n `20`; unknown avg `-0.0801` n `769`
- 4h: commodity avg `0.1433` n `12`; crypto_alt avg `-0.298` n `230`; crypto_major avg `-0.3358` n `8`; equity avg `0.2715` n `96`; fx avg `0.0396` n `6`; index avg `0.0696` n `25`; metal avg `0.1671` n `20`; unknown avg `0.0259` n `769`
- 24h: commodity avg `0.3972` n `12`; crypto_alt avg `-2.103` n `230`; crypto_major avg `-3.021` n `8`; equity avg `-2.8664` n `94`; fx avg `0.0162` n `6`; index avg `-0.4651` n `25`; metal avg `-0.3841` n `20`; unknown avg `-0.4288` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
