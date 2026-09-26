# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T20:22:33.197719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `-0.2357` n `234`; crypto_major avg `-0.0831` n `8`; equity avg `-0.0192` n `141`; fx avg `-0.0025` n `6`; index avg `-0.0017` n `26`; metal avg `0.0008` n `20`; unknown avg `0.5111` n `961`
- 1h: commodity avg `0.0176` n `12`; crypto_alt avg `-0.4978` n `234`; crypto_major avg `-0.1764` n `8`; equity avg `0.0008` n `141`; fx avg `0.0071` n `6`; index avg `-0.0023` n `26`; metal avg `0.0024` n `20`; unknown avg `156.6773` n `953`
- 4h: commodity avg `0.0333` n `12`; crypto_alt avg `-1.5933` n `234`; crypto_major avg `-0.6957` n `8`; equity avg `-0.0695` n `141`; fx avg `-0.0024` n `6`; index avg `-0.0166` n `26`; metal avg `0.008` n `20`; unknown avg `12.8282` n `953`
- 24h: commodity avg `0.2813` n `12`; crypto_alt avg `0.6266` n `234`; crypto_major avg `-0.849` n `8`; equity avg `0.0412` n `141`; fx avg `0.0101` n `6`; index avg `-0.0332` n `26`; metal avg `-0.0222` n `20`; unknown avg `1.339` n `860`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
