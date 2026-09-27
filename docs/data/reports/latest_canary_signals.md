# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T03:37:31.389554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `0.003` n `234`; crypto_major avg `-0.0081` n `8`; equity avg `0.0106` n `141`; fx avg `0.0014` n `6`; index avg `0.0008` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.2824` n `961`
- 1h: commodity avg `0.0307` n `12`; crypto_alt avg `-0.2607` n `234`; crypto_major avg `-0.2381` n `8`; equity avg `0.0039` n `141`; fx avg `-0.0041` n `6`; index avg `0.0061` n `26`; metal avg `-0.0072` n `20`; unknown avg `-0.0469` n `959`
- 4h: commodity avg `-0.0458` n `12`; crypto_alt avg `-0.232` n `234`; crypto_major avg `-0.1426` n `8`; equity avg `0.077` n `141`; fx avg `-0.0055` n `6`; index avg `0.0076` n `26`; metal avg `-0.0075` n `20`; unknown avg `-0.1195` n `947`
- 24h: commodity avg `-0.0197` n `12`; crypto_alt avg `0.7372` n `234`; crypto_major avg `-0.4348` n `8`; equity avg `0.2541` n `141`; fx avg `0.0032` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0106` n `20`; unknown avg `4.2216` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
