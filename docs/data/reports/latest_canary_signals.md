# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T15:37:22.528754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5145` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0638` n `12`; crypto_alt avg `-0.0715` n `228`; crypto_major avg `-0.2264` n `8`; equity avg `-0.0231` n `66`; fx avg `0.0155` n `6`; index avg `-0.0752` n `23`; metal avg `-0.1792` n `18`; unknown avg `0.3493` n `384`
- 1h: commodity avg `-0.5774` n `12`; crypto_alt avg `0.515` n `228`; crypto_major avg `0.3908` n `8`; equity avg `0.5549` n `66`; fx avg `-0.0041` n `6`; index avg `0.1312` n `23`; metal avg `0.2318` n `18`; unknown avg `0.1242` n `384`
- 4h: commodity avg `-1.6105` n `12`; crypto_alt avg `1.3665` n `228`; crypto_major avg `0.904` n `8`; equity avg `0.7258` n `66`; fx avg `-0.0346` n `6`; index avg `0.6471` n `23`; metal avg `0.4692` n `18`; unknown avg `1.2098` n `384`
- 24h: commodity avg `-1.933` n `12`; crypto_alt avg `2.6907` n `228`; crypto_major avg `1.7479` n `8`; equity avg `2.3512` n `66`; fx avg `-0.0821` n `6`; index avg `1.3996` n `23`; metal avg `1.1878` n `18`; unknown avg `1.4724` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
