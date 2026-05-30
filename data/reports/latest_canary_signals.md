# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T07:52:18.913596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.0617` n `228`; crypto_major avg `0.0589` n `8`; equity avg `0.0199` n `69`; fx avg `0.0` n `6`; index avg `-0.0027` n `23`; metal avg `-0.0111` n `18`; unknown avg `-0.0476` n `421`
- 1h: commodity avg `0.0228` n `12`; crypto_alt avg `-0.0983` n `228`; crypto_major avg `0.0581` n `8`; equity avg `0.0556` n `69`; fx avg `0.0005` n `6`; index avg `0.015` n `23`; metal avg `-0.0095` n `18`; unknown avg `-0.1546` n `421`
- 4h: commodity avg `-0.1031` n `12`; crypto_alt avg `-0.175` n `228`; crypto_major avg `0.207` n `8`; equity avg `0.2322` n `69`; fx avg `0.0037` n `6`; index avg `0.1387` n `23`; metal avg `-0.0109` n `18`; unknown avg `0.0776` n `401`
- 24h: commodity avg `-0.6751` n `12`; crypto_alt avg `1.5686` n `228`; crypto_major avg `1.9472` n `8`; equity avg `0.9641` n `69`; fx avg `0.0581` n `6`; index avg `0.1372` n `23`; metal avg `-0.0871` n `18`; unknown avg `0.2716` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
