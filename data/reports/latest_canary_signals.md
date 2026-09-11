# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T08:52:40.836839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.04` n `12`; crypto_alt avg `-0.0809` n `233`; crypto_major avg `-0.0081` n `8`; equity avg `0.0558` n `136`; fx avg `-0.0016` n `6`; index avg `0.0058` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.0008` n `796`
- 1h: commodity avg `-0.2132` n `12`; crypto_alt avg `0.1606` n `233`; crypto_major avg `0.2603` n `8`; equity avg `0.3174` n `136`; fx avg `-0.0544` n `6`; index avg `0.0785` n `26`; metal avg `0.0773` n `20`; unknown avg `0.0245` n `788`
- 4h: commodity avg `-0.4549` n `12`; crypto_alt avg `-0.0853` n `233`; crypto_major avg `0.2899` n `8`; equity avg `0.7871` n `136`; fx avg `-0.0345` n `6`; index avg `0.1424` n `26`; metal avg `0.2297` n `20`; unknown avg `0.8231` n `762`
- 24h: commodity avg `0.4349` n `12`; crypto_alt avg `-1.0364` n `233`; crypto_major avg `-1.2047` n `8`; equity avg `-0.8808` n `136`; fx avg `-0.037` n `6`; index avg `-0.126` n `26`; metal avg `-0.8035` n `20`; unknown avg `1.3966` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
