# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T15:07:30.158705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1136` n `12`; crypto_alt avg `-0.3167` n `230`; crypto_major avg `-0.3647` n `8`; equity avg `-0.5558` n `96`; fx avg `0.0257` n `6`; index avg `-0.0667` n `25`; metal avg `0.065` n `20`; unknown avg `-0.0465` n `769`
- 1h: commodity avg `-0.1997` n `12`; crypto_alt avg `-0.6172` n `230`; crypto_major avg `-0.6657` n `8`; equity avg `-0.6776` n `96`; fx avg `0.0278` n `6`; index avg `-0.0809` n `25`; metal avg `0.0724` n `20`; unknown avg `0.0151` n `769`
- 4h: commodity avg `0.0948` n `12`; crypto_alt avg `-0.4959` n `230`; crypto_major avg `-0.6217` n `8`; equity avg `-0.191` n `96`; fx avg `0.0452` n `6`; index avg `-0.0597` n `25`; metal avg `0.1349` n `20`; unknown avg `0.2586` n `769`
- 24h: commodity avg `0.321` n `12`; crypto_alt avg `-2.1747` n `230`; crypto_major avg `-3.1667` n `8`; equity avg `-3.0551` n `94`; fx avg `0.0131` n `6`; index avg `-0.5452` n `25`; metal avg `-0.3331` n `20`; unknown avg `-0.4371` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
