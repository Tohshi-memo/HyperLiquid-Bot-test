# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T09:37:25.706420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `0.0386` n `228`; crypto_major avg `0.047` n `8`; equity avg `0.0352` n `88`; fx avg `0.0145` n `6`; index avg `-0.0017` n `23`; metal avg `0.0641` n `20`; unknown avg `-0.1208` n `765`
- 1h: commodity avg `-0.0367` n `12`; crypto_alt avg `0.6087` n `228`; crypto_major avg `0.5882` n `8`; equity avg `0.1233` n `88`; fx avg `0.0209` n `6`; index avg `-0.0023` n `23`; metal avg `0.118` n `20`; unknown avg `0.0933` n `765`
- 4h: commodity avg `-0.3001` n `12`; crypto_alt avg `-0.2397` n `228`; crypto_major avg `-0.5815` n `8`; equity avg `-0.1775` n `88`; fx avg `0.0536` n `6`; index avg `-0.0404` n `23`; metal avg `0.0863` n `20`; unknown avg `-0.0551` n `743`
- 24h: commodity avg `-0.4554` n `12`; crypto_alt avg `-0.0383` n `228`; crypto_major avg `-0.268` n `8`; equity avg `0.6283` n `88`; fx avg `0.116` n `6`; index avg `0.0271` n `23`; metal avg `-0.5273` n `20`; unknown avg `0.12` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
