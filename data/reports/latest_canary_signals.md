# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T05:52:25.516113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0612` n `12`; crypto_alt avg `0.0432` n `233`; crypto_major avg `0.0713` n `8`; equity avg `0.184` n `136`; fx avg `-0.0218` n `6`; index avg `0.0409` n `26`; metal avg `0.0357` n `20`; unknown avg `0.1074` n `796`
- 1h: commodity avg `-0.2489` n `12`; crypto_alt avg `-0.0654` n `233`; crypto_major avg `0.0945` n `8`; equity avg `0.2728` n `136`; fx avg `-0.0053` n `6`; index avg `0.0368` n `26`; metal avg `0.1427` n `20`; unknown avg `16.4892` n `794`
- 4h: commodity avg `-0.3421` n `12`; crypto_alt avg `0.6052` n `233`; crypto_major avg `0.498` n `8`; equity avg `0.2591` n `136`; fx avg `-0.0648` n `6`; index avg `0.1235` n `26`; metal avg `0.2241` n `20`; unknown avg `25.668` n `782`
- 24h: commodity avg `0.8663` n `12`; crypto_alt avg `-1.7521` n `233`; crypto_major avg `-1.919` n `8`; equity avg `-1.7065` n `136`; fx avg `0.0331` n `6`; index avg `-0.2812` n `26`; metal avg `-1.1652` n `20`; unknown avg `-0.273` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
