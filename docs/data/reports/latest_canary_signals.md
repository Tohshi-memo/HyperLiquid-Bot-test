# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T11:22:25.681167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0218` n `12`; crypto_alt avg `0.0331` n `230`; crypto_major avg `-0.0298` n `8`; equity avg `-0.0078` n `93`; fx avg `0.002` n `6`; index avg `-0.0067` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.0024` n `767`
- 1h: commodity avg `-0.0954` n `12`; crypto_alt avg `-0.0401` n `230`; crypto_major avg `-0.0532` n `8`; equity avg `-0.0788` n `93`; fx avg `0.0052` n `6`; index avg `-0.0132` n `25`; metal avg `-0.0772` n `20`; unknown avg `-0.1084` n `767`
- 4h: commodity avg `-0.0861` n `12`; crypto_alt avg `0.2526` n `230`; crypto_major avg `0.1995` n `8`; equity avg `-0.2327` n `93`; fx avg `-0.0102` n `6`; index avg `-0.0579` n `25`; metal avg `-0.1432` n `20`; unknown avg `-0.1165` n `765`
- 24h: commodity avg `-0.1103` n `12`; crypto_alt avg `1.6561` n `230`; crypto_major avg `2.9982` n `8`; equity avg `1.2855` n `92`; fx avg `0.0173` n `6`; index avg `0.3537` n `25`; metal avg `0.2165` n `20`; unknown avg `0.2385` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
