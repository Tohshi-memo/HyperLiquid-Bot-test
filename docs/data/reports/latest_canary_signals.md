# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T09:52:27.241193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.0206` n `230`; crypto_major avg `-0.0569` n `8`; equity avg `-0.1176` n `112`; fx avg `0.0049` n `6`; index avg `0.0031` n `25`; metal avg `-0.0167` n `20`; unknown avg `-0.022` n `785`
- 1h: commodity avg `-0.0226` n `12`; crypto_alt avg `-0.151` n `230`; crypto_major avg `-0.2871` n `8`; equity avg `-0.1077` n `112`; fx avg `-0.0005` n `6`; index avg `-0.0171` n `25`; metal avg `-0.0159` n `20`; unknown avg `-0.0498` n `785`
- 4h: commodity avg `0.2843` n `12`; crypto_alt avg `0.0397` n `230`; crypto_major avg `-0.0528` n `8`; equity avg `0.1786` n `112`; fx avg `0.0835` n `6`; index avg `0.0268` n `25`; metal avg `-0.1791` n `20`; unknown avg `57.2269` n `753`
- 24h: commodity avg `0.4278` n `12`; crypto_alt avg `0.7602` n `230`; crypto_major avg `-0.0027` n `8`; equity avg `-0.0971` n `112`; fx avg `0.232` n `6`; index avg `0.0647` n `25`; metal avg `-0.1372` n `20`; unknown avg `56.9555` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
