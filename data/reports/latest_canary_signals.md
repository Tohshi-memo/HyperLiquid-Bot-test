# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T09:52:25.624213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `0.1322` n `230`; crypto_major avg `0.1095` n `8`; equity avg `0.2644` n `96`; fx avg `-0.015` n `6`; index avg `0.0279` n `25`; metal avg `0.0174` n `20`; unknown avg `0.0544` n `769`
- 1h: commodity avg `0.164` n `12`; crypto_alt avg `0.397` n `230`; crypto_major avg `0.3942` n `8`; equity avg `0.8555` n `96`; fx avg `0.0037` n `6`; index avg `0.0886` n `25`; metal avg `0.1113` n `20`; unknown avg `0.0509` n `768`
- 4h: commodity avg `0.2579` n `12`; crypto_alt avg `0.4395` n `230`; crypto_major avg `0.5065` n `8`; equity avg `0.4089` n `96`; fx avg `0.0663` n `6`; index avg `0.0046` n `25`; metal avg `0.0554` n `20`; unknown avg `0.085` n `736`
- 24h: commodity avg `0.0667` n `12`; crypto_alt avg `-1.3153` n `230`; crypto_major avg `-2.5413` n `8`; equity avg `-5.0131` n `94`; fx avg `-0.0168` n `6`; index avg `-0.7184` n `25`; metal avg `-0.7145` n `20`; unknown avg `-0.415` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
