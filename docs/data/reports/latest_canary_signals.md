# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T17:37:39.344700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0594` n `12`; crypto_alt avg `0.6583` n `228`; crypto_major avg `0.6681` n `8`; equity avg `0.3037` n `73`; fx avg `-0.0225` n `6`; index avg `0.0099` n `23`; metal avg `-0.066` n `18`; unknown avg `0.2776` n `419`
- 1h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.895` n `228`; crypto_major avg `0.8075` n `8`; equity avg `0.3131` n `73`; fx avg `-0.0327` n `6`; index avg `-0.0125` n `23`; metal avg `-0.005` n `18`; unknown avg `1.0624` n `419`
- 4h: commodity avg `0.5012` n `12`; crypto_alt avg `-0.5016` n `228`; crypto_major avg `-0.772` n `8`; equity avg `-1.0583` n `73`; fx avg `-0.0419` n `6`; index avg `-0.3304` n `23`; metal avg `-0.7487` n `18`; unknown avg `0.8569` n `419`
- 24h: commodity avg `0.8861` n `12`; crypto_alt avg `0.1708` n `228`; crypto_major avg `-2.4495` n `8`; equity avg `-1.8407` n `72`; fx avg `0.0073` n `6`; index avg `-0.1774` n `23`; metal avg `-1.8362` n `18`; unknown avg `1.0485` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
