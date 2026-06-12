# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T11:52:30.300762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1934` n `12`; crypto_alt avg `0.0726` n `228`; crypto_major avg `0.1139` n `8`; equity avg `0.0872` n `74`; fx avg `0.0014` n `6`; index avg `0.0585` n `23`; metal avg `0.2251` n `18`; unknown avg `0.0304` n `643`
- 1h: commodity avg `0.0934` n `12`; crypto_alt avg `-0.1625` n `228`; crypto_major avg `0.1172` n `8`; equity avg `0.2892` n `74`; fx avg `-0.0188` n `6`; index avg `0.1701` n `23`; metal avg `0.0151` n `18`; unknown avg `0.1138` n `643`
- 4h: commodity avg `-0.2857` n `12`; crypto_alt avg `1.1712` n `228`; crypto_major avg `1.4119` n `8`; equity avg `0.9783` n `74`; fx avg `0.0047` n `6`; index avg `0.5318` n `23`; metal avg `0.8803` n `18`; unknown avg `0.1599` n `643`
- 24h: commodity avg `-2.0632` n `12`; crypto_alt avg `1.3842` n `228`; crypto_major avg `1.4073` n `8`; equity avg `2.8155` n `74`; fx avg `0.0132` n `6`; index avg `1.6672` n `23`; metal avg `3.2376` n `18`; unknown avg `1.0907` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
