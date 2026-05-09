# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T00:52:16.787653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.1124` n `228`; crypto_major avg `-0.0609` n `8`; equity avg `-0.0306` n `65`; fx avg `-0.0028` n `5`; index avg `-0.1327` n `23`; metal avg `0.0399` n `18`; unknown avg `-0.046` n `375`
- 1h: commodity avg `-0.0807` n `12`; crypto_alt avg `0.6495` n `228`; crypto_major avg `0.244` n `8`; equity avg `0.0532` n `65`; fx avg `-0.0089` n `5`; index avg `-0.1296` n `23`; metal avg `0.0579` n `18`; unknown avg `-0.0361` n `375`
- 4h: commodity avg `-0.1899` n `12`; crypto_alt avg `1.1736` n `228`; crypto_major avg `0.3656` n `8`; equity avg `0.2151` n `65`; fx avg `-0.0402` n `5`; index avg `0.0396` n `23`; metal avg `-0.1722` n `18`; unknown avg `-0.3656` n `375`
- 24h: commodity avg `-0.8571` n `12`; crypto_alt avg `4.2857` n `228`; crypto_major avg `1.9647` n `8`; equity avg `3.8108` n `65`; fx avg `0.1014` n `5`; index avg `1.3123` n `23`; metal avg `0.7515` n `18`; unknown avg `1.0353` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
