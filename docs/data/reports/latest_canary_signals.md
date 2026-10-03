# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T10:52:24.541023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0997` n `13`; crypto_alt avg `0.0547` n `235`; crypto_major avg `0.0014` n `8`; equity avg `0.002` n `143`; fx avg `-0.0018` n `6`; index avg `0.0034` n `26`; metal avg `-0.0029` n `20`; unknown avg `-0.0141` n `984`
- 1h: commodity avg `-0.0166` n `13`; crypto_alt avg `0.3816` n `235`; crypto_major avg `0.0408` n `8`; equity avg `0.0243` n `143`; fx avg `-0.0017` n `6`; index avg `0.0053` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.018` n `982`
- 4h: commodity avg `0.037` n `13`; crypto_alt avg `0.158` n `235`; crypto_major avg `-0.027` n `8`; equity avg `0.041` n `143`; fx avg `-0.0031` n `6`; index avg `0.0062` n `26`; metal avg `-0.008` n `20`; unknown avg `1.3156` n `966`
- 24h: commodity avg `0.6063` n `13`; crypto_alt avg `-1.7607` n `235`; crypto_major avg `-2.2732` n `8`; equity avg `0.1454` n `142`; fx avg `0.0074` n `6`; index avg `0.1352` n `26`; metal avg `-0.3186` n `20`; unknown avg `-0.2856` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
