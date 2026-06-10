# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T12:52:26.824756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0921` n `12`; crypto_alt avg `-0.244` n `228`; crypto_major avg `-0.1967` n `8`; equity avg `-0.2081` n `74`; fx avg `0.0109` n `6`; index avg `-0.05` n `23`; metal avg `-0.2392` n `18`; unknown avg `-0.0006` n `547`
- 1h: commodity avg `-0.0771` n `12`; crypto_alt avg `1.2073` n `228`; crypto_major avg `0.858` n `8`; equity avg `1.242` n `74`; fx avg `0.0021` n `6`; index avg `0.5833` n `23`; metal avg `0.1384` n `18`; unknown avg `0.1296` n `547`
- 4h: commodity avg `1.3115` n `12`; crypto_alt avg `0.5024` n `228`; crypto_major avg `0.7849` n `8`; equity avg `0.6734` n `74`; fx avg `-0.0025` n `6`; index avg `0.3928` n `23`; metal avg `0.0832` n `18`; unknown avg `0.2033` n `547`
- 24h: commodity avg `0.4386` n `12`; crypto_alt avg `-1.1966` n `228`; crypto_major avg `-2.797` n `8`; equity avg `-3.6631` n `74`; fx avg `-0.112` n `6`; index avg `-2.0271` n `23`; metal avg `-3.6276` n `18`; unknown avg `1.1246` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
