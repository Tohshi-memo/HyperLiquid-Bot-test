# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T09:37:28.248208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0737` n `12`; crypto_alt avg `-0.3608` n `233`; crypto_major avg `-0.347` n `8`; equity avg `-0.057` n `136`; fx avg `-0.0003` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0091` n `20`; unknown avg `-0.0998` n `796`
- 1h: commodity avg `-0.1046` n `12`; crypto_alt avg `-0.6353` n `233`; crypto_major avg `-0.5556` n `8`; equity avg `-0.0607` n `136`; fx avg `-0.0131` n `6`; index avg `-0.0107` n `26`; metal avg `-0.0788` n `20`; unknown avg `0.0209` n `794`
- 4h: commodity avg `-0.3329` n `12`; crypto_alt avg `-0.5314` n `233`; crypto_major avg `-0.2832` n `8`; equity avg `0.5802` n `136`; fx avg `-0.0624` n `6`; index avg `0.1299` n `26`; metal avg `0.0487` n `20`; unknown avg `0.3893` n `762`
- 24h: commodity avg `0.272` n `12`; crypto_alt avg `-1.402` n `233`; crypto_major avg `-1.5925` n `8`; equity avg `-0.8781` n `136`; fx avg `-0.0584` n `6`; index avg `-0.1092` n `26`; metal avg `-0.8252` n `20`; unknown avg `1.3323` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
