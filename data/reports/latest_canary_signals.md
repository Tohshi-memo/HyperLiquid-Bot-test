# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T06:37:23.828425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2144` n `12`; crypto_alt avg `-0.0804` n `228`; crypto_major avg `-0.1782` n `8`; equity avg `0.0866` n `74`; fx avg `0.0083` n `6`; index avg `0.1149` n `23`; metal avg `-0.0187` n `18`; unknown avg `0.1` n `547`
- 1h: commodity avg `-0.024` n `12`; crypto_alt avg `0.2059` n `228`; crypto_major avg `-0.0185` n `8`; equity avg `0.609` n `74`; fx avg `0.0277` n `6`; index avg `0.2721` n `23`; metal avg `0.658` n `18`; unknown avg `-0.4235` n `537`
- 4h: commodity avg `-0.5152` n `12`; crypto_alt avg `-0.3103` n `228`; crypto_major avg `-0.5034` n `8`; equity avg `0.0604` n `74`; fx avg `0.0809` n `6`; index avg `-0.235` n `23`; metal avg `0.513` n `18`; unknown avg `-0.5819` n `537`
- 24h: commodity avg `-0.9188` n `12`; crypto_alt avg `-2.0698` n `228`; crypto_major avg `-4.3896` n `8`; equity avg `-3.6336` n `74`; fx avg `0.2037` n `6`; index avg `-1.716` n `23`; metal avg `-2.5406` n `18`; unknown avg `0.0002` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
