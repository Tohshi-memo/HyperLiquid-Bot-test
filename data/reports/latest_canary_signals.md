# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T10:22:32.581452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0376` n `12`; crypto_alt avg `0.0488` n `230`; crypto_major avg `0.0124` n `8`; equity avg `0.0547` n `100`; fx avg `0.0057` n `6`; index avg `0.0257` n `25`; metal avg `0.0104` n `20`; unknown avg `0.0032` n `775`
- 1h: commodity avg `-0.2066` n `12`; crypto_alt avg `0.0378` n `230`; crypto_major avg `0.0075` n `8`; equity avg `0.1008` n `100`; fx avg `0.0027` n `6`; index avg `0.0445` n `25`; metal avg `0.0179` n `20`; unknown avg `-0.0152` n `775`
- 4h: commodity avg `-0.4286` n `12`; crypto_alt avg `0.3643` n `230`; crypto_major avg `0.3495` n `8`; equity avg `0.1606` n `100`; fx avg `-0.0403` n `6`; index avg `0.0578` n `25`; metal avg `0.0879` n `20`; unknown avg `-0.0391` n `775`
- 24h: commodity avg `-0.8786` n `12`; crypto_alt avg `1.5826` n `230`; crypto_major avg `1.6492` n `8`; equity avg `0.6646` n `100`; fx avg `0.0089` n `6`; index avg `0.1718` n `25`; metal avg `0.1389` n `20`; unknown avg `0.0557` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1457`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1342`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1305`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1241`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1239`, n `666`, weak_sample_signal
