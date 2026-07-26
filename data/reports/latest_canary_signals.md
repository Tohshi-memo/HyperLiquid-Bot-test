# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T08:07:25.119847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `0.064` n `230`; crypto_major avg `-0.0178` n `8`; equity avg `-0.0033` n `100`; fx avg `-0.036` n `6`; index avg `-0.006` n `25`; metal avg `0.0063` n `20`; unknown avg `0.0449` n `775`
- 1h: commodity avg `-0.0416` n `12`; crypto_alt avg `-0.0486` n `230`; crypto_major avg `-0.2139` n `8`; equity avg `-0.0543` n `100`; fx avg `-0.041` n `6`; index avg `-0.0037` n `25`; metal avg `0.0231` n `20`; unknown avg `-0.0008` n `775`
- 4h: commodity avg `-0.0588` n `12`; crypto_alt avg `0.4526` n `230`; crypto_major avg `0.0293` n `8`; equity avg `-0.0261` n `100`; fx avg `-0.0116` n `6`; index avg `-0.009` n `25`; metal avg `0.0249` n `20`; unknown avg `0.0344` n `759`
- 24h: commodity avg `-0.5857` n `12`; crypto_alt avg `1.9125` n `230`; crypto_major avg `1.8371` n `8`; equity avg `0.5295` n `100`; fx avg `0.0049` n `6`; index avg `0.1173` n `25`; metal avg `0.0721` n `20`; unknown avg `0.0787` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1425`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1277`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1246`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1235`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1207`, n `666`, weak_sample_signal
