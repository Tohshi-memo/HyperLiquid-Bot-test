# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T07:22:25.313350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `12`; crypto_alt avg `0.0064` n `230`; crypto_major avg `0.0109` n `8`; equity avg `-0.0097` n `96`; fx avg `0.0105` n `6`; index avg `0.0223` n `25`; metal avg `-0.0077` n `20`; unknown avg `0.0221` n `770`
- 1h: commodity avg `0.0203` n `12`; crypto_alt avg `0.0325` n `230`; crypto_major avg `-0.0063` n `8`; equity avg `0.0173` n `96`; fx avg `0.0036` n `6`; index avg `0.0244` n `25`; metal avg `0.001` n `20`; unknown avg `-0.0656` n `770`
- 4h: commodity avg `-0.0151` n `12`; crypto_alt avg `0.159` n `230`; crypto_major avg `0.1443` n `8`; equity avg `0.1582` n `96`; fx avg `0.0203` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.0127` n `752`
- 24h: commodity avg `0.3015` n `12`; crypto_alt avg `0.3343` n `230`; crypto_major avg `0.9979` n `8`; equity avg `0.0567` n `96`; fx avg `-0.0068` n `6`; index avg `0.0047` n `25`; metal avg `-0.0205` n `20`; unknown avg `0.0581` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
