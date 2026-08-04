# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T08:07:56.753229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.0328` n `230`; crypto_major avg `-0.0218` n `8`; equity avg `0.3125` n `107`; fx avg `-0.0031` n `6`; index avg `0.0187` n `25`; metal avg `0.0628` n `20`; unknown avg `0.1129` n `781`
- 1h: commodity avg `0.0713` n `12`; crypto_alt avg `0.317` n `230`; crypto_major avg `0.2505` n `8`; equity avg `0.407` n `107`; fx avg `0.0329` n `6`; index avg `0.0376` n `25`; metal avg `0.1092` n `20`; unknown avg `1.0748` n `781`
- 4h: commodity avg `-0.073` n `12`; crypto_alt avg `0.0023` n `230`; crypto_major avg `0.1459` n `8`; equity avg `1.2133` n `107`; fx avg `0.0481` n `6`; index avg `0.1972` n `25`; metal avg `0.2163` n `20`; unknown avg `1.0617` n `765`
- 24h: commodity avg `0.1687` n `12`; crypto_alt avg `1.3721` n `230`; crypto_major avg `1.6157` n `8`; equity avg `3.4566` n `107`; fx avg `0.1078` n `6`; index avg `0.3557` n `25`; metal avg `0.2241` n `20`; unknown avg `1.2978` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
