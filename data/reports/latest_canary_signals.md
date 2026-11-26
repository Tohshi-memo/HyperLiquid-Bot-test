# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T19:52:26.129150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `-0.0395` n `239`; crypto_major avg `-0.0442` n `8`; equity avg `-0.0421` n `168`; fx avg `0.0023` n `6`; index avg `-0.0035` n `27`; metal avg `0.0154` n `20`; unknown avg `-0.4393` n `1263`
- 1h: commodity avg `0.0182` n `13`; crypto_alt avg `0.1787` n `239`; crypto_major avg `0.314` n `8`; equity avg `0.1555` n `168`; fx avg `-0.0047` n `6`; index avg `0.012` n `27`; metal avg `0.0123` n `20`; unknown avg `24.2344` n `1259`
- 4h: commodity avg `-0.0378` n `13`; crypto_alt avg `0.9076` n `239`; crypto_major avg `0.9423` n `8`; equity avg `0.1665` n `168`; fx avg `-0.0133` n `6`; index avg `0.0139` n `27`; metal avg `-0.0563` n `20`; unknown avg `49.1367` n `1199`
- 24h: commodity avg `0.2073` n `13`; crypto_alt avg `1.8111` n `239`; crypto_major avg `1.1441` n `8`; equity avg `1.3226` n `168`; fx avg `-0.0336` n `6`; index avg `0.0917` n `27`; metal avg `0.3003` n `20`; unknown avg `33.2821` n `1031`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
