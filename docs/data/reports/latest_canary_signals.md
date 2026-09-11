# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T07:22:27.073965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `0.1697` n `233`; crypto_major avg `0.0313` n `8`; equity avg `-0.0572` n `136`; fx avg `0.0144` n `6`; index avg `-0.0109` n `26`; metal avg `-0.0196` n `20`; unknown avg `0.0968` n `794`
- 1h: commodity avg `-0.0921` n `12`; crypto_alt avg `0.136` n `233`; crypto_major avg `0.1241` n `8`; equity avg `0.1175` n `136`; fx avg `0.0135` n `6`; index avg `0.0314` n `26`; metal avg `-0.0299` n `20`; unknown avg `0.8304` n `792`
- 4h: commodity avg `-0.4231` n `12`; crypto_alt avg `1.1018` n `233`; crypto_major avg `0.9304` n `8`; equity avg `0.9499` n `136`; fx avg `0.0062` n `6`; index avg `0.1944` n `26`; metal avg `0.3692` n `20`; unknown avg `42.4682` n `762`
- 24h: commodity avg `0.7929` n `12`; crypto_alt avg `-0.984` n `233`; crypto_major avg `-1.2112` n `8`; equity avg `-1.3724` n `136`; fx avg `0.0527` n `6`; index avg `-0.2372` n `26`; metal avg `-0.9663` n `20`; unknown avg `0.6195` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
