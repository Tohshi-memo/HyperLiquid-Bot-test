# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T14:22:35.974382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `-0.1251` n `230`; crypto_major avg `-0.1721` n `8`; equity avg `-0.0236` n `96`; fx avg `-0.0008` n `6`; index avg `0.003` n `25`; metal avg `0.0053` n `20`; unknown avg `-0.0009` n `770`
- 1h: commodity avg `-0.0069` n `12`; crypto_alt avg `0.0481` n `230`; crypto_major avg `0.1297` n `8`; equity avg `-0.029` n `96`; fx avg `0.0046` n `6`; index avg `0.001` n `25`; metal avg `0.0102` n `20`; unknown avg `0.0613` n `770`
- 4h: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.1259` n `230`; crypto_major avg `-0.0736` n `8`; equity avg `-0.0305` n `96`; fx avg `0.0246` n `6`; index avg `0.0007` n `25`; metal avg `0.0053` n `20`; unknown avg `0.0145` n `770`
- 24h: commodity avg `0.2133` n `12`; crypto_alt avg `0.3475` n `230`; crypto_major avg `0.8636` n `8`; equity avg `0.2945` n `96`; fx avg `-0.0138` n `6`; index avg `-0.0124` n `25`; metal avg `-0.0556` n `20`; unknown avg `0.1168` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1256`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1225`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.111`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0904`, n `666`, weak_sample_signal
