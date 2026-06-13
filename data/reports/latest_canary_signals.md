# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T15:52:27.848148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.097` n `12`; crypto_alt avg `-0.0251` n `228`; crypto_major avg `-0.0479` n `8`; equity avg `-0.0064` n `74`; fx avg `-0.0005` n `6`; index avg `-0.01` n `23`; metal avg `0.1254` n `18`; unknown avg `-0.1108` n `644`
- 1h: commodity avg `0.0283` n `12`; crypto_alt avg `0.4883` n `228`; crypto_major avg `0.135` n `8`; equity avg `0.1287` n `74`; fx avg `0.0014` n `6`; index avg `0.0382` n `23`; metal avg `0.1327` n `18`; unknown avg `-2.0544` n `644`
- 4h: commodity avg `-0.1398` n `12`; crypto_alt avg `0.7272` n `228`; crypto_major avg `0.871` n `8`; equity avg `0.4086` n `74`; fx avg `-0.0106` n `6`; index avg `0.2012` n `23`; metal avg `0.1576` n `18`; unknown avg `-2.0144` n `644`
- 24h: commodity avg `-0.556` n `12`; crypto_alt avg `1.9034` n `228`; crypto_major avg `0.6641` n `8`; equity avg `0.5361` n `74`; fx avg `0.0103` n `6`; index avg `0.7249` n `23`; metal avg `0.7361` n `18`; unknown avg `-1.7403` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
