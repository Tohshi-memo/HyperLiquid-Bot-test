# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T15:15:12.224571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0511` n `12`; crypto_alt avg `0.2125` n `228`; crypto_major avg `0.173` n `8`; equity avg `0.0429` n `74`; fx avg `0.0` n `6`; index avg `0.0144` n `23`; metal avg `-0.1171` n `18`; unknown avg `-2.0657` n `644`
- 1h: commodity avg `-0.1285` n `12`; crypto_alt avg `0.5214` n `228`; crypto_major avg `0.3191` n `8`; equity avg `0.184` n `74`; fx avg `0.0014` n `6`; index avg `0.0354` n `23`; metal avg `-0.0503` n `18`; unknown avg `-1.9108` n `644`
- 4h: commodity avg `-0.1954` n `12`; crypto_alt avg `0.5498` n `228`; crypto_major avg `0.8733` n `8`; equity avg `0.3072` n `74`; fx avg `-0.0085` n `6`; index avg `0.1659` n `23`; metal avg `0.1874` n `18`; unknown avg `-1.9297` n `644`
- 24h: commodity avg `-0.4175` n `12`; crypto_alt avg `1.2388` n `228`; crypto_major avg `-0.1054` n `8`; equity avg `-0.424` n `74`; fx avg `0.029` n `6`; index avg `0.3975` n `23`; metal avg `0.4444` n `18`; unknown avg `-1.9218` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
