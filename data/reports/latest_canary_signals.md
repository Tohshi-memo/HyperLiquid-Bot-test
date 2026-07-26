# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T16:37:28.694853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `0.1388` n `230`; crypto_major avg `0.1754` n `8`; equity avg `0.0641` n `100`; fx avg `0.0042` n `6`; index avg `0.0054` n `25`; metal avg `0.0244` n `20`; unknown avg `-0.1613` n `775`
- 1h: commodity avg `0.0055` n `12`; crypto_alt avg `0.2783` n `230`; crypto_major avg `0.2001` n `8`; equity avg `0.0328` n `100`; fx avg `-0.0072` n `6`; index avg `0.0241` n `25`; metal avg `0.0319` n `20`; unknown avg `-0.1216` n `775`
- 4h: commodity avg `0.0067` n `12`; crypto_alt avg `0.3625` n `230`; crypto_major avg `0.6188` n `8`; equity avg `0.2006` n `100`; fx avg `-0.0175` n `6`; index avg `0.0293` n `25`; metal avg `0.0523` n `20`; unknown avg `0.1122` n `775`
- 24h: commodity avg `-0.477` n `12`; crypto_alt avg `1.3995` n `230`; crypto_major avg `1.5098` n `8`; equity avg `0.9164` n `100`; fx avg `0.0281` n `6`; index avg `0.2138` n `25`; metal avg `0.22` n `20`; unknown avg `0.0344` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
