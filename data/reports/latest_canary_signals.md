# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T08:07:18.032649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.047` n `12`; crypto_alt avg `0.0614` n `228`; crypto_major avg `0.0546` n `8`; equity avg `-0.0189` n `69`; fx avg `-0.0001` n `6`; index avg `-0.0023` n `23`; metal avg `-0.0027` n `18`; unknown avg `-0.0228` n `421`
- 1h: commodity avg `-0.0266` n `12`; crypto_alt avg `0.14` n `228`; crypto_major avg `0.1494` n `8`; equity avg `0.0363` n `69`; fx avg `0.0005` n `6`; index avg `0.0468` n `23`; metal avg `-0.0142` n `18`; unknown avg `-0.0241` n `421`
- 4h: commodity avg `-0.2168` n `12`; crypto_alt avg `-0.0428` n `228`; crypto_major avg `0.3174` n `8`; equity avg `0.2252` n `69`; fx avg `0.0041` n `6`; index avg `0.1377` n `23`; metal avg `0.0367` n `18`; unknown avg `-0.1156` n `401`
- 24h: commodity avg `-0.8845` n `12`; crypto_alt avg `1.3932` n `228`; crypto_major avg `1.7174` n `8`; equity avg `0.9226` n `69`; fx avg `0.0686` n `6`; index avg `0.1634` n `23`; metal avg `0.0753` n `18`; unknown avg `0.1852` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
