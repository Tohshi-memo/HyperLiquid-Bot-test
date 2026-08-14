# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T00:37:24.498185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.0865` n `230`; crypto_major avg `-0.0733` n `8`; equity avg `0.1208` n `113`; fx avg `-0.0091` n `6`; index avg `0.0181` n `25`; metal avg `-0.0394` n `20`; unknown avg `0.8247` n `787`
- 1h: commodity avg `0.0038` n `12`; crypto_alt avg `0.0093` n `230`; crypto_major avg `-0.0058` n `8`; equity avg `0.011` n `113`; fx avg `-0.0109` n `6`; index avg `0.005` n `25`; metal avg `-0.1168` n `20`; unknown avg `4.7126` n `787`
- 4h: commodity avg `0.0301` n `12`; crypto_alt avg `0.3255` n `230`; crypto_major avg `-0.09` n `8`; equity avg `0.1686` n `113`; fx avg `-0.0132` n `6`; index avg `0.0386` n `25`; metal avg `-0.0576` n `20`; unknown avg `4.7148` n `787`
- 24h: commodity avg `-0.3439` n `12`; crypto_alt avg `0.1583` n `230`; crypto_major avg `0.4182` n `8`; equity avg `1.4919` n `113`; fx avg `0.0729` n `6`; index avg `0.3428` n `25`; metal avg `-0.7599` n `20`; unknown avg `7.7259` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2431`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
