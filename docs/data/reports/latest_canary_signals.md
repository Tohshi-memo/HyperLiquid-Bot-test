# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T01:22:29.437089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.2152` n `12`; crypto_alt avg `0.0587` n `228`; crypto_major avg `0.0134` n `8`; equity avg `-0.0424` n `74`; fx avg `0.0264` n `6`; index avg `0.0669` n `23`; metal avg `0.236` n `18`; unknown avg `-0.2926` n `645`
- 1h: commodity avg `-0.1348` n `12`; crypto_alt avg `-0.5094` n `228`; crypto_major avg `-0.5601` n `8`; equity avg `-0.201` n `74`; fx avg `0.0601` n `6`; index avg `0.053` n `23`; metal avg `-0.0223` n `18`; unknown avg `0.2642` n `645`
- 4h: commodity avg `-0.3861` n `12`; crypto_alt avg `1.2544` n `228`; crypto_major avg `1.4999` n `8`; equity avg `1.0174` n `74`; fx avg `0.0532` n `6`; index avg `0.5386` n `23`; metal avg `1.7143` n `18`; unknown avg `1.1336` n `637`
- 24h: commodity avg `-1.0593` n `12`; crypto_alt avg `1.4022` n `228`; crypto_major avg `1.6295` n `8`; equity avg `1.4717` n `74`; fx avg `0.01` n `6`; index avg `0.7172` n `23`; metal avg `1.85` n `18`; unknown avg `1.6758` n `585`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
