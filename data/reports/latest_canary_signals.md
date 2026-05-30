# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T12:07:18.625578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0638` n `12`; crypto_alt avg `0.0581` n `228`; crypto_major avg `0.0625` n `8`; equity avg `0.0597` n `69`; fx avg `-0.0007` n `6`; index avg `0.0582` n `23`; metal avg `-0.0112` n `18`; unknown avg `0.9989` n `421`
- 1h: commodity avg `0.0704` n `12`; crypto_alt avg `0.034` n `228`; crypto_major avg `0.2173` n `8`; equity avg `0.0804` n `69`; fx avg `-0.0003` n `6`; index avg `0.0592` n `23`; metal avg `-0.03` n `18`; unknown avg `0.8388` n `421`
- 4h: commodity avg `0.145` n `12`; crypto_alt avg `0.0608` n `228`; crypto_major avg `0.3498` n `8`; equity avg `0.1581` n `69`; fx avg `0.0197` n `6`; index avg `0.0019` n `23`; metal avg `0.0172` n `18`; unknown avg `0.8323` n `421`
- 24h: commodity avg `-0.1898` n `12`; crypto_alt avg `2.224` n `228`; crypto_major avg `2.7111` n `8`; equity avg `1.4456` n `69`; fx avg `0.1101` n `6`; index avg `0.0502` n `23`; metal avg `-0.0201` n `18`; unknown avg `0.8453` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
