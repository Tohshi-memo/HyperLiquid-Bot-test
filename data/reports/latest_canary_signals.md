# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T01:37:30.811954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0505` n `13`; crypto_alt avg `0.1222` n `235`; crypto_major avg `0.1558` n `8`; equity avg `0.1129` n `150`; fx avg `-0.0061` n `6`; index avg `0.0269` n `26`; metal avg `0.0807` n `20`; unknown avg `0.4122` n `1077`
- 1h: commodity avg `0.0394` n `13`; crypto_alt avg `0.2261` n `235`; crypto_major avg `0.2019` n `8`; equity avg `0.1187` n `150`; fx avg `-0.0156` n `6`; index avg `0.0204` n `26`; metal avg `0.3674` n `20`; unknown avg `0.0105` n `1075`
- 4h: commodity avg `0.1575` n `13`; crypto_alt avg `1.322` n `235`; crypto_major avg `0.6512` n `8`; equity avg `0.1431` n `150`; fx avg `-0.0532` n `6`; index avg `0.0042` n `26`; metal avg `0.3312` n `20`; unknown avg `1.3548` n `1069`
- 24h: commodity avg `0.3033` n `13`; crypto_alt avg `-2.4722` n `235`; crypto_major avg `-2.6011` n `8`; equity avg `-1.0857` n `150`; fx avg `-0.2036` n `6`; index avg `-0.217` n `26`; metal avg `-0.3147` n `20`; unknown avg `247.8947` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
