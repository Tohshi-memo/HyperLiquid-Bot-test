# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T08:52:26.937144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `-0.0894` n `234`; crypto_major avg `-0.0719` n `8`; equity avg `0.0049` n `141`; fx avg `-0.0019` n `6`; index avg `0.0049` n `26`; metal avg `-0.0056` n `20`; unknown avg `-0.0606` n `961`
- 1h: commodity avg `0.0051` n `12`; crypto_alt avg `-0.1574` n `234`; crypto_major avg `0.2354` n `8`; equity avg `0.086` n `141`; fx avg `-0.0068` n `6`; index avg `0.024` n `26`; metal avg `-0.0132` n `20`; unknown avg `1.6945` n `943`
- 4h: commodity avg `-0.0346` n `12`; crypto_alt avg `1.8137` n `234`; crypto_major avg `1.3472` n `8`; equity avg `0.1937` n `141`; fx avg `-0.0092` n `6`; index avg `0.029` n `26`; metal avg `0.0045` n `20`; unknown avg `4.5934` n `923`
- 24h: commodity avg `0.035` n `12`; crypto_alt avg `1.1851` n `234`; crypto_major avg `0.7495` n `8`; equity avg `0.3894` n `141`; fx avg `0.021` n `6`; index avg `0.0402` n `26`; metal avg `-0.006` n `20`; unknown avg `6.5356` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
