# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T05:52:29.986726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.3894` n `234`; crypto_major avg `-0.1101` n `8`; equity avg `-0.0252` n `140`; fx avg `0.0` n `6`; index avg `-0.0251` n `26`; metal avg `-0.0049` n `20`; unknown avg `2.566` n `942`
- 1h: commodity avg `0.008` n `12`; crypto_alt avg `-0.137` n `234`; crypto_major avg `0.3427` n `8`; equity avg `-0.0039` n `140`; fx avg `0.0202` n `6`; index avg `-0.0344` n `26`; metal avg `0.0046` n `20`; unknown avg `5.997` n `940`
- 4h: commodity avg `-0.0282` n `12`; crypto_alt avg `-0.5315` n `234`; crypto_major avg `-0.0849` n `8`; equity avg `-0.1039` n `140`; fx avg `0.0101` n `6`; index avg `-0.0318` n `26`; metal avg `-0.0108` n `20`; unknown avg `17.0497` n `914`
- 24h: commodity avg `0.1355` n `12`; crypto_alt avg `3.5887` n `234`; crypto_major avg `4.7025` n `8`; equity avg `0.4576` n `140`; fx avg `0.0849` n `6`; index avg `-0.0211` n `26`; metal avg `-0.029` n `20`; unknown avg `2.664` n `767`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
