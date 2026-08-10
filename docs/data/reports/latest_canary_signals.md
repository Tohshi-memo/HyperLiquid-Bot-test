# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T22:52:31.416037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `0.0172` n `230`; crypto_major avg `0.0797` n `8`; equity avg `-0.0009` n `113`; fx avg `0.0029` n `6`; index avg `0.0076` n `25`; metal avg `0.03` n `20`; unknown avg `-0.0563` n `785`
- 1h: commodity avg `-0.0467` n `12`; crypto_alt avg `0.0027` n `230`; crypto_major avg `-0.0903` n `8`; equity avg `-0.0529` n `113`; fx avg `0.0082` n `6`; index avg `-0.0134` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.0763` n `785`
- 4h: commodity avg `-0.0357` n `12`; crypto_alt avg `-0.3457` n `230`; crypto_major avg `0.1326` n `8`; equity avg `-0.4778` n `113`; fx avg `-0.0013` n `6`; index avg `-0.0338` n `25`; metal avg `0.1169` n `20`; unknown avg `2.9037` n `785`
- 24h: commodity avg `0.8242` n `12`; crypto_alt avg `-0.9591` n `230`; crypto_major avg `-0.8209` n `8`; equity avg `-1.6628` n `113`; fx avg `0.2618` n `6`; index avg `-0.0534` n `25`; metal avg `0.3792` n `20`; unknown avg `103.6421` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1887`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
