# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T13:37:29.289625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1072` n `12`; crypto_alt avg `-0.1093` n `228`; crypto_major avg `-0.1496` n `8`; equity avg `-0.0511` n `78`; fx avg `0.104` n `6`; index avg `0.016` n `23`; metal avg `-0.007` n `18`; unknown avg `-0.0023` n `702`
- 1h: commodity avg `-0.0937` n `12`; crypto_alt avg `0.2669` n `228`; crypto_major avg `0.1703` n `8`; equity avg `0.0079` n `78`; fx avg `-0.0164` n `6`; index avg `0.0106` n `23`; metal avg `0.0302` n `18`; unknown avg `0.155` n `702`
- 4h: commodity avg `0.0443` n `12`; crypto_alt avg `0.1066` n `228`; crypto_major avg `-0.3569` n `8`; equity avg `-0.0875` n `78`; fx avg `0.0264` n `6`; index avg `0.0024` n `23`; metal avg `-0.0468` n `18`; unknown avg `-0.0247` n `702`
- 24h: commodity avg `-0.0287` n `12`; crypto_alt avg `2.122` n `228`; crypto_major avg `0.3041` n `8`; equity avg `0.559` n `78`; fx avg `0.0569` n `6`; index avg `0.0457` n `23`; metal avg `-0.0393` n `18`; unknown avg `0.7491` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
