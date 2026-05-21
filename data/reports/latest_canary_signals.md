# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T17:37:17.760632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.06` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.9479` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.1236` n `12`; crypto_alt avg `0.3145` n `228`; crypto_major avg `0.1459` n `8`; equity avg `-0.0354` n `67`; fx avg `0.0132` n `6`; index avg `0.0878` n `23`; metal avg `0.0216` n `18`; unknown avg `1.3933` n `386`
- 1h: commodity avg `-0.9299` n `12`; crypto_alt avg `1.258` n `228`; crypto_major avg `1.0532` n `8`; equity avg `0.8054` n `67`; fx avg `-0.0005` n `6`; index avg `0.5039` n `23`; metal avg `0.6496` n `18`; unknown avg `2.234` n `385`
- 4h: commodity avg `-1.6237` n `12`; crypto_alt avg `1.8942` n `228`; crypto_major avg `1.3242` n `8`; equity avg `1.0542` n `67`; fx avg `-0.0068` n `6`; index avg `0.534` n `23`; metal avg `1.6617` n `18`; unknown avg `2.5955` n `385`
- 24h: commodity avg `0.034` n `12`; crypto_alt avg `1.8251` n `228`; crypto_major avg `2.3722` n `8`; equity avg `1.6464` n `66`; fx avg `0.0068` n `6`; index avg `0.6388` n `23`; metal avg `0.4772` n `18`; unknown avg `7.5482` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0446`, n `668`, weak_sample_signal
