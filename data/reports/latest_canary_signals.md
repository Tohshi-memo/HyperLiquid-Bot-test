# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T09:37:27.185861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2593` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `-0.6222` n `228`; crypto_major avg `-0.6709` n `8`; equity avg `-0.0551` n `74`; fx avg `0.0087` n `6`; index avg `-0.0614` n `23`; metal avg `-0.0822` n `18`; unknown avg `-0.1738` n `547`
- 1h: commodity avg `-0.2683` n `12`; crypto_alt avg `-0.6847` n `228`; crypto_major avg `-0.5127` n `8`; equity avg `0.0864` n `74`; fx avg `0.0239` n `6`; index avg `0.048` n `23`; metal avg `-0.1127` n `18`; unknown avg `-0.3386` n `547`
- 4h: commodity avg `-0.273` n `12`; crypto_alt avg `-1.0138` n `228`; crypto_major avg `-1.1145` n `8`; equity avg `-0.0001` n `74`; fx avg `0.1668` n `6`; index avg `0.1448` n `23`; metal avg `0.0969` n `18`; unknown avg `-0.0343` n `503`
- 24h: commodity avg `-1.4724` n `12`; crypto_alt avg `-0.5855` n `228`; crypto_major avg `0.0795` n `8`; equity avg `2.3306` n `74`; fx avg `0.0839` n `6`; index avg `1.2323` n `23`; metal avg `0.8292` n `18`; unknown avg `-2.9133` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
