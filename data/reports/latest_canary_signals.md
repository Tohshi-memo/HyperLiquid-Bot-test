# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T15:52:25.620774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.5944` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.0284` n `230`; crypto_major avg `-0.0612` n `8`; equity avg `0.0078` n `113`; fx avg `-0.0088` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0395` n `20`; unknown avg `0.002` n `786`
- 1h: commodity avg `0.0497` n `12`; crypto_alt avg `0.1169` n `230`; crypto_major avg `0.2315` n `8`; equity avg `0.0951` n `113`; fx avg `0.0076` n `6`; index avg `-0.031` n `25`; metal avg `-0.08` n `20`; unknown avg `0.0327` n `786`
- 4h: commodity avg `-0.0453` n `12`; crypto_alt avg `-0.5314` n `230`; crypto_major avg `-0.6666` n `8`; equity avg `0.9278` n `113`; fx avg `-0.0145` n `6`; index avg `0.078` n `25`; metal avg `-0.2606` n `20`; unknown avg `0.1325` n `786`
- 24h: commodity avg `0.1047` n `12`; crypto_alt avg `0.2027` n `230`; crypto_major avg `1.3625` n `8`; equity avg `3.2118` n `113`; fx avg `0.0327` n `6`; index avg `0.336` n `25`; metal avg `0.2448` n `20`; unknown avg `0.0834` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2048`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1955`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
