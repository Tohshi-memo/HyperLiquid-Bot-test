# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T22:22:29.671389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `-0.0191` n `230`; crypto_major avg `-0.1246` n `8`; equity avg `-0.0229` n `112`; fx avg `-0.0031` n `6`; index avg `0.008` n `25`; metal avg `-0.0365` n `20`; unknown avg `0.0568` n `785`
- 1h: commodity avg `0.2275` n `12`; crypto_alt avg `0.2872` n `230`; crypto_major avg `0.2585` n `8`; equity avg `-0.1213` n `112`; fx avg `0.0055` n `6`; index avg `-0.0349` n `25`; metal avg `-0.1414` n `20`; unknown avg `0.2779` n `785`
- 4h: commodity avg `0.4345` n `12`; crypto_alt avg `0.4484` n `230`; crypto_major avg `0.1951` n `8`; equity avg `-0.0877` n `112`; fx avg `-0.0048` n `6`; index avg `-0.0388` n `25`; metal avg `-0.1512` n `20`; unknown avg `-0.3974` n `785`
- 24h: commodity avg `0.4675` n `12`; crypto_alt avg `1.7139` n `230`; crypto_major avg `0.499` n `8`; equity avg `0.0831` n `112`; fx avg `0.001` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0801` n `20`; unknown avg `-0.3009` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
