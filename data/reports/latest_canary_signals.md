# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T04:52:27.146014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `-0.0082` n `228`; crypto_major avg `-0.126` n `8`; equity avg `0.0341` n `88`; fx avg `0.0158` n `6`; index avg `-0.0119` n `23`; metal avg `-0.0791` n `20`; unknown avg `1.3577` n `765`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.0563` n `228`; crypto_major avg `-0.0429` n `8`; equity avg `0.3346` n `88`; fx avg `-0.0003` n `6`; index avg `0.1063` n `23`; metal avg `0.242` n `20`; unknown avg `8.6562` n `765`
- 4h: commodity avg `-0.0095` n `12`; crypto_alt avg `-0.0213` n `228`; crypto_major avg `-0.3597` n `8`; equity avg `0.8761` n `88`; fx avg `-0.0363` n `6`; index avg `0.2781` n `23`; metal avg `0.0563` n `20`; unknown avg `11.7682` n `763`
- 24h: commodity avg `-0.246` n `12`; crypto_alt avg `0.3338` n `228`; crypto_major avg `1.3952` n `8`; equity avg `2.6801` n `88`; fx avg `0.1317` n `6`; index avg `0.4865` n `23`; metal avg `-0.3395` n `20`; unknown avg `14.1013` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
