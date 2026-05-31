# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T06:52:17.956340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0235` n `12`; crypto_alt avg `0.0672` n `228`; crypto_major avg `-0.098` n `8`; equity avg `0.032` n `69`; fx avg `0.0102` n `6`; index avg `0.0071` n `23`; metal avg `0.018` n `18`; unknown avg `-0.2232` n `421`
- 1h: commodity avg `-0.0679` n `12`; crypto_alt avg `0.0382` n `228`; crypto_major avg `-0.2585` n `8`; equity avg `0.1108` n `69`; fx avg `0.0217` n `6`; index avg `0.0021` n `23`; metal avg `-0.0072` n `18`; unknown avg `-0.0379` n `401`
- 4h: commodity avg `0.0068` n `12`; crypto_alt avg `0.3177` n `228`; crypto_major avg `-0.0045` n `8`; equity avg `0.2677` n `69`; fx avg `0.0216` n `6`; index avg `0.0209` n `23`; metal avg `0.0286` n `18`; unknown avg `-0.1393` n `401`
- 24h: commodity avg `0.0755` n `12`; crypto_alt avg `0.6157` n `228`; crypto_major avg `2.0707` n `8`; equity avg `1.0453` n `69`; fx avg `0.063` n `6`; index avg `-0.033` n `23`; metal avg `-0.0213` n `18`; unknown avg `0.4178` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
