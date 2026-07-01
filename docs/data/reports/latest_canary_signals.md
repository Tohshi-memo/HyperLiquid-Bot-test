# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T23:48:56.603235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.1198` n `228`; crypto_major avg `-0.1524` n `8`; equity avg `-0.0569` n `88`; fx avg `-0.0101` n `6`; index avg `-0.0474` n `25`; metal avg `-0.0513` n `20`; unknown avg `-0.0456` n `763`
- 1h: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.8014` n `228`; crypto_major avg `-0.6532` n `8`; equity avg `-0.3817` n `88`; fx avg `-0.0083` n `6`; index avg `-0.0817` n `25`; metal avg `-0.1094` n `20`; unknown avg `140.9414` n `763`
- 4h: commodity avg `-0.0056` n `12`; crypto_alt avg `0.0528` n `228`; crypto_major avg `-0.3348` n `8`; equity avg `-0.3916` n `88`; fx avg `0.0342` n `6`; index avg `-0.091` n `25`; metal avg `-0.0495` n `20`; unknown avg `142.9706` n `763`
- 24h: commodity avg `-0.6301` n `12`; crypto_alt avg `1.6097` n `228`; crypto_major avg `1.0754` n `8`; equity avg `-1.997` n `88`; fx avg `0.0278` n `6`; index avg `-0.58` n `25`; metal avg `0.2611` n `20`; unknown avg `147.7574` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
