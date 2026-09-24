# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T15:07:39.334673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2559` n `12`; crypto_alt avg `0.5283` n `234`; crypto_major avg `0.4089` n `8`; equity avg `-0.1076` n `141`; fx avg `0.0127` n `6`; index avg `-0.0375` n `26`; metal avg `-0.0938` n `20`; unknown avg `1.5357` n `895`
- 1h: commodity avg `0.672` n `12`; crypto_alt avg `0.0813` n `234`; crypto_major avg `-0.2501` n `8`; equity avg `-0.2685` n `141`; fx avg `0.019` n `6`; index avg `-0.0853` n `26`; metal avg `-0.1685` n `20`; unknown avg `45.2328` n `895`
- 4h: commodity avg `0.6312` n `12`; crypto_alt avg `2.1638` n `234`; crypto_major avg `1.0002` n `8`; equity avg `0.0029` n `141`; fx avg `-0.0085` n `6`; index avg `-0.0268` n `26`; metal avg `-0.0864` n `20`; unknown avg `5.2729` n `889`
- 24h: commodity avg `1.1927` n `12`; crypto_alt avg `0.3924` n `234`; crypto_major avg `-0.752` n `8`; equity avg `-1.5721` n `141`; fx avg `0.0248` n `6`; index avg `-0.2923` n `26`; metal avg `-0.363` n `20`; unknown avg `265.5525` n `823`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
