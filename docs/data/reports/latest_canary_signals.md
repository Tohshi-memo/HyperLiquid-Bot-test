# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T20:08:02.046762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0372` n `12`; crypto_alt avg `-0.0192` n `234`; crypto_major avg `-0.1008` n `8`; equity avg `0.0165` n `141`; fx avg `-0.0002` n `6`; index avg `0.0225` n `26`; metal avg `0.0262` n `20`; unknown avg `0.6557` n `905`
- 1h: commodity avg `0.0826` n `12`; crypto_alt avg `-0.0262` n `234`; crypto_major avg `0.0046` n `8`; equity avg `-0.2987` n `141`; fx avg `0.0047` n `6`; index avg `-0.0302` n `26`; metal avg `-0.0877` n `20`; unknown avg `257.9488` n `905`
- 4h: commodity avg `0.1207` n `12`; crypto_alt avg `-0.4959` n `234`; crypto_major avg `-0.2294` n `8`; equity avg `-0.3957` n `141`; fx avg `-0.014` n `6`; index avg `-0.0386` n `26`; metal avg `0.036` n `20`; unknown avg `5.6666` n `897`
- 24h: commodity avg `0.6431` n `12`; crypto_alt avg `-3.1872` n `234`; crypto_major avg `-3.3217` n `8`; equity avg `-1.6409` n `140`; fx avg `0.0104` n `6`; index avg `-0.3752` n `26`; metal avg `-0.8431` n `20`; unknown avg `13.1526` n `848`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
