# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T01:07:20.658377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1231` n `12`; crypto_alt avg `0.1635` n `228`; crypto_major avg `0.2059` n `8`; equity avg `0.0234` n `67`; fx avg `-0.0002` n `6`; index avg `0.0488` n `23`; metal avg `-0.0096` n `18`; unknown avg `0.0408` n `396`
- 1h: commodity avg `0.3717` n `12`; crypto_alt avg `0.235` n `228`; crypto_major avg `0.4962` n `8`; equity avg `0.1219` n `67`; fx avg `-0.001` n `6`; index avg `0.0829` n `23`; metal avg `0.0443` n `18`; unknown avg `-0.1759` n `396`
- 4h: commodity avg `0.147` n `12`; crypto_alt avg `-0.7453` n `228`; crypto_major avg `-0.2692` n `8`; equity avg `0.3342` n `67`; fx avg `0.0337` n `6`; index avg `0.2721` n `23`; metal avg `0.038` n `18`; unknown avg `-0.0364` n `396`
- 24h: commodity avg `-2.7664` n `12`; crypto_alt avg `2.6692` n `228`; crypto_major avg `2.5303` n `8`; equity avg `2.1734` n `67`; fx avg `0.049` n `6`; index avg `1.0886` n `23`; metal avg `1.0326` n `18`; unknown avg `1.3682` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
