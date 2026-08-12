# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T10:52:25.690584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0814` n `12`; crypto_alt avg `0.1229` n `230`; crypto_major avg `0.0586` n `8`; equity avg `-0.0441` n `113`; fx avg `-0.001` n `6`; index avg `-0.023` n `25`; metal avg `-0.0382` n `20`; unknown avg `-0.0132` n `786`
- 1h: commodity avg `0.1012` n `12`; crypto_alt avg `0.0763` n `230`; crypto_major avg `0.1053` n `8`; equity avg `-0.0159` n `113`; fx avg `0.0207` n `6`; index avg `-0.0167` n `25`; metal avg `-0.0157` n `20`; unknown avg `-0.0203` n `786`
- 4h: commodity avg `0.0938` n `12`; crypto_alt avg `0.0208` n `230`; crypto_major avg `0.6746` n `8`; equity avg `0.5673` n `113`; fx avg `-0.0179` n `6`; index avg `0.0645` n `25`; metal avg `0.0963` n `20`; unknown avg `0.0046` n `786`
- 24h: commodity avg `0.1393` n `12`; crypto_alt avg `-1.0101` n `230`; crypto_major avg `0.9051` n `8`; equity avg `2.333` n `113`; fx avg `0.0265` n `6`; index avg `0.1949` n `25`; metal avg `0.1693` n `20`; unknown avg `-0.1755` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2428`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2323`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2073`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
