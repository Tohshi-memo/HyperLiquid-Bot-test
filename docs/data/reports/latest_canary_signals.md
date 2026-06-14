# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T15:37:32.424117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0608` n `12`; crypto_alt avg `0.0254` n `228`; crypto_major avg `0.0436` n `8`; equity avg `0.0055` n `74`; fx avg `-0.0043` n `6`; index avg `0.0319` n `23`; metal avg `-0.0203` n `18`; unknown avg `0.023` n `645`
- 1h: commodity avg `-0.1649` n `12`; crypto_alt avg `0.3729` n `228`; crypto_major avg `0.3137` n `8`; equity avg `0.2522` n `74`; fx avg `-0.0223` n `6`; index avg `0.1037` n `23`; metal avg `0.029` n `18`; unknown avg `0.2345` n `645`
- 4h: commodity avg `0.2742` n `12`; crypto_alt avg `-0.9586` n `228`; crypto_major avg `-0.8658` n `8`; equity avg `-0.3189` n `74`; fx avg `-0.0302` n `6`; index avg `0.1012` n `23`; metal avg `-0.0962` n `18`; unknown avg `0.3447` n `645`
- 24h: commodity avg `-0.1476` n `12`; crypto_alt avg `-1.7162` n `228`; crypto_major avg `-0.953` n `8`; equity avg `0.3307` n `74`; fx avg `-0.0232` n `6`; index avg `0.1651` n `23`; metal avg `-0.0356` n `18`; unknown avg `1.3412` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
