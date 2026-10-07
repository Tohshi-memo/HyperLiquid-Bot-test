# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T01:52:29.793836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0131` n `13`; crypto_alt avg `-0.1684` n `235`; crypto_major avg `-0.0355` n `8`; equity avg `-0.0883` n `150`; fx avg `-0.0023` n `6`; index avg `-0.0151` n `26`; metal avg `-0.0657` n `20`; unknown avg `-0.0409` n `1076`
- 1h: commodity avg `0.1136` n `13`; crypto_alt avg `-0.8826` n `235`; crypto_major avg `-0.4952` n `8`; equity avg `-0.3776` n `150`; fx avg `-0.024` n `6`; index avg `-0.0477` n `26`; metal avg `-0.073` n `20`; unknown avg `0.34` n `1074`
- 4h: commodity avg `0.2235` n `13`; crypto_alt avg `-0.7017` n `235`; crypto_major avg `-0.4195` n `8`; equity avg `-0.2847` n `150`; fx avg `-0.0054` n `6`; index avg `-0.0269` n `26`; metal avg `-0.1141` n `20`; unknown avg `0.2701` n `1060`
- 24h: commodity avg `0.4918` n `13`; crypto_alt avg `-1.2862` n `235`; crypto_major avg `-1.0922` n `8`; equity avg `0.2019` n `149`; fx avg `0.0632` n `6`; index avg `0.0153` n `26`; metal avg `-0.0074` n `20`; unknown avg `870.8191` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
