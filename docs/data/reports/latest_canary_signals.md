# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T03:37:28.135968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.327` n `234`; crypto_major avg `-0.1514` n `8`; equity avg `-0.1164` n `141`; fx avg `0.0048` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0278` n `20`; unknown avg `-0.2496` n `945`
- 1h: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.0167` n `234`; crypto_major avg `-0.1633` n `8`; equity avg `-0.1645` n `141`; fx avg `0.0217` n `6`; index avg `-0.0266` n `26`; metal avg `-0.0542` n `20`; unknown avg `1.6849` n `943`
- 4h: commodity avg `-0.0772` n `12`; crypto_alt avg `0.7554` n `234`; crypto_major avg `-0.2337` n `8`; equity avg `-0.3645` n `141`; fx avg `0.0488` n `6`; index avg `-0.0521` n `26`; metal avg `-0.034` n `20`; unknown avg `1.664` n `937`
- 24h: commodity avg `0.4844` n `12`; crypto_alt avg `-4.7632` n `234`; crypto_major avg `-4.5125` n `8`; equity avg `-1.5698` n `140`; fx avg `0.0973` n `6`; index avg `-0.331` n `26`; metal avg `-0.6373` n `20`; unknown avg `585.6135` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
