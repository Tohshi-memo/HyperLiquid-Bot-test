# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T00:52:32.384885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0497` n `12`; crypto_alt avg `-0.3839` n `228`; crypto_major avg `-0.3049` n `8`; equity avg `-0.0769` n `78`; fx avg `-0.0142` n `6`; index avg `-0.0099` n `23`; metal avg `0.0009` n `18`; unknown avg `0.3452` n `687`
- 1h: commodity avg `-0.151` n `12`; crypto_alt avg `0.2463` n `228`; crypto_major avg `0.0635` n `8`; equity avg `0.0349` n `78`; fx avg `-0.0041` n `6`; index avg `-0.0138` n `23`; metal avg `0.0201` n `18`; unknown avg `-0.2947` n `687`
- 4h: commodity avg `-0.0926` n `12`; crypto_alt avg `0.3532` n `228`; crypto_major avg `0.102` n `8`; equity avg `0.2102` n `78`; fx avg `0.0016` n `6`; index avg `0.0587` n `23`; metal avg `0.0189` n `18`; unknown avg `-0.4204` n `679`
- 24h: commodity avg `0.2302` n `12`; crypto_alt avg `-3.2993` n `228`; crypto_major avg `-4.4081` n `8`; equity avg `0.9253` n `78`; fx avg `-0.0932` n `6`; index avg `0.2739` n `23`; metal avg `-4.0913` n `18`; unknown avg `-0.4125` n `564`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
