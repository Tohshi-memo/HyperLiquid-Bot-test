# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T10:37:33.937306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `-0.1008` n `234`; crypto_major avg `-0.0159` n `8`; equity avg `0.007` n `140`; fx avg `0.0042` n `6`; index avg `0.0017` n `26`; metal avg `-0.0036` n `20`; unknown avg `1.5701` n `943`
- 1h: commodity avg `0.0416` n `12`; crypto_alt avg `-0.8235` n `234`; crypto_major avg `-0.3749` n `8`; equity avg `-0.0431` n `140`; fx avg `0.0039` n `6`; index avg `0.0131` n `26`; metal avg `-0.0267` n `20`; unknown avg `-0.0084` n `941`
- 4h: commodity avg `0.045` n `12`; crypto_alt avg `-0.9827` n `234`; crypto_major avg `-0.283` n `8`; equity avg `-0.0465` n `140`; fx avg `0.006` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0086` n `20`; unknown avg `0.8678` n `935`
- 24h: commodity avg `0.2725` n `12`; crypto_alt avg `-2.2974` n `234`; crypto_major avg `-2.2062` n `8`; equity avg `-0.282` n `140`; fx avg `-0.0681` n `6`; index avg `-0.0479` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.5046` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
