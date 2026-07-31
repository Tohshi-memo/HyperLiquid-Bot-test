# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T01:22:27.401994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `12`; crypto_alt avg `0.0625` n `230`; crypto_major avg `0.098` n `8`; equity avg `-0.0136` n `102`; fx avg `0.0095` n `6`; index avg `-0.004` n `25`; metal avg `-0.0694` n `20`; unknown avg `0.0082` n `779`
- 1h: commodity avg `-0.2351` n `12`; crypto_alt avg `0.5558` n `230`; crypto_major avg `0.3557` n `8`; equity avg `0.804` n `102`; fx avg `0.0875` n `6`; index avg `0.23` n `25`; metal avg `-0.1901` n `20`; unknown avg `2.308` n `779`
- 4h: commodity avg `-0.1824` n `12`; crypto_alt avg `0.4991` n `230`; crypto_major avg `0.3431` n `8`; equity avg `1.623` n `102`; fx avg `0.2378` n `6`; index avg `0.4782` n `25`; metal avg `-0.1951` n `20`; unknown avg `0.225` n `779`
- 24h: commodity avg `-0.1633` n `12`; crypto_alt avg `1.0761` n `230`; crypto_major avg `1.7849` n `8`; equity avg `8.0771` n `102`; fx avg `-0.1619` n `6`; index avg `1.2009` n `25`; metal avg `0.3075` n `20`; unknown avg `0.1443` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
