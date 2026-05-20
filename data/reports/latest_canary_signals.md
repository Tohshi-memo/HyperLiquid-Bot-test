# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T16:07:17.517887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.727` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0581` n `12`; crypto_alt avg `0.2035` n `228`; crypto_major avg `0.0973` n `8`; equity avg `-0.0162` n `66`; fx avg `0.0083` n `6`; index avg `-0.0108` n `23`; metal avg `-0.0853` n `18`; unknown avg `0.1017` n `384`
- 1h: commodity avg `-0.7007` n `12`; crypto_alt avg `0.7985` n `228`; crypto_major avg `0.3979` n `8`; equity avg `0.3945` n `66`; fx avg `0.0242` n `6`; index avg `0.1338` n `23`; metal avg `0.2335` n `18`; unknown avg `0.166` n `384`
- 4h: commodity avg `-1.6887` n `12`; crypto_alt avg `1.7207` n `228`; crypto_major avg `1.0383` n `8`; equity avg `0.729` n `66`; fx avg `-0.0071` n `6`; index avg `0.7714` n `23`; metal avg `0.6081` n `18`; unknown avg `0.6504` n `384`
- 24h: commodity avg `-2.215` n `12`; crypto_alt avg `3.1113` n `228`; crypto_major avg `2.0745` n `8`; equity avg `2.2295` n `66`; fx avg `-0.0535` n `6`; index avg `1.3776` n `23`; metal avg `1.2062` n `18`; unknown avg `1.2392` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0456`, n `668`, weak_sample_signal
