# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T18:37:20.348404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0839` n `12`; crypto_alt avg `-0.0862` n `228`; crypto_major avg `-0.1728` n `8`; equity avg `-0.0096` n `66`; fx avg `0.0166` n `6`; index avg `-0.0078` n `23`; metal avg `0.1545` n `18`; unknown avg `-0.1864` n `384`
- 1h: commodity avg `0.3523` n `12`; crypto_alt avg `-0.39` n `228`; crypto_major avg `-0.3915` n `8`; equity avg `0.0679` n `66`; fx avg `0.0162` n `6`; index avg `-0.0114` n `23`; metal avg `0.1646` n `18`; unknown avg `0.1332` n `384`
- 4h: commodity avg `-0.8654` n `12`; crypto_alt avg `0.6864` n `228`; crypto_major avg `0.4336` n `8`; equity avg `0.697` n `66`; fx avg `0.019` n `6`; index avg `0.2256` n `23`; metal avg `0.4446` n `18`; unknown avg `0.4608` n `384`
- 24h: commodity avg `-2.6926` n `12`; crypto_alt avg `2.4713` n `228`; crypto_major avg `1.6542` n `8`; equity avg `1.167` n `66`; fx avg `-0.0254` n `6`; index avg `0.7069` n `23`; metal avg `1.4544` n `18`; unknown avg `1.0274` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0444`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
