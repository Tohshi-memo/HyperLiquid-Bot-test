# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T10:52:26.161479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `-0.0314` n `230`; crypto_major avg `0.0011` n `8`; equity avg `0.0146` n `98`; fx avg `-0.0064` n `6`; index avg `0.0148` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.0325` n `770`
- 1h: commodity avg `0.1137` n `12`; crypto_alt avg `0.054` n `230`; crypto_major avg `0.0362` n `8`; equity avg `0.0077` n `98`; fx avg `0.0155` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0489` n `20`; unknown avg `0.0197` n `770`
- 4h: commodity avg `-0.4196` n `12`; crypto_alt avg `0.9025` n `230`; crypto_major avg `0.7705` n `8`; equity avg `0.7557` n `98`; fx avg `0.0194` n `6`; index avg `0.1761` n `25`; metal avg `0.2055` n `20`; unknown avg `0.153` n `763`
- 24h: commodity avg `-0.5171` n `12`; crypto_alt avg `0.1887` n `230`; crypto_major avg `-0.2488` n `8`; equity avg `0.5734` n `97`; fx avg `-0.0302` n `6`; index avg `0.1193` n `25`; metal avg `0.2017` n `20`; unknown avg `-0.0646` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0943`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0854`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
