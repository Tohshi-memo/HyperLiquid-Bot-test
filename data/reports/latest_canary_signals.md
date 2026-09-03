# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T22:52:27.009999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `-0.0228` n `232`; crypto_major avg `0.0513` n `8`; equity avg `0.0055` n `133`; fx avg `0.0039` n `6`; index avg `0.0111` n `26`; metal avg `0.0063` n `20`; unknown avg `2.7688` n `792`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.7334` n `232`; crypto_major avg `-0.6265` n `8`; equity avg `-0.0814` n `133`; fx avg `0.019` n `6`; index avg `-0.0046` n `26`; metal avg `0.0085` n `20`; unknown avg `3.7251` n `784`
- 4h: commodity avg `0.0342` n `12`; crypto_alt avg `-0.7862` n `232`; crypto_major avg `-0.3567` n `8`; equity avg `-0.1732` n `133`; fx avg `0.0211` n `6`; index avg `-0.0346` n `26`; metal avg `-0.0176` n `20`; unknown avg `4.7807` n `766`
- 24h: commodity avg `-0.1061` n `12`; crypto_alt avg `4.0324` n `232`; crypto_major avg `5.1846` n `8`; equity avg `1.2764` n `133`; fx avg `-0.223` n `6`; index avg `0.1672` n `26`; metal avg `0.8181` n `20`; unknown avg `1.0792` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
