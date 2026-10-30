# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T05:07:32.808678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.2533` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1341` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0186` n `13`; crypto_alt avg `0.1567` n `238`; crypto_major avg `0.2374` n `8`; equity avg `-0.0733` n `156`; fx avg `-0.0015` n `6`; index avg `-0.0094` n `27`; metal avg `0.0504` n `20`; unknown avg `0.2791` n `1254`
- 1h: commodity avg `-0.0363` n `13`; crypto_alt avg `1.1871` n `238`; crypto_major avg `0.7568` n `8`; equity avg `0.4424` n `156`; fx avg `0.011` n `6`; index avg `0.0815` n `27`; metal avg `0.1095` n `20`; unknown avg `1.1791` n `1254`
- 4h: commodity avg `0.1486` n `13`; crypto_alt avg `2.3189` n `238`; crypto_major avg `2.2827` n `8`; equity avg `1.3105` n `156`; fx avg `-0.051` n `6`; index avg `0.1104` n `27`; metal avg `0.0294` n `20`; unknown avg `4.9255` n `1234`
- 24h: commodity avg `-0.0971` n `13`; crypto_alt avg `-4.0706` n `238`; crypto_major avg `-0.3549` n `8`; equity avg `-2.8005` n `155`; fx avg `0.1211` n `6`; index avg `-0.3393` n `27`; metal avg `-0.6553` n `20`; unknown avg `28.8596` n `982`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
