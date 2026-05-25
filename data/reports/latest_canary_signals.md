# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T19:52:17.006650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0456` n `12`; crypto_alt avg `0.1234` n `228`; crypto_major avg `0.0609` n `8`; equity avg `0.0663` n `67`; fx avg `0.0038` n `6`; index avg `0.1569` n `23`; metal avg `0.0203` n `18`; unknown avg `0.1035` n `405`
- 1h: commodity avg `-0.3541` n `12`; crypto_alt avg `-0.2475` n `228`; crypto_major avg `-0.1345` n `8`; equity avg `0.002` n `67`; fx avg `0.0097` n `6`; index avg `0.128` n `23`; metal avg `0.0041` n `18`; unknown avg `0.7287` n `405`
- 4h: commodity avg `-0.2377` n `12`; crypto_alt avg `0.1207` n `228`; crypto_major avg `-0.3976` n `8`; equity avg `0.0578` n `67`; fx avg `0.01` n `6`; index avg `0.1567` n `23`; metal avg `0.0909` n `18`; unknown avg `-0.1424` n `405`
- 24h: commodity avg `-1.191` n `12`; crypto_alt avg `2.0957` n `228`; crypto_major avg `0.2882` n `8`; equity avg `0.8491` n `67`; fx avg `-0.0207` n `6`; index avg `0.6411` n `23`; metal avg `1.6481` n `18`; unknown avg `1.2578` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
