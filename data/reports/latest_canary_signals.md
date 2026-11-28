# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T22:52:24.403981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0107` n `13`; crypto_alt avg `-0.1596` n `239`; crypto_major avg `-0.1392` n `8`; equity avg `-0.02` n `168`; fx avg `0.001` n `6`; index avg `0.0109` n `27`; metal avg `-0.0177` n `20`; unknown avg `4.1192` n `1254`
- 1h: commodity avg `0.0042` n `13`; crypto_alt avg `0.2446` n `239`; crypto_major avg `0.2641` n `8`; equity avg `0.0531` n `168`; fx avg `-0.0043` n `6`; index avg `0.022` n `27`; metal avg `0.0` n `20`; unknown avg `2.0556` n `1238`
- 4h: commodity avg `0.1784` n `13`; crypto_alt avg `-0.1469` n `239`; crypto_major avg `-0.0007` n `8`; equity avg `0.1103` n `168`; fx avg `0.0068` n `6`; index avg `0.0364` n `27`; metal avg `0.0181` n `20`; unknown avg `5.7346` n `1172`
- 24h: commodity avg `0.0975` n `13`; crypto_alt avg `-3.2218` n `239`; crypto_major avg `-0.8775` n `8`; equity avg `0.0442` n `168`; fx avg `-0.0024` n `6`; index avg `0.0125` n `27`; metal avg `0.0126` n `20`; unknown avg `4.3865` n `1075`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
