# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T09:22:24.586320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.2752` n `230`; crypto_major avg `-0.2674` n `8`; equity avg `-0.0865` n `96`; fx avg `0.0006` n `6`; index avg `0.0021` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.0364` n `770`
- 1h: commodity avg `0.0243` n `12`; crypto_alt avg `-0.1123` n `230`; crypto_major avg `-0.0662` n `8`; equity avg `-0.0543` n `96`; fx avg `-0.0239` n `6`; index avg `0.0205` n `25`; metal avg `-0.0323` n `20`; unknown avg `-0.0869` n `770`
- 4h: commodity avg `0.0648` n `12`; crypto_alt avg `-0.1826` n `230`; crypto_major avg `-0.0822` n `8`; equity avg `0.1064` n `96`; fx avg `0.0002` n `6`; index avg `0.0455` n `25`; metal avg `-0.0454` n `20`; unknown avg `0.0079` n `752`
- 24h: commodity avg `0.3214` n `12`; crypto_alt avg `0.5483` n `230`; crypto_major avg `1.144` n `8`; equity avg `0.2553` n `96`; fx avg `-0.0214` n `6`; index avg `-0.0382` n `25`; metal avg `-0.0803` n `20`; unknown avg `0.0412` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
