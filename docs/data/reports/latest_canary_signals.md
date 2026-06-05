# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T03:22:21.123388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0533` n `12`; crypto_alt avg `0.4653` n `228`; crypto_major avg `0.2718` n `8`; equity avg `0.0515` n `74`; fx avg `-0.0061` n `6`; index avg `0.0024` n `23`; metal avg `-0.0138` n `18`; unknown avg `0.396` n `424`
- 1h: commodity avg `-0.0391` n `12`; crypto_alt avg `-1.1436` n `228`; crypto_major avg `-0.816` n `8`; equity avg `-0.2523` n `74`; fx avg `-0.0187` n `6`; index avg `-0.1569` n `23`; metal avg `-0.315` n `18`; unknown avg `0.0432` n `424`
- 4h: commodity avg `0.1492` n `12`; crypto_alt avg `-1.7735` n `228`; crypto_major avg `-1.1064` n `8`; equity avg `-0.5971` n `74`; fx avg `0.1171` n `6`; index avg `-0.5599` n `23`; metal avg `-1.0305` n `18`; unknown avg `0.5195` n `424`
- 24h: commodity avg `-0.0037` n `12`; crypto_alt avg `-6.2103` n `228`; crypto_major avg `-4.6739` n `8`; equity avg `-1.3732` n `73`; fx avg `0.1965` n `6`; index avg `-0.4646` n `23`; metal avg `-0.7399` n `18`; unknown avg `-1.2375` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
