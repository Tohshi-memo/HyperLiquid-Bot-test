# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T10:37:31.492538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0529` n `12`; crypto_alt avg `0.0003` n `230`; crypto_major avg `-0.0118` n `8`; equity avg `-0.0472` n `102`; fx avg `-0.0235` n `6`; index avg `0.004` n `25`; metal avg `0.0269` n `20`; unknown avg `0.0067` n `780`
- 1h: commodity avg `0.1577` n `12`; crypto_alt avg `0.1046` n `230`; crypto_major avg `0.0726` n `8`; equity avg `0.1326` n `102`; fx avg `0.0273` n `6`; index avg `0.048` n `25`; metal avg `0.073` n `20`; unknown avg `0.0304` n `780`
- 4h: commodity avg `0.456` n `12`; crypto_alt avg `-0.3459` n `230`; crypto_major avg `-0.7912` n `8`; equity avg `0.4785` n `102`; fx avg `0.0675` n `6`; index avg `0.075` n `25`; metal avg `-0.1326` n `20`; unknown avg `0.005` n `779`
- 24h: commodity avg `0.1775` n `12`; crypto_alt avg `-0.3283` n `230`; crypto_major avg `-0.3337` n `8`; equity avg `7.7595` n `102`; fx avg `-0.0996` n `6`; index avg `1.1561` n `25`; metal avg `0.0601` n `20`; unknown avg `0.038` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
