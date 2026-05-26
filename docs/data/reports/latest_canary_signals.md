# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T00:07:16.098311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1704` n `12`; crypto_alt avg `-0.1394` n `228`; crypto_major avg `-0.0576` n `8`; equity avg `-0.4458` n `67`; fx avg `-0.0327` n `6`; index avg `0.0445` n `23`; metal avg `-0.1437` n `18`; unknown avg `-0.0373` n `405`
- 1h: commodity avg `0.2071` n `12`; crypto_alt avg `-0.0532` n `228`; crypto_major avg `-0.0377` n `8`; equity avg `-0.4516` n `67`; fx avg `-0.0493` n `6`; index avg `-0.0044` n `23`; metal avg `-0.5546` n `18`; unknown avg `-0.3438` n `405`
- 4h: commodity avg `0.3204` n `12`; crypto_alt avg `-1.1287` n `228`; crypto_major avg `-0.4979` n `8`; equity avg `-0.7291` n `67`; fx avg `-0.0286` n `6`; index avg `-0.1868` n `23`; metal avg `-0.4393` n `18`; unknown avg `-0.652` n `405`
- 24h: commodity avg `-0.1744` n `12`; crypto_alt avg `1.1305` n `228`; crypto_major avg `-0.2595` n `8`; equity avg `0.1837` n `67`; fx avg `-0.0343` n `6`; index avg `0.4983` n `23`; metal avg `-0.0651` n `18`; unknown avg `0.7608` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
