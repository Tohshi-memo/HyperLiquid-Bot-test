# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T21:07:32.761245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3117` n `12`; crypto_alt avg `0.8383` n `228`; crypto_major avg `0.8455` n `8`; equity avg `0.099` n `73`; fx avg `-0.0086` n `6`; index avg `0.0359` n `23`; metal avg `0.0718` n `18`; unknown avg `1.6237` n `419`
- 1h: commodity avg `0.3941` n `12`; crypto_alt avg `-0.1793` n `228`; crypto_major avg `0.1233` n `8`; equity avg `-0.6964` n `73`; fx avg `-0.0117` n `6`; index avg `-0.1859` n `23`; metal avg `-0.1037` n `18`; unknown avg `1.037` n `419`
- 4h: commodity avg `0.5037` n `12`; crypto_alt avg `-0.006` n `228`; crypto_major avg `-0.021` n `8`; equity avg `-0.658` n `73`; fx avg `0.0216` n `6`; index avg `-0.2111` n `23`; metal avg `-0.5714` n `18`; unknown avg `0.8737` n `419`
- 24h: commodity avg `1.3828` n `12`; crypto_alt avg `0.0809` n `228`; crypto_major avg `-2.2118` n `8`; equity avg `-3.221` n `72`; fx avg `0.0636` n `6`; index avg `-0.6564` n `23`; metal avg `-2.3303` n `18`; unknown avg `0.9106` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
