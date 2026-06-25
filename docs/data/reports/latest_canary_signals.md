# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T10:37:30.427809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `-0.1632` n `228`; crypto_major avg `-0.22` n `8`; equity avg `0.0494` n `86`; fx avg `-0.0062` n `6`; index avg `0.0249` n `23`; metal avg `0.0275` n `20`; unknown avg `-0.0311` n `765`
- 1h: commodity avg `0.0009` n `12`; crypto_alt avg `-0.358` n `228`; crypto_major avg `-0.4324` n `8`; equity avg `0.1826` n `86`; fx avg `-0.0362` n `6`; index avg `0.0259` n `23`; metal avg `-0.0135` n `20`; unknown avg `-0.0046` n `765`
- 4h: commodity avg `0.1` n `12`; crypto_alt avg `-0.5995` n `228`; crypto_major avg `-0.6498` n `8`; equity avg `0.2872` n `86`; fx avg `-0.0141` n `6`; index avg `0.0069` n `23`; metal avg `0.4083` n `20`; unknown avg `0.0195` n `749`
- 24h: commodity avg `-0.2856` n `12`; crypto_alt avg `-1.1997` n `228`; crypto_major avg `-0.9976` n `8`; equity avg `0.2068` n `86`; fx avg `-0.0063` n `6`; index avg `0.5063` n `23`; metal avg `-1.1162` n `20`; unknown avg `-0.4955` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
