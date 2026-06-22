# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T04:37:30.566237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.0034` n `228`; crypto_major avg `0.005` n `8`; equity avg `-0.0957` n `79`; fx avg `0.0029` n `6`; index avg `-0.0381` n `23`; metal avg `-0.0029` n `18`; unknown avg `-0.0567` n `701`
- 1h: commodity avg `-0.0719` n `12`; crypto_alt avg `-0.3228` n `228`; crypto_major avg `-0.4302` n `8`; equity avg `-0.2833` n `79`; fx avg `-0.0185` n `6`; index avg `-0.0807` n `23`; metal avg `-0.0248` n `18`; unknown avg `-0.2437` n `701`
- 4h: commodity avg `-0.3836` n `12`; crypto_alt avg `0.0165` n `228`; crypto_major avg `-0.3017` n `8`; equity avg `0.1734` n `79`; fx avg `0.0902` n `6`; index avg `0.0037` n `23`; metal avg `0.0126` n `18`; unknown avg `-0.5069` n `685`
- 24h: commodity avg `-0.3496` n `12`; crypto_alt avg `-0.2385` n `228`; crypto_major avg `-1.1897` n `8`; equity avg `-0.6887` n `79`; fx avg `0.0084` n `6`; index avg `-0.0708` n `23`; metal avg `0.0831` n `18`; unknown avg `-0.2894` n `629`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
