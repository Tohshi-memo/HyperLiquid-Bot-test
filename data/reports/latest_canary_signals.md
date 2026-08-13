# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T07:58:32.672368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `-0.1393` n `230`; crypto_major avg `-0.0847` n `8`; equity avg `0.0449` n `113`; fx avg `0.0105` n `6`; index avg `-0.0045` n `25`; metal avg `-0.053` n `20`; unknown avg `-0.046` n `787`
- 1h: commodity avg `-0.1489` n `12`; crypto_alt avg `-0.0601` n `230`; crypto_major avg `0.0275` n `8`; equity avg `-0.0799` n `113`; fx avg `-0.0095` n `6`; index avg `-0.0102` n `25`; metal avg `-0.1277` n `20`; unknown avg `0.0107` n `787`
- 4h: commodity avg `-0.046` n `12`; crypto_alt avg `0.0518` n `230`; crypto_major avg `0.3993` n `8`; equity avg `-0.4471` n `113`; fx avg `0.0675` n `6`; index avg `-0.0633` n `25`; metal avg `-0.3184` n `20`; unknown avg `0.0051` n `755`
- 24h: commodity avg `-0.2946` n `12`; crypto_alt avg `-0.5263` n `230`; crypto_major avg `0.396` n `8`; equity avg `1.8696` n `113`; fx avg `0.0095` n `6`; index avg `0.2445` n `25`; metal avg `-0.5298` n `20`; unknown avg `0.0375` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2484`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
