# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T12:22:18.753155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1579` n `12`; crypto_alt avg `-0.103` n `228`; crypto_major avg `-0.1568` n `8`; equity avg `0.0354` n `66`; fx avg `-0.003` n `6`; index avg `0.0299` n `23`; metal avg `-0.1624` n `18`; unknown avg `-0.1789` n `384`
- 1h: commodity avg `-0.3031` n `12`; crypto_alt avg `-0.1916` n `228`; crypto_major avg `-0.1657` n `8`; equity avg `0.061` n `66`; fx avg `0.0244` n `6`; index avg `0.0574` n `23`; metal avg `-0.1487` n `18`; unknown avg `1.3773` n `384`
- 4h: commodity avg `-0.4696` n `12`; crypto_alt avg `-0.0949` n `228`; crypto_major avg `0.2345` n `8`; equity avg `0.3895` n `66`; fx avg `0.0273` n `6`; index avg `0.2087` n `23`; metal avg `0.0833` n `18`; unknown avg `-0.2468` n `384`
- 24h: commodity avg `-0.5371` n `12`; crypto_alt avg `0.7773` n `228`; crypto_major avg `0.6889` n `8`; equity avg `1.809` n `66`; fx avg `-0.077` n `6`; index avg `0.3824` n `23`; metal avg `-0.8036` n `18`; unknown avg `0.5432` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
