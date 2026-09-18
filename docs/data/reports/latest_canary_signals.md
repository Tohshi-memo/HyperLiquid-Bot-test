# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T23:22:31.054541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `0.176` n `234`; crypto_major avg `0.0255` n `8`; equity avg `-0.0076` n `140`; fx avg `0.0151` n `6`; index avg `0.0009` n `26`; metal avg `-0.0024` n `20`; unknown avg `-0.0207` n `942`
- 1h: commodity avg `0.0325` n `12`; crypto_alt avg `0.0403` n `234`; crypto_major avg `-0.1476` n `8`; equity avg `-0.066` n `140`; fx avg `0.0206` n `6`; index avg `-0.0048` n `26`; metal avg `0.003` n `20`; unknown avg `0.0844` n `940`
- 4h: commodity avg `0.0233` n `12`; crypto_alt avg `0.5408` n `234`; crypto_major avg `-0.0599` n `8`; equity avg `0.2705` n `140`; fx avg `0.059` n `6`; index avg `0.0573` n `26`; metal avg `-0.025` n `20`; unknown avg `0.4572` n `872`
- 24h: commodity avg `-0.0675` n `12`; crypto_alt avg `6.7062` n `234`; crypto_major avg `6.627` n `8`; equity avg `1.3143` n `140`; fx avg `0.2591` n `6`; index avg `0.0508` n `26`; metal avg `0.339` n `20`; unknown avg `4.1266` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
