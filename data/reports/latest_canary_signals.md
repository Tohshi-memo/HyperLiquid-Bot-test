# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T17:22:36.987634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0464` n `13`; crypto_alt avg `-0.0218` n `237`; crypto_major avg `0.0234` n `8`; equity avg `-0.0214` n `151`; fx avg `0.0126` n `6`; index avg `-0.0017` n `26`; metal avg `0.0035` n `20`; unknown avg `0.033` n `1196`
- 1h: commodity avg `0.0648` n `13`; crypto_alt avg `-0.0815` n `237`; crypto_major avg `0.0512` n `8`; equity avg `-0.3708` n `151`; fx avg `0.003` n `6`; index avg `-0.0693` n `26`; metal avg `-0.0156` n `20`; unknown avg `-0.0339` n `1194`
- 4h: commodity avg `0.3401` n `13`; crypto_alt avg `-0.2944` n `237`; crypto_major avg `-0.6761` n `8`; equity avg `-0.8295` n `151`; fx avg `-0.0002` n `6`; index avg `-0.0578` n `26`; metal avg `-0.1195` n `20`; unknown avg `-0.0871` n `1133`
- 24h: commodity avg `-0.0192` n `13`; crypto_alt avg `1.3278` n `237`; crypto_major avg `1.516` n `8`; equity avg `2.9017` n `151`; fx avg `-0.0304` n `6`; index avg `0.5456` n `26`; metal avg `0.0764` n `20`; unknown avg `2.9017` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1957`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
