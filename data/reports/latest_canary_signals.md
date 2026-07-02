# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T09:52:35.977050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0615` n `12`; crypto_alt avg `0.1225` n `229`; crypto_major avg `-0.0506` n `8`; equity avg `-0.0354` n `88`; fx avg `-0.0091` n `6`; index avg `-0.0169` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.1893` n `763`
- 1h: commodity avg `-0.0169` n `12`; crypto_alt avg `0.685` n `228`; crypto_major avg `0.9099` n `8`; equity avg `0.0248` n `88`; fx avg `-0.0302` n `6`; index avg `-0.0403` n `25`; metal avg `-0.0338` n `20`; unknown avg `0.0247` n `763`
- 4h: commodity avg `-0.1032` n `12`; crypto_alt avg `1.0277` n `228`; crypto_major avg `1.0434` n `8`; equity avg `-0.242` n `88`; fx avg `-0.0987` n `6`; index avg `-0.0936` n `25`; metal avg `0.1432` n `20`; unknown avg `0.6963` n `741`
- 24h: commodity avg `-0.4428` n `12`; crypto_alt avg `2.8777` n `228`; crypto_major avg `2.6302` n `8`; equity avg `-1.8455` n `88`; fx avg `-0.1145` n `6`; index avg `-0.5268` n `25`; metal avg `1.1076` n `20`; unknown avg `3.3444` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
