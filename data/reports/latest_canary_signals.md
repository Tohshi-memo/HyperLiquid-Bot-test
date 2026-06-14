# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T06:22:38.718722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `-0.1328` n `228`; crypto_major avg `-0.0575` n `8`; equity avg `0.0279` n `74`; fx avg `-0.0124` n `6`; index avg `-0.0317` n `23`; metal avg `0.0063` n `18`; unknown avg `-0.0261` n `645`
- 1h: commodity avg `-0.0199` n `12`; crypto_alt avg `0.5667` n `228`; crypto_major avg `0.1741` n `8`; equity avg `0.0329` n `74`; fx avg `-0.0111` n `6`; index avg `-0.0382` n `23`; metal avg `0.0157` n `18`; unknown avg `-0.2284` n `629`
- 4h: commodity avg `-0.0258` n `12`; crypto_alt avg `-0.3254` n `228`; crypto_major avg `-0.4059` n `8`; equity avg `0.0248` n `74`; fx avg `-0.0278` n `6`; index avg `-0.0849` n `23`; metal avg `0.0182` n `18`; unknown avg `-0.8369` n `613`
- 24h: commodity avg `-0.6672` n `12`; crypto_alt avg `1.795` n `228`; crypto_major avg `1.6401` n `8`; equity avg `0.8159` n `74`; fx avg `-0.0179` n `6`; index avg `0.1564` n `23`; metal avg `0.3426` n `18`; unknown avg `-1.191` n `603`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
