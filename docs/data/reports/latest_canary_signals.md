# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T07:07:29.018600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0446` n `12`; crypto_alt avg `-0.0403` n `230`; crypto_major avg `-0.0098` n `8`; equity avg `0.0321` n `96`; fx avg `0.0014` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.1179` n `770`
- 1h: commodity avg `0.0147` n `12`; crypto_alt avg `0.064` n `230`; crypto_major avg `0.0532` n `8`; equity avg `0.0509` n `96`; fx avg `0.0014` n `6`; index avg `0.0028` n `25`; metal avg `0.0086` n `20`; unknown avg `-0.0804` n `770`
- 4h: commodity avg `0.0293` n `12`; crypto_alt avg `-0.0349` n `230`; crypto_major avg `-0.0193` n `8`; equity avg `0.1186` n `96`; fx avg `0.0078` n `6`; index avg `-0.0282` n `25`; metal avg `0.0195` n `20`; unknown avg `-0.0272` n `752`
- 24h: commodity avg `0.2789` n `12`; crypto_alt avg `0.3491` n `230`; crypto_major avg `1.0967` n `8`; equity avg `0.1273` n `96`; fx avg `-0.01` n `6`; index avg `-0.0103` n `25`; metal avg `-0.007` n `20`; unknown avg `-0.0005` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
