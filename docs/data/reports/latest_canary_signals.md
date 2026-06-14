# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T14:22:29.131796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1889` n `12`; crypto_alt avg `-0.0866` n `228`; crypto_major avg `-0.1738` n `8`; equity avg `-0.1183` n `74`; fx avg `-0.0072` n `6`; index avg `-0.0402` n `23`; metal avg `-0.0432` n `18`; unknown avg `0.0363` n `645`
- 1h: commodity avg `0.3659` n `12`; crypto_alt avg `-0.0643` n `228`; crypto_major avg `-0.1414` n `8`; equity avg `-0.1887` n `74`; fx avg `-0.007` n `6`; index avg `-0.0852` n `23`; metal avg `-0.0705` n `18`; unknown avg `0.0594` n `645`
- 4h: commodity avg `0.7263` n `12`; crypto_alt avg `-0.9679` n `228`; crypto_major avg `-0.7748` n `8`; equity avg `-0.3477` n `74`; fx avg `0.0016` n `6`; index avg `0.0038` n `23`; metal avg `-0.1851` n `18`; unknown avg `0.3712` n `645`
- 24h: commodity avg `0.07` n `12`; crypto_alt avg `-0.8296` n `228`; crypto_major avg `-0.4736` n `8`; equity avg `0.48` n `74`; fx avg `-0.0008` n `6`; index avg `0.1097` n `23`; metal avg `-0.0776` n `18`; unknown avg `-1.0666` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
