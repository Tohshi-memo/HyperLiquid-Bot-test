# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T20:22:28.657807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `-0.0592` n `232`; crypto_major avg `0.0297` n `8`; equity avg `-0.2358` n `133`; fx avg `-0.0119` n `6`; index avg `-0.0283` n `26`; metal avg `-0.0199` n `20`; unknown avg `0.0874` n `784`
- 1h: commodity avg `-0.0511` n `12`; crypto_alt avg `0.1461` n `232`; crypto_major avg `0.1112` n `8`; equity avg `-0.1723` n `133`; fx avg `-0.0419` n `6`; index avg `-0.0266` n `26`; metal avg `0.024` n `20`; unknown avg `0.6921` n `778`
- 4h: commodity avg `0.0098` n `12`; crypto_alt avg `-0.1539` n `232`; crypto_major avg `-0.0986` n `8`; equity avg `0.4547` n `133`; fx avg `-0.0256` n `6`; index avg `0.0043` n `26`; metal avg `0.0824` n `20`; unknown avg `-0.3138` n `778`
- 24h: commodity avg `0.1222` n `12`; crypto_alt avg `-0.2448` n `232`; crypto_major avg `-0.2693` n `8`; equity avg `0.488` n `133`; fx avg `-0.388` n `6`; index avg `0.0952` n `26`; metal avg `0.4918` n `20`; unknown avg `0.4075` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0446`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
