# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T06:52:21.866908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.0334` n `231`; crypto_major avg `-0.0179` n `8`; equity avg `-0.0027` n `128`; fx avg `-0.002` n `6`; index avg `-0.0023` n `26`; metal avg `0.0014` n `20`; unknown avg `-0.0023` n `791`
- 1h: commodity avg `0.0141` n `12`; crypto_alt avg `0.1503` n `231`; crypto_major avg `0.116` n `8`; equity avg `0.0014` n `128`; fx avg `0.0047` n `6`; index avg `-0.011` n `26`; metal avg `0.0078` n `20`; unknown avg `-0.0323` n `759`
- 4h: commodity avg `0.0138` n `12`; crypto_alt avg `0.2939` n `231`; crypto_major avg `-0.0055` n `8`; equity avg `0.0414` n `128`; fx avg `0.0123` n `6`; index avg `0.0` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.008` n `759`
- 24h: commodity avg `0.0513` n `12`; crypto_alt avg `0.9538` n `231`; crypto_major avg `1.1022` n `8`; equity avg `0.3062` n `128`; fx avg `0.0147` n `6`; index avg `0.0563` n `26`; metal avg `0.1039` n `20`; unknown avg `0.7945` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
