# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T07:52:28.342480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `13`; crypto_alt avg `-0.1397` n `239`; crypto_major avg `-0.0202` n `8`; equity avg `-0.1271` n `161`; fx avg `0.0142` n `6`; index avg `-0.0164` n `27`; metal avg `0.0536` n `20`; unknown avg `0.2101` n `1260`
- 1h: commodity avg `0.1178` n `13`; crypto_alt avg `0.0556` n `239`; crypto_major avg `0.2939` n `8`; equity avg `0.1414` n `161`; fx avg `0.048` n `6`; index avg `-0.0003` n `27`; metal avg `0.0019` n `20`; unknown avg `1.7992` n `1254`
- 4h: commodity avg `0.2492` n `13`; crypto_alt avg `-0.4705` n `239`; crypto_major avg `-0.3697` n `8`; equity avg `-0.6521` n `161`; fx avg `0.0635` n `6`; index avg `-0.103` n `27`; metal avg `-0.0883` n `20`; unknown avg `1.5452` n `1206`
- 24h: commodity avg `0.3087` n `13`; crypto_alt avg `-1.4725` n `239`; crypto_major avg `-0.6786` n `8`; equity avg `-0.5719` n `161`; fx avg `-0.1136` n `6`; index avg `-0.0959` n `27`; metal avg `-0.6291` n `20`; unknown avg `0.8661` n `1125`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
