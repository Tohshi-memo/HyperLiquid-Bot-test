# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T18:37:29.420321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.062` n `12`; crypto_alt avg `-0.143` n `230`; crypto_major avg `-0.1202` n `8`; equity avg `-0.0174` n `113`; fx avg `0.0005` n `6`; index avg `0.0122` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0834` n `787`
- 1h: commodity avg `-0.1399` n `12`; crypto_alt avg `-0.0931` n `230`; crypto_major avg `-0.0952` n `8`; equity avg `-0.1166` n `113`; fx avg `0.0007` n `6`; index avg `-0.0183` n `25`; metal avg `-0.0154` n `20`; unknown avg `-0.0649` n `787`
- 4h: commodity avg `0.0334` n `12`; crypto_alt avg `-1.0364` n `230`; crypto_major avg `-0.7414` n `8`; equity avg `-0.1835` n `113`; fx avg `0.0074` n `6`; index avg `-0.0059` n `25`; metal avg `-0.0341` n `20`; unknown avg `-0.0053` n `787`
- 24h: commodity avg `-0.5728` n `12`; crypto_alt avg `-0.8678` n `230`; crypto_major avg `-0.279` n `8`; equity avg `1.1992` n `113`; fx avg `0.0039` n `6`; index avg `0.3017` n `25`; metal avg `-0.4619` n `20`; unknown avg `-0.0344` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2342`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
