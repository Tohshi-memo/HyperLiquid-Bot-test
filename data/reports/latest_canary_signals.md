# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T11:37:22.206638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1766` n `12`; crypto_alt avg `-0.5481` n `228`; crypto_major avg `-0.6265` n `8`; equity avg `-0.0374` n `74`; fx avg `0.0138` n `6`; index avg `-0.013` n `23`; metal avg `0.0733` n `18`; unknown avg `-0.3613` n `424`
- 1h: commodity avg `0.0321` n `12`; crypto_alt avg `-0.562` n `228`; crypto_major avg `-0.0906` n `8`; equity avg `-0.2218` n `74`; fx avg `0.0161` n `6`; index avg `-0.0697` n `23`; metal avg `0.0395` n `18`; unknown avg `-0.2438` n `424`
- 4h: commodity avg `0.0539` n `12`; crypto_alt avg `-0.2336` n `228`; crypto_major avg `-0.0835` n `8`; equity avg `0.4926` n `74`; fx avg `0.0662` n `6`; index avg `0.1741` n `23`; metal avg `0.1867` n `18`; unknown avg `-0.0885` n `424`
- 24h: commodity avg `-0.2362` n `12`; crypto_alt avg `-3.6156` n `228`; crypto_major avg `-2.2778` n `8`; equity avg `0.0651` n `73`; fx avg `0.13` n `6`; index avg `0.1798` n `23`; metal avg `-0.5827` n `18`; unknown avg `0.0332` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
