# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T23:37:29.557757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.091` n `232`; crypto_major avg `0.0847` n `8`; equity avg `0.04` n `133`; fx avg `0.0025` n `6`; index avg `0.0014` n `26`; metal avg `0.0051` n `20`; unknown avg `-0.0017` n `792`
- 1h: commodity avg `-0.0231` n `12`; crypto_alt avg `0.071` n `232`; crypto_major avg `0.1083` n `8`; equity avg `0.0626` n `133`; fx avg `0.0092` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0321` n `20`; unknown avg `-0.0565` n `790`
- 4h: commodity avg `-0.0035` n `12`; crypto_alt avg `0.3092` n `232`; crypto_major avg `0.3169` n `8`; equity avg `0.186` n `133`; fx avg `-0.0211` n `6`; index avg `0.0014` n `26`; metal avg `-0.025` n `20`; unknown avg `-0.195` n `772`
- 24h: commodity avg `0.1759` n `12`; crypto_alt avg `-0.3321` n `232`; crypto_major avg `-0.541` n `8`; equity avg `1.1741` n `133`; fx avg `-0.381` n `6`; index avg `0.1383` n `26`; metal avg `0.4167` n `20`; unknown avg `-0.2072` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
