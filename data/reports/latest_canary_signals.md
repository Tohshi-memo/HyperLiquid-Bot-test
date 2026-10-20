# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T02:07:32.536205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0282` n `13`; crypto_alt avg `-0.4144` n `237`; crypto_major avg `-0.2987` n `8`; equity avg `-0.1699` n `151`; fx avg `0.0076` n `6`; index avg `-0.0274` n `26`; metal avg `0.0458` n `20`; unknown avg `-0.3852` n `1196`
- 1h: commodity avg `-0.04` n `13`; crypto_alt avg `-0.0138` n `237`; crypto_major avg `0.0109` n `8`; equity avg `0.2471` n `151`; fx avg `0.0157` n `6`; index avg `0.052` n `26`; metal avg `0.0797` n `20`; unknown avg `1.7385` n `1196`
- 4h: commodity avg `0.0835` n `13`; crypto_alt avg `-0.4995` n `237`; crypto_major avg `-0.6614` n `8`; equity avg `-0.8216` n `151`; fx avg `-0.0319` n `6`; index avg `-0.1626` n `26`; metal avg `-0.0613` n `20`; unknown avg `-0.1395` n `1188`
- 24h: commodity avg `0.1897` n `13`; crypto_alt avg `-0.7319` n `237`; crypto_major avg `-0.8286` n `8`; equity avg `-0.6604` n `151`; fx avg `-0.0312` n `6`; index avg `-0.0893` n `26`; metal avg `-0.3076` n `20`; unknown avg `4.9705` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
