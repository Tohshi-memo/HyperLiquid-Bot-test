# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T23:37:26.110864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.0137` n `230`; crypto_major avg `0.0554` n `8`; equity avg `0.0418` n `98`; fx avg `0.0037` n `6`; index avg `0.0323` n `25`; metal avg `0.0059` n `20`; unknown avg `2.5255` n `769`
- 1h: commodity avg `-0.0692` n `12`; crypto_alt avg `-0.0796` n `230`; crypto_major avg `0.0671` n `8`; equity avg `-0.0011` n `98`; fx avg `0.0046` n `6`; index avg `0.0287` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.9147` n `769`
- 4h: commodity avg `0.0101` n `12`; crypto_alt avg `0.2271` n `230`; crypto_major avg `0.3209` n `8`; equity avg `0.1976` n `98`; fx avg `0.0177` n `6`; index avg `0.094` n `25`; metal avg `-0.1479` n `20`; unknown avg `-0.0376` n `769`
- 24h: commodity avg `-0.0145` n `12`; crypto_alt avg `-0.168` n `230`; crypto_major avg `0.3197` n `8`; equity avg `0.5358` n `97`; fx avg `0.0886` n `6`; index avg `0.0312` n `25`; metal avg `-0.1127` n `20`; unknown avg `0.0033` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1421`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1354`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.126`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0953`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0949`, n `666`, weak_sample_signal
