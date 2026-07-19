# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T10:52:28.591723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: crypto_alt avg `0.1806` n `225`; crypto_major avg `0.1333` n `7`; metal avg `0.0325` n `1`; unknown avg `-0.0048` n `703`
- 1h: commodity avg `-0.0088` n `12`; crypto_alt avg `0.2191` n `230`; crypto_major avg `0.1646` n `8`; equity avg `-0.0519` n `96`; fx avg `0.022` n `6`; index avg `-0.0007` n `25`; metal avg `0.0008` n `20`; unknown avg `0.083` n `770`
- 4h: commodity avg `-0.0048` n `12`; crypto_alt avg `0.0775` n `230`; crypto_major avg `0.1388` n `8`; equity avg `0.0475` n `96`; fx avg `0.0145` n `6`; index avg `0.0271` n `25`; metal avg `-0.0572` n `20`; unknown avg `-0.059` n `770`
- 24h: commodity avg `0.2156` n `12`; crypto_alt avg `0.5972` n `230`; crypto_major avg `1.1695` n `8`; equity avg `0.176` n `96`; fx avg `0.0006` n `6`; index avg `-0.0317` n `25`; metal avg `-0.0777` n `20`; unknown avg `0.1423` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1114`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.111`, n `667`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `667`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
