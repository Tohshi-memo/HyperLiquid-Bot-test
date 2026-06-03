# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T15:52:31.230372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0549` n `12`; crypto_alt avg `-0.0464` n `228`; crypto_major avg `-0.1197` n `8`; equity avg `-0.1262` n `73`; fx avg `-0.0096` n `6`; index avg `-0.0399` n `23`; metal avg `-0.0758` n `18`; unknown avg `0.8535` n `419`
- 1h: commodity avg `0.1798` n `12`; crypto_alt avg `-0.5484` n `228`; crypto_major avg `-0.5382` n `8`; equity avg `-0.7459` n `73`; fx avg `0.0181` n `6`; index avg `-0.2562` n `23`; metal avg `-0.4301` n `18`; unknown avg `1.0438` n `419`
- 4h: commodity avg `-0.1895` n `12`; crypto_alt avg `0.1247` n `228`; crypto_major avg `-0.8962` n `8`; equity avg `-2.0144` n `73`; fx avg `-0.0379` n `6`; index avg `-0.6492` n `23`; metal avg `-1.1394` n `18`; unknown avg `0.9963` n `419`
- 24h: commodity avg `1.068` n `12`; crypto_alt avg `2.5211` n `228`; crypto_major avg `-1.663` n `8`; equity avg `-1.7272` n `72`; fx avg `0.0205` n `6`; index avg `-0.291` n `23`; metal avg `-2.2241` n `18`; unknown avg `1.6283` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
