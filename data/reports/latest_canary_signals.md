# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T09:07:25.506772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0561` n `12`; crypto_alt avg `-0.0555` n `230`; crypto_major avg `-0.0892` n `8`; equity avg `-0.0244` n `113`; fx avg `0.0011` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0175` n `20`; unknown avg `0.0303` n `787`
- 1h: commodity avg `-0.1588` n `12`; crypto_alt avg `-0.0894` n `230`; crypto_major avg `-0.3334` n `8`; equity avg `-0.0411` n `113`; fx avg `-0.0027` n `6`; index avg `-0.005` n `25`; metal avg `0.0458` n `20`; unknown avg `0.5651` n `787`
- 4h: commodity avg `-0.3123` n `12`; crypto_alt avg `-0.0664` n `230`; crypto_major avg `-0.1562` n `8`; equity avg `-0.7132` n `113`; fx avg `0.0828` n `6`; index avg `-0.079` n `25`; metal avg `-0.2845` n `20`; unknown avg `-0.0176` n `755`
- 24h: commodity avg `-0.4028` n `12`; crypto_alt avg `-0.3851` n `230`; crypto_major avg `0.0945` n `8`; equity avg `1.2847` n `113`; fx avg `0.0179` n `6`; index avg `0.1435` n `25`; metal avg `-0.5332` n `20`; unknown avg `0.7414` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2447`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
