# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T01:07:25.654387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `12`; crypto_alt avg `-0.2` n `228`; crypto_major avg `-0.0983` n `8`; equity avg `-0.0282` n `78`; fx avg `0.008` n `6`; index avg `-0.0021` n `23`; metal avg `-0.0267` n `18`; unknown avg `-0.2483` n `687`
- 1h: commodity avg `-0.1046` n `12`; crypto_alt avg `-0.3003` n `228`; crypto_major avg `-0.3172` n `8`; equity avg `-0.0902` n `78`; fx avg `0.0068` n `6`; index avg `-0.0097` n `23`; metal avg `-0.0058` n `18`; unknown avg `46.4929` n `687`
- 4h: commodity avg `-0.0334` n `12`; crypto_alt avg `0.1426` n `228`; crypto_major avg `-0.0038` n `8`; equity avg `0.1869` n `78`; fx avg `0.0479` n `6`; index avg `0.064` n `23`; metal avg `-0.0165` n `18`; unknown avg `-0.5995` n `679`
- 24h: commodity avg `0.2665` n `12`; crypto_alt avg `-3.4887` n `228`; crypto_major avg `-4.5013` n `8`; equity avg `0.8967` n `78`; fx avg `-0.0852` n `6`; index avg `0.2717` n `23`; metal avg `-4.1162` n `18`; unknown avg `-0.7239` n `564`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
