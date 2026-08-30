# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T10:37:30.372794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.1137` n `231`; crypto_major avg `0.0363` n `8`; equity avg `-0.003` n `128`; fx avg `-0.0019` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.0836` n `793`
- 1h: commodity avg `0.0015` n `12`; crypto_alt avg `0.4993` n `231`; crypto_major avg `0.1206` n `8`; equity avg `-0.0057` n `128`; fx avg `-0.0` n `6`; index avg `-0.0012` n `26`; metal avg `0.0017` n `20`; unknown avg `-0.1302` n `793`
- 4h: commodity avg `-0.0272` n `12`; crypto_alt avg `0.209` n `231`; crypto_major avg `-0.2137` n `8`; equity avg `-0.0269` n `128`; fx avg `-0.0054` n `6`; index avg `0.0009` n `26`; metal avg `-0.0072` n `20`; unknown avg `-0.2348` n `791`
- 24h: commodity avg `-0.0244` n `12`; crypto_alt avg `1.4363` n `231`; crypto_major avg `0.8145` n `8`; equity avg `0.2497` n `128`; fx avg `0.0109` n `6`; index avg `0.071` n `26`; metal avg `0.0956` n `20`; unknown avg `0.7204` n `716`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
