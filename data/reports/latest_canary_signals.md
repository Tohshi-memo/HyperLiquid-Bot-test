# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T13:52:27.833102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0879` n `12`; crypto_alt avg `-1.1177` n `228`; crypto_major avg `-1.5219` n `8`; equity avg `-0.9508` n `74`; fx avg `-0.0449` n `6`; index avg `-0.5364` n `23`; metal avg `-0.1051` n `18`; unknown avg `0.5895` n `424`
- 1h: commodity avg `-0.2105` n `12`; crypto_alt avg `0.073` n `228`; crypto_major avg `-0.6451` n `8`; equity avg `-1.9328` n `74`; fx avg `-0.027` n `6`; index avg `-1.1539` n `23`; metal avg `-1.1521` n `18`; unknown avg `1.1858` n `424`
- 4h: commodity avg `-0.501` n `12`; crypto_alt avg `-1.5108` n `228`; crypto_major avg `-1.7528` n `8`; equity avg `-2.4393` n `74`; fx avg `-0.0382` n `6`; index avg `-1.4274` n `23`; metal avg `-1.5706` n `18`; unknown avg `2.1893` n `424`
- 24h: commodity avg `-0.6797` n `12`; crypto_alt avg `-6.4415` n `228`; crypto_major avg `-5.185` n `8`; equity avg `-3.3374` n `74`; fx avg `0.0556` n `6`; index avg `-1.5484` n `23`; metal avg `-2.7381` n `18`; unknown avg `0.9832` n `404`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
